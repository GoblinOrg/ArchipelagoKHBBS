import logging

import yaml
import os
import Utils
import zipfile

from .Locations import KHBBSLocation, location_table
from .Items import KHBBSItem, item_table
from worlds.Files import APContainer


class KHBBSContainer(APContainer):
    game: str = 'Kingdom Hearts Birth by Sleep'

    def __init__(self, patch_data: dict, base_path: str, output_directory: str,
        player=None, player_name: str = "", server: str = ""):
        self.patch_data = patch_data
        self.file_path = base_path
        container_path = os.path.join(output_directory, base_path + ".zip")
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        for filename, text in self.patch_data.items():
            opened_zipfile.writestr(filename, text)
        super().write_contents(opened_zipfile)


def patch_khbbs(self, output_directory, character):
    mod_name = f"AP-{self.multiworld.seed_name}-P{self.player}-{self.multiworld.get_file_safe_player_name(self.player)}"
    mod_dir = os.path.join(output_directory, mod_name + "_" + Utils.__version__)
    
    seed_lua = build_seed_lua(self, character)
    
    self.mod_yml = {
        "assets": [
            {
                'method': 'copy',
                'name':   'scripts/seed.lua',
                'source': [
                    {
                        'name': 'seed.lua',
                    }
                ]
            }
        ],
        'title':  'BBSFMAP Randomizer Seed'
    }
    
    openkhmod = {
        "mod.yml":  yaml.dump(self.mod_yml, line_break="\n"),
        "seed.lua": seed_lua,
    }

    mod = KHBBSContainer(openkhmod, mod_dir, output_directory, self.player,
            self.multiworld.get_file_safe_player_name(self.player))
    mod.write()

def build_seed_lua(self, character):
    seed_lua = get_lua_header()
    seed_lua = seed_lua + get_lua_character_check(character)
    seed_lua = seed_lua + get_lua_field_item_pointer(self)
    seed_lua = seed_lua + get_sticker_replace(self)
    seed_lua = seed_lua + get_chest_replace(self)
    seed_lua = seed_lua + get_end(self)
    return seed_lua

def get_lua_header():
    return """LUAGUI_NAME = "bbsAPSeed"
LUAGUI_AUTH = "Gicu"
LUAGUI_DESC = "BBS FM AP Seed"

game_version = 1 --1 for 1.0.0.9 EGS, 2 for Steam
IsEpicGLVersion = 0x6107D4
IsSteamGLVersion = 0x6107B4
IsSteamJPVersion = 0x610534
can_execute = false
frame_count = 0
patched = false

function version_choice(array, choice)
    a = array
    return a[choice]
end

function _OnInit()
    if ReadByte(IsEpicGLVersion) == 0xFF then
        game_version = 1
        ConsolePrint("EGS Version Detected")
        can_execute = true
    end
    if ReadByte(IsSteamGLVersion) == 0xFF then
        game_version = 2
        ConsolePrint("Steam Version Detected")
        can_execute = true
    end
    if can_execute then
    end
end

function _OnFrame()
    frame_count = (frame_count + 1) % 30
    if can_execute and frame_count == 0 then
        if ReadInt(version_choice({0x0, 0x81711F}, game_version)) ~= 0xFFFFFF00 then --Not on Title Screen
            if ReadInt(version_choice({0x0, 0x81711F}, game_version)) ~= 0xD0100 then
                if ReadInt(version_choice({0x0, 0x81711F}, game_version)) ~= 0x20100 or ReadInt(version_choice({0x0, 0x817123}, game_version)) ~= 0x100 or ReadShort(version_choice({0x0, 0x817127}, game_version)) ~= 0x100 then\n"""

def get_lua_character_check(character):
    return """                    if ReadByte(version_choice({0x0, 0x10F9F800}, game_version)) == 0x0""" + str(character) + """ then\n"""

def get_lua_field_item_pointer(self):
    return """                        field_item_address_pointer = GetPointer(version_choice({0x0, 0x10F9F3C0}, game_version))
                        if field_item_address_pointer > 0 and not patched then\n"""

def get_sticker_replace(self):
    replace_stickers_str = ""
    for location in self.multiworld.get_filled_locations(self.player):
        location_data = location_table[location.name]
        if location_data.type == "Sticker":
            write_value = "00000"
            replace_stickers_str = replace_stickers_str + ("    " * 7) + "WriteInt(field_item_address_pointer + (" + str(location_data.offset) + "), 0x"
            if self.player == location.item.player:
                item_data = item_table[location.item.name]
                if item_data.category == "Key Item":
                    write_value = get_world_offset(location_data.category) + item_data.khbbsid
            replace_stickers_str = replace_stickers_str + write_value + ", true)\n"
    return replace_stickers_str

def get_chest_replace(self):
    replace_chests_str = ""
    for location in self.multiworld.get_filled_locations(self.player):
        location_data = location_table[location.name]
        if location_data.type == "Chest":
            write_value = "0000000"
            replace_chests_str = replace_chests_str + ("    " * 7) + "WriteInt(field_item_address_pointer + (" + str(location_data.offset) + "), 0x"
            if self.player == location.item.player:
                item_data = item_table[location.item.name]
                if item_data.category in ["Attack Command", "Magic Command", "Item Command", "Friendship Command", "Movement Command", "Defense Command", "Reprisal Command", "Shotlock Command"] and not location_data.forced_remote:
                    item_prefix = "01"
                    write_value = get_world_offset(location_data.category) + item_prefix + item_data.khbbsid
                elif item_data.category in ["Key Item"] and not location_data.forced_remote:
                    item_prefix = "00"
                    write_value = get_world_offset(location_data.category) + item_prefix + item_data.khbbsid
            replace_chests_str = replace_chests_str + write_value + ", true)\n"
    return replace_chests_str

def get_end(self):
    return """                            patched = true
                        end
                    end
                end
            end
        end
    end
end"""

def get_world_offset(world):
    world_offsets = {
        "The Land of Departure":  "1",
        "Dwarf Woodlands":        "2",
        "Castle of Dreams":       "3",
        "Enchanted Dominion":     "4",
        "The Mysterious Tower":   "5",
        "Radiant Garden":         "6",
        "Realm of Darkness":      "7",
        "Olympus Coliseum":       "8",
        "Deep Space":             "9",
        "Never Land":             "B",
        "Disney Town":            "C",
        "The Keyblade Graveyard": "D"}
    return world_offsets[world]