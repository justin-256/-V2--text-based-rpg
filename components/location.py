from components.container import Container
from vars import vars
from utils.list_to_string import list_str

class Location:
    def __init__(self, name, ref_name, synonyms, contents, surroundings, light, description):
        self.name = name
        self.synonyms = synonyms
        self.ref_name = ref_name
        self.contents = contents
        self.surroundings = surroundings
        self.light = light    
        self.description = description

class Door:
    def __init__(self, name, isopen, islocked, keyid):
        self.name = name
        self.isopen = isopen
        self.islocked = islocked
        self.keyid = keyid

def printmap():

    max_x = 1
    max_y = -1

    x = -1
    y = 1

    while y >= max_y:
        line = ""
        while x <= max_x:
            type = areas["house"][list_str([x,y,1])].type
            if type == "Location":
                line += "*"
            elif type == "Barrier":
                line += "X"
            elif type == "Building":
                line += "#"
            x+=1
            line += " "
        y-=1
        x=-1
        print(line)

