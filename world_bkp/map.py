from components.location import *

data = {
    "kitchen": Location(
        name = "kitchen",
        synonyms = ["home"],
        ref_name = "Kitchen",

        contents = [
            "bench"
        ],
        surroundings = {
            "N":{"passable":False,"location":None, "joiner":False},
            "S":{"passable":False,"location":None, "joiner":False},
            "E":{"passable":False,"location":None, "joiner":False},
            "W":{"passable":"kitchen_backyard_door","location":"backyard", "joiner":True},
            "U":{"passable":False, "location":None, "joiner":False},
            "D":{"passable":False,"location":None, "joiner":False},
        },
        light = 0,
        description = "",
    ),
    
    "backyard": Location(
        name = "backyard",
        synonyms = ["back garden"],
        ref_name = "West of house",
        contents = [
            "bench",
            "box"
        ],
        surroundings = {
            "N":{"passable":False, "location":None, "joiner":False},
            "S":{"passable":False, "location":None, "joiner":False},
            "E":{"passable":"kitchen_backyard_door", "location":"kitchen", "joiner":True},
            "W":{"passable":False, "location":None, "joiner":False},
            "U":{"passable":True, "location":"treehouse", "joiner":False},
            "D":{"passable":False, "location":None, "joiner":False},
        },
        light = 0,
        description = "You are standing in the backyard behind the house.",
    )
}