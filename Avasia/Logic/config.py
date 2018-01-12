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

# enemy stats
# -------------------------
enemy_name = ""
enemy_hp = 0
enemy_defense = 0
enemy_atk = 0
enemy_spd = 0
enemy = Enemy(name=enemy_name,
              hp=enemy_hp,
              atk=enemy_atk,
              defense=enemy_defense,
              spd=enemy_spd)


# player stats
# -------------------------
name = ""
player_hp = 0
player_defense = 0
player_atk = 0
player_spd = 0
class_id = ""
player = Player(name=name,
                hp=player_hp,
                atk=player_atk,
                defense=player_defense,
                spd=player_spd,
                class_id=class_id)

player_stats = {}
player_stats["HP"] = str(player_hp)
player_stats["ATK"] = str(player_atk)
player_stats["DEFENSE"] = str(player_defense)
player_stats["SPEED"] = str(player_spd)



# ------------------------Gold----------------------------
player_gold = Gold(name="Gold",
                   des="Shiny gold coins.",
                   value=0)

