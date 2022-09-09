 from components.container import Container
from components.character import Character, Player, Npc
from components.world_parser import importfile, exportfile
from vars import vars
from interface import usr_out, usr_in
from utils.list_to_string import list_str
from commands.look import look

helpls = ["[h] help - Print help menu\n",
"[q] quit - Quit game\n",
"[p] pause - Pause game\n",
"\n",
"############################################\n",
"\n",
"[l] look - Look around\n",
"[n] north - Go north\n",
"[s] south - Go south\n",
"[e] east - Go east\n",
"[w] west - Go west\n",
"[i] inventory - Print inventory contents\n",
"take - Take item (put it in inventory)\n",
"put - Put item on/in table/container\n",
"examine - Examine item\n",
"move - Move item\n",
"pull - Pull item\n",
"turn - Turn on or off item\n",
"open - Open item\n",
"close - Close item\n",
"read - Read piece of literature"]

def help(PLYR, **kwargs):
    for line in helpls:
        usr_out(line)