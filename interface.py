from colorama import Fore
import textwrap
import os

def usr_out(text, raw = False):    
    if raw:
        print(text)
    else:
        print(textwrap.fill(text, width = os.get_terminal_size().columns))

def usr_in(text):
    return input(text)

def log(text):
    print(Fore.BLUE + str(text) + Fore.RESET)
    
