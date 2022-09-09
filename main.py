import os, json
from components.character import Character, Player, Npc
from components.world_parser import importfile, exportfile, loadnew
from commands.look import look
from vars import vars
from interface import usr_out, usr_in, log
from components.menu import menu

build = "0.01"
splash = f"█  SKV2 IN-DV BUILD [{build}]  "
columns = os.get_terminal_size().columns

if __name__ == "__main__":
    #loadnew()
    #exportfile("world")
    print(splash + "█" * (columns - len(splash)))
    print("")
    importfile("world")
    menu()    
