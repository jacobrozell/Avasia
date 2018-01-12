from Avasia.Logic.Attack_Storage import *
from Avasia.Logic.util import containsAny
import Avasia.Logic.config as config


def hunter_combat():
    print("An " + config.enemy_name + " appeared!")
    print("The " + config.enemy_name + " has " + str(config.enemy_hp) + " health and " + str(
        config.enemy_defense) + " defense!")
    while config.enemy_hp > 0:

        # Multiple deaths form a list. Choose random -----------------------
        if config.player_hp <= 0:
            print("The " + config.enemy_name + " lays his mace into the side of your head.")
            print("Everything goes black.")
            quit()
        # ------------------------------------------------------------------
        elif config.enemy_hp <= 0:
            print(config.enemy_name + " was defeated!")
            break
        else:

            # Enemy attacks first
            if config.enemy_spd > config.player_spd:

                # Enemy Attack
                print()
                print("The " + config.enemy_name + " attacks first!")
                # config.player.take_hit(config.enemy_atk)
                if config.enemy_atk <= config.player_defense:
                    print("Your defense completely absorbs the blow!")
                    print()
                else:
                    config.player_hp -= config.enemy_atk - config.player_defense
                    print("Your defense softens the blow by " + str(config.player_defense) + "!")
                    print("You take " + str(config.enemy_atk - config.player_defense) + "!")
                    print("Your health is now " + str(config.player_hp) + "!")
                    print()

                print("Choose an attack!")
                print(str(config.player.attacks))  # Class Variable
                attack = input()
                attack = attack.upper()
                strik = ["STRIKE"]
                pounc = ["POUNCE"]
                # Player attack
                if containsAny(attack, strik):
                    strike()
                elif containsAny(attack, pounc):
                    pounce()

            # Player attacks first
            if config.player_spd > config.enemy_spd:
                print()
                print("Choose an attack!")
                print(str(config.player.attacks))  # Class Variable
                attack = input()
                attack = attack.upper()
                strik = ["STRIKE"]
                pounc = ["POUNCE"]
                # Player attack
                if containsAny(attack, strik):
                    strike()
                elif containsAny(attack, pounc):
                    pounce()

                # config.player.choose_attack(attack)
                # if False:
                #    continue

                # Enemy Attack
                # config.player.take_hit(config.enemy_atk)
                print()
                print("The " + config.enemy_name + " attacks first!")
                # config.player.take_hit(config.enemy_atk)
                if config.enemy_atk <= config.player_defense:
                    print("Your defense completely absorbs the blow!")
                    print()
                else:
                    config.player_hp -= config.enemy_atk - config.player_defense
                    print("Your defense softens the blow by " + str(config.player_defense) + "!")
                    print("You take " + str(config.enemy_atk - config.player_defense) + "!")
                    print("Your health is now " + str(config.player_hp) + "!")
                    print()

    print()
    print("The " + config.enemy_name + " has been defeated!")
    print()