from components.container import Container
from vars import vars
from interface import usr_out, usr_in

rargs = []

def look(PLYR, **kwargs):

    global objects_dict
    playername = "player"
    player_location_name = vars.players[playername].location
    for i in vars.map:
        if i == player_location_name:
            player_location = vars.map[player_location_name]

    
    objectsList = []
    for i in vars.map[player_location_name].contents:
        for j in vars.objects:
            if i == j: #################USE MAP()
                objectsList.append(vars.objects[j])

    charactersList = []
    for i in vars.characters.values():
        if i.location == player_location_name:
            charactersList.append(i)
    
    players = ""
    for i in vars.players.values():
        if i.location == player_location_name and i.name != playername:
            players += "   " + i.name.capitalize() + "\n"
    

    objects = ""
    for i in [*objectsList, *charactersList]: 
        objects += i.description + " "

    #objects which stay in place get printed, and things interacted with are put in containers
    obt = ""
    
    for i in objectsList:
        if isinstance(i, Container):
            obt += f"The {i.name} contains: " #replace with custom string in class for different container types such as a table.
            obt += i.fetch_contents().capitalize() + ".\n"


    usr_out(f"{player_location.ref_name}:")
    usr_out(f"")
    usr_out(f"{player_location.description} {objects}")
    usr_out(f"{obt}")
    if len(players) > 0:
        usr_out(f"Players here:")
        usr_out(f"{players}")
    else:
        usr_out("There are no other players here.")