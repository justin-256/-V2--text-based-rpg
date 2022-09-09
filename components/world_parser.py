import os
import json
from components.character import Character, Player
from components.location import Location
from components.object import Object
from vars import vars
import pickle
import zipfile
from interface import usr_in, usr_out



    
def importfile(filedir):

    if 1:
        path = "world" #output path

        os.makedirs(path, exist_ok=True)
        
        from world_bkp.map import data as filemap
        from world_bkp.characters import data as filecharacters
        from world_bkp.objects import data as fileobjects
        from world_bkp.players import data as fileplayers
        from world_bkp.surroundingsjoiners import data as filesurroundingsjoiners
    
        #EEEFFFFFFIIICIENCYYYYYY!!!
        with open(f'{path}/map.sk', 'wb') as outp:
                pickle.dump(filemap, outp, protocol=None, fix_imports=True, buffer_callback=None)
        with open(f'{path}/characters.sk', 'wb') as outp:
                pickle.dump(filecharacters, outp, protocol=None, fix_imports=True, buffer_callback=None)
        with open(f'{path}/objects.sk', 'wb') as outp:
                pickle.dump(fileobjects, outp, protocol=None, fix_imports=True, buffer_callback=None)
        with open(f'{path}/players.sk', 'wb') as outp:
                pickle.dump(fileplayers, outp, protocol=None, fix_imports=True, buffer_callback=None)
        with open(f'{path}/surroundingsjoiners.sk', 'wb') as outp:
                pickle.dump(filesurroundingsjoiners, outp, protocol=None, fix_imports=True, buffer_callback=None)
        
    global vars
    try:
        with open(f"{filedir}/map.sk", "rb") as data:
            vars.map = pickle.load(data)
    except FileNotFoundError:
        usr_out("ERROR LOADING map.sk")        

    try:
        with open(f"{filedir}/surroundingsjoiners.sk", "rb") as data:
            vars.joiners = pickle.load(data)
    except FileNotFoundError:
        usr_out("ERROR LOADING surroundingsjoiners.sk")        
    
    try:            
        with open(f"{filedir}/objects.sk", "rb") as data:
            vars.objects = pickle.load(data)
    except FileNotFoundError:
        usr_out("ERROR LOADING objects.sk")        
    
    try:            
        with open(f"{filedir}/players.sk", "rb") as data:
            vars.players = pickle.load(data)
    except FileNotFoundError:
        usr_out("ERROR LOADING players.sk")        

    try:            
        with open(f"{filedir}/characters.sk", "rb") as data:
            vars.characters = pickle.load(data)
    except FileNotFoundError:
        usr_out("ERROR LOADING characters.sk")        

    
def exportfile(filedir):
    pass

def loadnew(): #creates new world from defaults
    importfile("world_new")


 