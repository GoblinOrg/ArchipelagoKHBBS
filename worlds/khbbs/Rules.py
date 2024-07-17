from BaseClasses import CollectionState, MultiWorld

def set_rules(khbbsworld):
    multiworld = khbbsworld.multiworld
    player     = khbbsworld.player
    # Location Rules
    multiworld.get_location("(T) Land of Departure Eraqus Defeated Max HP Increase"     , player).access_rule = lambda state: state.has_any({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
    multiworld.get_location("(T) Land of Departure Eraqus Defeated Chaos Ripper"        , player).access_rule = lambda state: state.has_any({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
    multiworld.get_location("(T) Land of Departure Eraqus Defeated Xehanort's Report 8" , player).access_rule = lambda state: state.has_any({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
    
    # Region rules.
    multiworld.get_entrance("Dwarf Woodlands"                                           , player).access_rule = lambda state: state.has("Dwarf Woodlands",    player)
    multiworld.get_entrance("Castle of Dreams"                                          , player).access_rule = lambda state: state.has("Castle of Dreams",   player)
    multiworld.get_entrance("Enchanted Dominion"                                        , player).access_rule = lambda state: state.has("Enchanted Dominion", player)
    multiworld.get_entrance("Mysterious Tower"                                          , player).access_rule = lambda state: state.has("Mysterious Tower",   player)
    multiworld.get_entrance("Radiant Garden"                                            , player).access_rule = lambda state: state.has("Radiant Garden",     player)
    multiworld.get_entrance("Olympus Coliseum"                                          , player).access_rule = lambda state: state.has("Olympus Coliseum",   player)
    multiworld.get_entrance("Deep Space"                                                , player).access_rule = lambda state: state.has("Deep Space",         player)
    multiworld.get_entrance("Destiny Islands"                                           , player).access_rule = lambda state: state.has("Destiny Islands",    player)
    multiworld.get_entrance("Neverland"                                                 , player).access_rule = lambda state: state.has("Neverland",          player)
    multiworld.get_entrance("Disney Town"                                               , player).access_rule = lambda state: state.has("Disney Town",        player)
    multiworld.get_entrance("Keyblade Graveyard"                                        , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)

    # Win condition.
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
    