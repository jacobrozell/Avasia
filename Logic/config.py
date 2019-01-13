from Player.PlayerClass import Player
from Enemy.EnemyClass import Enemy
import colorama as c


# Variables to keep track of
current_room_id = ""
fountain = False
ulric = False
doran = False
varrustysword = False
varbrokenaxe = False
courtyard = False
returnfish = False
portalRoom = False

# enemy stats
# -------------------------
enemy = Enemy(name="",
              hp=0,
              atk=0,
              defense=0,
              speed=0)


# player stats
# -------------------------

player = Player(name="",
                hp=0,
                atk=0,
                luck=0,
                speed=0,
                gold=0,
                class_id="")

# Colors
base_color = str(c.Fore.LIGHTBLUE_EX)
talk_color = str(c.Fore.CYAN)
die_color = str(c.Fore.RED)
room_color = str(c.Fore.BLACK)
trophy_color = str(c.Fore.GREEN)
