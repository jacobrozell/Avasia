import Logic.config as config
import Logic.util as util
import random as random
enemy = config.enemy
player = config.player

all_combat_commands = ["ATTACK", "HEAL"]
combat_heal = ["HEAL", "EAT", "DRINK", "USE ITEM", "USE"]
combat_help = ["HELP", "COMMANDS"]
attack = ["ATTACK", "STRIKE", "FIGHT"]
luck_roll = 0

while True:
    print(enemy.name)
    print("HEALTH: ",enemy.hp)
    print(player.name)
    print("HEALTH: ",player.hp)
    print()
    command = input("What do will you do?")
    command.upper()

    if util.containsAny(command,combat_help):
        print(all_combat_commands)
        print()
    elif util.containsAny(command,combat_heal):
        print("What do you want to use?")
        config.player.print_player_inventory()
        itemToBeEaten = input()

    elif util.containsAny(command,attack):
        if player.spd >= enemy.spd:
            luck_roll = random.randint(0, 10)
            if luck_roll <= player.luck:
                print("You attack ", enemy.name)
                print("You deal", player.atk, " damage!")
                enemy.hp -= player.atk
                if enemy.hp <= 0:
                    break
            else:
                print("You missed!")
            luck_roll = random.randint(0, 10)
            if luck_roll >= player.luck:
                print(enemy.name, " attacks and damages you for ", enemy.atk)
                player.hp -= enemy.atk
                if player.hp <= 0:
                    break
        else:
            print(enemy.name, " attacks and damages you for ",enemy.atk)
            print("You attack ", enemy.name)
            print("You deal", player.atk, " damage!")
            enemy.hp -= player.atk
            if enemy.hp <= 0:
                break

if player.hp <= 0:

else:
    print(enemy.name, " was slain!")
    #return to previous spot



