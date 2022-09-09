import os, json
from components.character import Character
from components.world_parser import importfile, exportfile
from vars import vars
from interface import usr_out, usr_in
from components.action_parser import parse_input
from components.location import printmap

def menu():
    usr_out(f"  _____ _ _           _   _  __          \r\n / ____(_) |         | | | |/ /           __      _____    ___  \r\n| (___  _| | __ _ __ | |_| \' / __ _   _   \\ \\    / /__ \\  / _ \\ \r\n \\___ \\| | |/_ \\ \'_ \\| __|  < /_ \\ | | |   \\ \\  / /   ) || | | | \r\n ____) | | | __/ | | | |_| . \\ __/ |_| |    \\ \\/ /   / / | | | |\r\n|_____/|_|_|\\__|_| |_|\\__|_|\\_\\__|\\__, |     \\  /   / /_ | |_| |\r\n  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   __/ |      \\/   |____(_)___/\r\n  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  |___/  \n\n", raw = True)
    while True:
        parse_input(input("> "))
        #action = input("> ").lower
            
            
        
        