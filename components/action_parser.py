from components.container import Container
from commands.look import look
from commands.movement import move
from commands.help import help
from vars import vars
from interface import log

action_functions = {
    "look":look,
    
    "north":move,
    "south":move,
    "east":move,
    "west":move,
    "up":move,
    "down":move,

    "help":help
    
}

# Loads the valid objects which can be named in the command. 
def load_objects():
    """    
    characters
    objects
    map"""
    global objects_dict, action_functions
    playername = "player"
    player_location = vars.players[playername].location

    
    objects = {}
    for i in vars.map[player_location].contents:
        for j in vars.objects:
            if i == j:
                objects.update({i: vars.objects[j].synonyms + [i]})
                if isinstance(vars.objects[j], Container):
                    for i in vars.objects[j].contents:
                        for j in vars.objects:
                            if i == j:
                                objects.update({i: vars.objects[j].synonyms + [i]})


    characters = {}
    for i in vars.characters.values():
        if i.location == player_location:
            characters.update({i.name: i.synonyms + [i.name]})
    
    players = {}
    for i in vars.players.values():
        if i.location == player_location and i.name != playername:
            players.update({i.name: i.synonyms + [i.name]})

    # name and the synonyms are in the wrong way, looks better thr right way. just change the .update lines
    locations = {}
    

    objects_dict = {**objects, **characters, **players, **locations}
"""
    vars.map = {}
    vars.surroundingsjoiners = {}
    vars.objects = {}
    vars.characters = {}
"""

    
# Saves time
def checkls(checks, list):
    x = [False, -1]
    for i in checks:
        if i in list:
            x[0] = True
            x[1] = (list.index(i))
    return x

# Main parsing function
def parse_input(arg):
    load_objects()

    # Convert arg to lowercase and into a list, check if it has content
    arg = arg.lower().split()
    if len(arg) < 1:
        print("Error, input length")
        return

    # Remove random words
    strip_strings = ["the", "a", "an", "of"]
    for i in strip_strings:
        for j in arg:
            if i == j:
                arg.remove(i)

    # BAN BAD WORDS
    bad_words = ["fucking", "fuck", "dipshit", "asshole", "idiot", "dumbass", "fortnite"]
    for i in bad_words:
        if i in arg:
            print("This game is no place for such language!")
            return

    # Define prepositions and commends
    prepos_dict = {
        "in":["inside", "in" "into"],
        "on":["ontop", "on"],
        "under":["under", "underneath"],
        "over":["over"],
        "at":["at"],
        "with":["with", "using"]
    }
    commands_dict = {  
        "north":    ["north", "n"],
        "south":    ["south", "s"],
        "east":     ["east", "e"],
        "west":     ["west", "w"],
        "up":       ["up", "u"],
        "down":     ["down", "d"],
        "help":     ["help", "h"],
        "quit":     ["quit", "q"],
        "inventory":["inventory", "i"],
        "look":     ["look", "l"],
        "examine":  ["examine", "inspect", "check", "investigate"],
        "move":     ["move", "slide"],
        "play":     ["play"],
        "pull":     ["pull", "tug"],
        "take":     ["take", "grab"],
        "put":      ["put", "place"],
        "turn":     ["turn"],
        "open":     ["open"],
        "close":    ["close"],
        "read":     ["read"]
        }  

    
    valid_objects = [i for j in objects_dict for i in j]
    valid_commands = [i for j in commands_dict.values() for i in j]
    valid_prepos = [i for j in prepos_dict.values() for i in j]

    # If there is no valid action in the argument, return
    actloc = checkls(valid_commands, arg)[1]
    if actloc == -1:
        print("action not exist")
        return
    
    # If a word comes before action, remove it and update action location
    if actloc >= 1:
        arg = arg[actloc:]
        actloc = checkls(valid_commands, arg)[1]

    # Set the action variable
    ACT = arg[0]

    # Check if there are more than one preposition
    preposloc = checkls(valid_prepos, arg)
    if len(preposloc) > 2:
        print("too many prepositions")
        return

    # Set the remaining variables
    if preposloc[0] == False:
        if len(arg) == 1:
            DOB = ""
        else:
            DOB = arg[actloc+1:]
            
            # Convert OBs to string and generate output

            DOB = " ".join(str(n) for n in DOB)

        PPN = ""
        IOB = ""
    else:
        DOB = arg[actloc+1:preposloc[1]]
        PPN = arg[preposloc[1]]
        IOB = arg[preposloc[1]+1:]

        # Convert OBs to string and generate output

        DOB = " ".join(str(n) for n in DOB)
        IOB = " ".join(str(n) for n in IOB)

        # Check if all objects are valid

        dob_valid = DOB in valid_objects
        iob_valid = IOB in valid_objects
        if dob_valid == False or iob_valid == False:
            if dob_valid == False:
                print(f"object {DOB} does not exist!")
            if iob_valid == False:
                print(f"object {IOB} does not exist!")
            return

    # Convert the synonyms into valid names
    ACT = next(k for k, v in commands_dict.items() if ACT in v)
    if len(DOB) >= 1: DOB = next(k for k, v in objects_dict.items() if DOB in v)
    if len(IOB) >= 1: IOB = next(k for k, v in objects_dict.items() if IOB in v)
    if len(PPN) >= 1: PPN = next(k for k, v in prepos_dict.items() if PPN in v)

    PLYR = "player"
    
    # Return results
    results = {
        "ACT":ACT, 
        "DOB":DOB, 
        "IOB":IOB,
        "PPN":PPN,
        "PLYR":PLYR
        }
    log(results)
    #return results

    #ACT - action
    #DOB - direct object
    #IOB - indirect object 
    #PPN - preposition
    if ACT not in action_functions:
        print("ACTION NOT VALID!")
    else:
        action_functions[ACT](**results)
        
        

