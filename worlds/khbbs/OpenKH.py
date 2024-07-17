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


def patch_khbbs(self, output_directory):
    mod_name = f"AP-{self.multiworld.seed_name}-P{self.player}-{self.multiworld.get_file_safe_player_name(self.player)}"
    mod_dir = os.path.join(output_directory, mod_name + "_" + Utils.__version__)
    
    seed_lua = build_seed_lua(self)
    
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

def build_seed_lua(self):
    character_id = 2
    seed_lua = get_lua_header()
    seed_lua = seed_lua + get_lua_character_check(character_id)
    seed_lua = seed_lua + get_sticker_replace(self)
    seed_lua = seed_lua + get_chest_replace(self)
    seed_lua = seed_lua + get_else_replace(self)
    return seed_lua

def get_lua_header():
    return """LUAGUI_NAME = "bbsAPDummyLocations"
LUAGUI_AUTH = "Gicu"
LUAGUI_DESC = "BBS FM AP Dummy Locations"

game_version = 1 --1 for 1.0.0.9 EGS, 2 for Steam
IsEpicGLVersion = 0x6107D4
IsSteamGLVersion = 0x6107B4
IsSteamJPVersion = 0x610534
can_execute = false

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
    if can_execute then
        if ReadInt(version_choice({0x0, 0x81711F}, game_version)) ~= 0xFFFFFF00 then --Not on Title Screen
            if ReadInt(version_choice({0x0, 0x81711F}, game_version)) ~= 0xD0100 then
                if ReadInt(version_choice({0x0, 0x81711F}, game_version)) ~= 0x20100 or ReadInt(version_choice({0x0, 0x817123}, game_version)) ~= 0x100 or ReadShort(version_choice({0x0, 0x817127}, game_version)) ~= 0x100 then\n"""

def get_lua_character_check(self):
    character_id = 2
    return """                    if ReadByte(version_choice({0x0, 0x10F9F800}, game_version)) == 0x0""" + str(character_id) + """ then\n"""

def get_sticker_replace(self):
    replace_stickers_str = ""
    for location in self.multiworld.get_filled_locations(self.player):
        location_data = location_table[location.name]
        item_data = item_table[location.item.name]
        if location_data.type == "Sticker":
            replace_stickers_str = replace_stickers_str + ("    " * 6) + "WriteInt(" + str(location_data.address) + ", 0x"
            if item_data.category == "Key Item":
                write_value = get_world_offset(location_data.category) + item_data.khbbsid
            else:
                write_value = "00000"
            replace_stickers_str = replace_stickers_str + write_value + ")\n"
    return replace_stickers_str

def get_chest_replace(self):
    replace_chests_str = ""
    for location in self.multiworld.get_filled_locations(self.player):
        location_data = location_table[location.name]
        item_data = item_table[location.item.name]
        if location_data.type == "Chest":
            replace_chests_str = replace_chests_str + ("    " * 6) + "WriteInt(" + str(location_data.address) + ", 0x"
            if item_data.category in ["Attack Command", "Magic Command", "Item Command", "Friendship Command", "Movement Command", "Defense Command", "Reprisal Command", "Shotlock Command"] and not location_data.forced_remote:
                item_prefix = "01"
                write_value = get_world_offset(location_data.category) + item_prefix + item_data.khbbsid
            elif item_data.category in ["Key Item"]:
                item_prefix = "00"
                write_value = get_world_offset(location_data.category) + item_prefix + item_data.khbbsid
            else:
                write_value = "0000000"
            replace_chests_str = replace_chests_str + write_value + ")\n"
    return replace_chests_str

def get_else_replace(self):
    return """
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0xF04 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x1 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x904 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x2 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x606 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x36 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0xD0B and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x36 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0xD0B and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x4 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x20A and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x33 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x10D and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x37 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x402 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x3 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x602 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x1 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x101 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x40 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0xB06 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x37 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x408 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x3E then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x609 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x2 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0x801 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x1 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0xA03 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x1 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                        end
                        if ReadShort(version_choice({0x0, 0x817120}, game_version)) == 0xA03 and ReadShort(version_choice({0x0, 0x817128}, game_version)) == 0x2 then
                            WriteInt(version_choice({0x0, 0x10F9F498}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F468}, game_version), 0x00000000)
                            WriteInt(version_choice({0x0, 0x10F9F480}, game_version), 0x00000000)
                        end
                    end
                end
            end
        end
    end
end"""

def get_world_offset(world):
    world_offsets = {
        "Land of Departure":  "1",
        "Dwarf Woodlands":    "2",
        "Castle of Dreams":   "3",
        "Enchanted Dominion": "4",
        "Mysterious Tower":   "5",
        "Radiant Garden":     "6",
        "Realm of Darkness":  "7",
        "Olympus Coliseum":   "8",
        "Deep Space":         "9",
        "Neverland":          "B",
        "Disney Town":        "C",
        "Keyblade Graveyard": "D"}
    return world_offsets[world]