from Avasia.Player.PlayerClass import Player
from Avasia.Enemy.EnemyClass import Enemy
from Avasia.Items.Gold import Gold


# Variables to keep track of
current_room_id = ""
fountain = 0
ulric = 0
varrustysword = 0
varbrokenaxe = 0
courtyard = 0
returnfish = 0

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
                class_id="")


# ------------------------Gold----------------------------
player_gold = Gold(name="Gold",
                   des="Shiny gold coins.",
                   value=0)
