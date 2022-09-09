from vars import vars
from interface import usr_out, usr_in
from commands.look import look

dir_crossref = {
    "north":"N",
    "south":"S",
    "east":"E",
    "west":"W",
    "up":"U",
    "down":"D"
}

def move(PLYR, ACT, **kwargs):
    player = vars.players[PLYR]

    direction = dir_crossref[ACT]
    
    direction = vars.map[player.location].surroundings[direction]
    
    if direction["joiner"] == True:
        passable = vars.joiners[direction["passable"]].isopen
    else: 
        passable = direction["passable"]

    if passable:
        player.location = direction["location"]
        look(PLYR)
    else:
        usr_out(f"You can't go {ACT}!")

    #"W":{"passable":"kitchen_backyard_door","location":"kitchen"},

