from Logic.Attack_Storage import *
from Logic.util import containsAny
import Logic.config as config
from random import randrange


def hunter_combat():
    print("An " + config.enemy.getName() + " appeared!")

    while config.enemy.getHp() > 0:

        print()
        config.enemy.display_stats()
        config.player.display_stats()
        print()

        # Set Speed randomly every loop
        tempplayerspeed = randrange(config.player.getSpeed(), config.player.getSpeed() * 2)
        tempespeed = randrange(config.enemy.getSpeed(), config.enemy.getSpeed() * 2)

        # Multiple deaths form a list. Choose random -----------------------
        if config.player.getHp() <= 0:
            print("The " + config.enemy.getName() + " lays his mace into the side of your head.")
            print("Everything goes black.")
            quit()
        # ------------------------------------------------------------------
        elif config.enemy.getHp() <= 0:
            print(config.enemy.getName() + " was defeated!")
            break
        else:

            # Enemy attacks first
            if tempespeed > tempplayerspeed:

                # Enemy Attack
                print()
                print("The " + config.enemy.getName() + " attacks first!")
                # config.player.take_hit(config.enemy.getAtk())
                if config.enemy.getAtk() <= config.player.getDef():
                    print("Your defense completely absorbs the blow!")
                    print()
                else:
                    amt = config.enemy.getAtk() - config.player.getDef()
                    config.player.take_hit(amt)
                    print("Your defense softens the blow by " + str(config.player.getDef()) + "!")
                    print()

                print("Choose an attack!")
                print(str(config.player.attacks))
                attack = input()
                attack = attack.upper()
                strik = ["STRIKE"]
                pounc = ["POUNCE"]
                # Player attack
                if containsAny(attack, strik):
                    strike()
                elif containsAny(attack, pounc):
                    pounce()
                else:
                    print("Attack not found!")
                    continue
                    
            # Player attacks first
            if tempplayerspeed >= tempespeed:
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
                else:
                    print("Attack not found!")
                    continue

                # Enemy Attack
                # config.player.take_hit(config.enemy.getAtk())
                print()
                print("The " + config.enemy.getName() + " attacks first!")
                # config.player.take_hit(config.enemy.getAtk())
                if config.enemy.getAtk() <= config.player.getDef():
                    print("Your defense completely absorbs the blow!")
                    print()
                else:
                    amt = config.enemy.getAtk() - config.player.getDef()
                    config.player.take_hit(amt)
                    print("Your defense softens the blow by " + str(config.player.getDef()) + "!")
                    print()

    print()
    print("The " + config.enemy.getName() + " has been defeated!")
    print()