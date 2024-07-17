from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import KHBBSLocation, location_table


class KHBBSRegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int, options):
    regions: Dict[str, KHBBSRegionData] = {
        "Menu":               KHBBSRegionData(None, ["Land of Departure"]),
        "Land of Departure":  KHBBSRegionData([],   ["World Map"]),
        "Dwarf Woodlands":    KHBBSRegionData([],   []),
        "Castle of Dreams":   KHBBSRegionData([],   []),
        "Enchanted Dominion": KHBBSRegionData([],   []),
        "Mysterious Tower":   KHBBSRegionData([],   []),
        "Radiant Garden":     KHBBSRegionData([],   []),
        "Olympus Coliseum":   KHBBSRegionData([],   []),
        "Deep Space":         KHBBSRegionData([],   []),
        "Destiny Islands":    KHBBSRegionData([],   []),
        "Neverland":          KHBBSRegionData([],   []),
        "Disney Town":        KHBBSRegionData([],   []),
        "Keyblade Graveyard": KHBBSRegionData([],   []),
        "World Map":          KHBBSRegionData([],   ["Dwarf Woodlands", "Castle of Dreams", "Enchanted Dominion", "Mysterious Tower",
                                                    "Radiant Garden", "Olympus Coliseum", "Deep Space", "Destiny Islands",
                                                    "Neverland", "Disney Town", "Keyblade Graveyard"]),
    }

    # Set up locations
    regions["Land of Departure"].locations.append("(T) Land of Departure Mountain Path Pulsing Crystal Chest")
    regions["Land of Departure"].locations.append("(T) Land of Departure Mountain Path Hi-Potion Chest")
    regions["Land of Departure"].locations.append("(T) Land of Departure Mountain Path Stop Chest")
    regions["Land of Departure"].locations.append("(T) Land of Departure Summit Soothing Crystal Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Vault Balloon Letter Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Vault Ether Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Vault Potion Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Vault Flame Salvo Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Underground Waterway Potion Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Underground Waterway Block Recipe Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Underground Waterway Poison Edge Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Courtyard Fission Firaga Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Courtyard Potion Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Flower Glade Hungry Crystal Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Courtyard Map Chest")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Underground Waterway Fire Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Palace Courtyard Pulsing Crystal Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Palace Courtyard Wellspring Crystal Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Palace Courtyard Slow Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Ballroom Fleeting Crystal Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Foyer Strike Raid Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Foyer Potion Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Foyer Hi-Potion Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Foyer Soothing Crystal Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Antechamber Thunder Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Palace Courtyard Map Chest")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Chateau Thunderstorm Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Waterside Potion Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Forest Clearing Blizzard Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Audience Chamber Zero Gravity Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Audience Chamber Ether Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Audience Chamber Potion Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Hallway Ether Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Aurora's Chamber Map Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Tower Room Sleep Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Waterside Pulsing Crystal Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Tower Room Attack Recipe Chest")
    regions["Mysterious Tower"].locations.append("(T) Mysterious Tower Mysterious Tower Pulsing Crystal Chest")
    regions["Mysterious Tower"].locations.append("(T) Mysterious Tower Mysterious Tower Balloon Letter Chest")
    regions["Mysterious Tower"].locations.append("(T) Mysterious Tower Mysterious Tower Cure Chest")
    regions["Mysterious Tower"].locations.append("(T) Mysterious Tower Tower Entrance Magic Recipe Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Aqueduct Esuna Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Aqueduct Blackout Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Aqueduct Hi-Potion Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Outer Gardens Fira Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Outer Gardens Pulsing Crystal Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Central Square Potion Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Central Square Hi-Potion Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Purification Facility Mega-Potion Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Purification Facility Chaos Crystal Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Castle Town Map Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Fountain Court Thunder Surge Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Fountain Court Fleeting Crystal Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Fountain Court Panacea Chest")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Merlin's House Shimmering Crystal Chest")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Coliseum Gates Fire Strike Chest")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Coliseum Gates Mega Attack Recipe Chest")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Coliseum Gates Mega-Potion Chest")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Vestibule Map Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Turo Prison Block High Jump Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Durgon Transporter Hi-Potion Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Ship Corridor Ether Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Ship Corridor Hi-Potion Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Ship Corridor Pulsing Crystal Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Ship Corridor Warp Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Control Room Hi-Potion Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Turo Prison Block Brutal Blast Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Turo Prison Block Pulsing Crystal Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Turo Prison Block Mega-Ether Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Ship Hub Hungry Crystal Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Machinery Bay Access Mine Square Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Turo Prison Block Mega-Potion Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Launch Deck Thundara Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Turo Transporter Map Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Launch Deck Abounding Crystal Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Launch Deck Wellspring Crystal Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Ship Hub Mega-Potion Chest")
    regions["Deep Space"].locations.append("(T) Deep Space Ship Hub Fleeting Crystal Chest")
    regions["Neverland"].locations.append("(T) Neverland Gully Map Chest")
    regions["Neverland"].locations.append("(T) Neverland Cove Hi-Potion Chest")
    regions["Neverland"].locations.append("(T) Neverland Cove Ether Chest")
    regions["Neverland"].locations.append("(T) Neverland Cliff Path Hi-Potion Chest")
    regions["Neverland"].locations.append("(T) Neverland Cliff Path Mega-Potion Chest")
    regions["Neverland"].locations.append("(T) Neverland Cliff Path Firaga Chest")
    regions["Neverland"].locations.append("(T) Neverland Mermaid Lagoon Dark Haze Chest")
    regions["Neverland"].locations.append("(T) Neverland Mermaid Lagoon Geo Impact Chest")
    regions["Neverland"].locations.append("(T) Neverland Mermaid Lagoon Elixir Chest")
    regions["Neverland"].locations.append("(T) Neverland Peter's Hideout Shimmering Crystal Chest")
    regions["Neverland"].locations.append("(T) Neverland Peter's Hideout Mega Magic Recipe Chest")
    regions["Neverland"].locations.append("(T) Neverland Jungle Clearing Hi-Potion Chest")
    regions["Neverland"].locations.append("(T) Neverland Rainbow Falls: Crest Abounding Crystal Chest")
    regions["Neverland"].locations.append("(T) Neverland Skull Rock: Entrance Panacea Chest")
    regions["Neverland"].locations.append("(T) Neverland Skull Rock: Cavern Megalixir Chest")
    regions["Neverland"].locations.append("(T) Neverland Skull Rock: Cavern Ars Solum Chest")
    regions["Neverland"].locations.append("(T) Neverland Skull Rock: Cavern Chaos Crystal Chest")
    regions["Neverland"].locations.append("(T) Neverland Rainbow Falls: Base Megalixir Chest")
    regions["Neverland"].locations.append("(T) Neverland Rainbow Falls: Base Zero Graviga Chest")
    regions["Neverland"].locations.append("(T) Neverland Gully Hi-Potion Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Main Plaza Map Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Main Plaza Potion Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Raceway Abounding Crystal Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Raceway Payback Fang Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Raceway Slot Edge Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Gizmo Gallery Panacea Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Gizmo Gallery Action Recipe Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Gizmo Gallery Chaos Crystal Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Gizmo Gallery Thunder Chest 1")
    regions["Disney Town"].locations.append("(T) Disney Town Gizmo Gallery Thunder Chest 2")
    regions["Disney Town"].locations.append("(T) Disney Town Pete's Rec Room Zero Gravira Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Pete's Rec Room Aerial Slam Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Gizmo Gallery Absolute Zero Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Pete's Rec Room Break Time Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Pete's Rec Room Chaos Crystal Chest")
    regions["Disney Town"].locations.append("(T) Disney Town Gizmo Gallery Mega-Potion Chest")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Twister Trench Windcutter Chest")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Twister Trench Mega-Potion Chest")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Twister Trench Mega-Ether Chest")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Twister Trench Megalixir Chest")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Seat of War Elixir Chest")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Seat of War Mega-Potion Chest")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Seat of War Map Chest")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Forest Clearing Balloon Sticker")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Audience Chamber Huey Sticker")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Tower Room Flying Balloon Sticker")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Chateau Traffic Cone Sticker")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Passage Flying Balloon Sticker")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Underground Waterway Louie Sticker")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Flower Glade Balloon Sticker")
    regions["Mysterious Tower"].locations.append("(T) Mysterious Tower Sorcerer's Chamber Balloon Sticker")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Outer Gardens Airplane Sticker")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Central Square Flying Balloon Sticker")
    regions["Radiant Garden"].locations.append("(T) Radiant Fountain Court Dale Sticker")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Coliseum Gates Balloon Sticker")
    regions["Deep Space"].locations.append("(T) Deep Space Turo Prison Block Flying Balloon Sticker")
    regions["Deep Space"].locations.append("(T) Deep Space Ship Corridor UFO Sticker")
    regions["Neverland"].locations.append("(T) Neverland Peter's Hideout Dewey Sticker")
    regions["Neverland"].locations.append("(T) Neverland Rainbow Falls: Base Rainbow Sticker")
    regions["Neverland"].locations.append("(T) Neverland Skull Rock: Entrance Chip Sticker")
    regions["Disney Town"].locations.append("(T) Disney Town Gizmo Gallery Pete Sticker")
    regions["Disney Town"].locations.append("(T) Disney Town Raceway Traffic Cone Sticker")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Twister Trench Traffic Cone Sticker")
    regions["Land of Departure"].locations.append("(T) Land of Departure Orbs Defeated Max HP Increase")
    regions["Land of Departure"].locations.append("(T) Land of Departure Orbs Defeated Critical Impact")
    regions["Land of Departure"].locations.append("(T) Land of Departure Orbs Defeated Ventus D-Link")
    regions["Land of Departure"].locations.append("(T) Land of Departure Orbs Defeated Aqua D-Link")
    regions["Land of Departure"].locations.append("(T) Land of Departure Orbs Defeated Keyblade Board")
    regions["Land of Departure"].locations.append("(T) Land of Departure Eraqus Defeated Max HP Increase")
    regions["Land of Departure"].locations.append("(T) Land of Departure Eraqus Defeated Chaos Ripper")
    regions["Land of Departure"].locations.append("(T) Land of Departure Eraqus Defeated Xehanort's Report 8")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Unversed Group Defeated Air Slide")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Max HP Increase")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Firestorm")
    regions["Dwarf Woodlands"].locations.append("(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Treasure Trove")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Cinderella Escorted Counter Hammer")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Symphony Master Defeated Max HP Increase")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Symphony Master Defeated Deck Capacity Increase")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Symphony Master Defeated Cinderella D-Link")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Symphony Master Defeated Stroke of Midnight")
    regions["Castle of Dreams"].locations.append("(T) Castle of Dreams Symphony Master Defeated Royal Board")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Unlock Aurora's Heart Maleficent D-Link")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Wheel Master Defeated Deck Capacity Increase")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Wheel Master Defeated Diamond Dust")
    regions["Enchanted Dominion"].locations.append("(T) Enchanted Dominion Wheel Master Defeated Fairy Stars")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Examine Pooh's Story Book Honey Pot Board")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Defeat Trinity Armor Max HP Increase")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Defeat Trinity Armor Rockbreaker")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Defeat Trinity Armor Disney Town Pass")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Defeat Braig Deck Capacity Increase")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Defeat Braig Dark Volley")
    regions["Radiant Garden"].locations.append("(T) Radiant Garden Defeat Braig Xehanort's Report 2")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Tournament Complete Max HP Increase")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Tournament Complete Sonic Impact")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Defeat Zack Deck Capacity Increase")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Defeat Zack Zack D-Link")
    regions["Olympus Coliseum"].locations.append("(T) Olympus Coliseum Defeat Zack Mark of a Hero")
    regions["Deep Space"].locations.append("(T) Deep Space Defeat Unversed in Space Max HP Increase")
    regions["Deep Space"].locations.append("(T) Deep Space Defeat Experiment 221 Thunderbolt")
    regions["Deep Space"].locations.append("(T) Deep Space Defeat Experiment 221 Experiment 626 D-Link")
    regions["Deep Space"].locations.append("(T) Deep Space Defeat Experiment 221 Hyperdrive")
    regions["Deep Space"].locations.append("(T) Deep Space Defeat Experiment 221 Spaceship Board")
    regions["Destiny Islands"].locations.append("(T) Destiny Islands Scene Ends of the Earth")
    regions["Neverland"].locations.append("(T) Neverland Defeat Peter Pan Bladecharge")
    regions["Neverland"].locations.append("(T) Neverland Defeat Peter Pan Peter Pan D-Link")
    regions["Neverland"].locations.append("(T) Neverland Defeat Countless Unversed Deck Capacity Increase")
    regions["Neverland"].locations.append("(T) Neverland Defeat Countless Unversed Pixie Petal")
    regions["Neverland"].locations.append("(T) Neverland Defeat Countless Unversed Skull Board")
    regions["Disney Town"].locations.append("(T) Disney Town Complete Rumble Racing Hi-Potion")
    regions["Disney Town"].locations.append("(T) Disney Town Complete Rumble Racing Toon Board")
   #regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Meet With Xehanort Dark Impulse")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Xehanort Defeated Max HP Increase")
    regions["Keyblade Graveyard"].locations.append("(T) Keyblade Graveyard Defeat Terranort")

    # Set up the regions correctly.
    for name, data in regions.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))

    multiworld.get_entrance("Land of Departure",  player).connect(multiworld.get_region("Land of Departure",  player))
    multiworld.get_entrance("Dwarf Woodlands",    player).connect(multiworld.get_region("Dwarf Woodlands",    player))
    multiworld.get_entrance("Castle of Dreams",   player).connect(multiworld.get_region("Castle of Dreams",   player))
    multiworld.get_entrance("Enchanted Dominion", player).connect(multiworld.get_region("Enchanted Dominion", player))
    multiworld.get_entrance("Mysterious Tower",   player).connect(multiworld.get_region("Mysterious Tower",   player))
    multiworld.get_entrance("Radiant Garden",     player).connect(multiworld.get_region("Radiant Garden",     player))
    multiworld.get_entrance("Olympus Coliseum",   player).connect(multiworld.get_region("Olympus Coliseum",   player))
    multiworld.get_entrance("Deep Space",         player).connect(multiworld.get_region("Deep Space",         player))
    multiworld.get_entrance("Destiny Islands",    player).connect(multiworld.get_region("Destiny Islands",    player))
    multiworld.get_entrance("Neverland",          player).connect(multiworld.get_region("Neverland",          player))
    multiworld.get_entrance("Disney Town",        player).connect(multiworld.get_region("Disney Town",        player))
    multiworld.get_entrance("Keyblade Graveyard", player).connect(multiworld.get_region("Keyblade Graveyard", player))
    multiworld.get_entrance("World Map",          player).connect(multiworld.get_region("World Map",          player))

def create_region(multiworld: MultiWorld, player: int, name: str, data: KHBBSRegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = KHBBSLocation(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    if data.region_exits:
        for exit in data.region_exits:
            entrance = Entrance(player, exit, region)
            region.exits.append(entrance)

    return region
