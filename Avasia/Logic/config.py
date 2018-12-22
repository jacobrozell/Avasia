from Player.PlayerClass import Player
from Enemy.EnemyClass import Enemy


# Variables to keep track of
current_room_id = ""
fountain = False
ulric = False
doran = False
varrustysword = False
varbrokenaxe = False
courtyard = False
returnfish = False

# enemy stats
# -------------------------
enemy = Enemy(name="",
              hp=0,
              atk=0,
              defense=0,
              spd=0)


# player stats
# -------------------------

player = Player(name="",
                hp=0,
                atk=0,
                luck=0,
                defense=0,
                spd=0,
                gold=0,
                class_id="")

