from Avasia.Class.Wolf_Attacks import *
from Avasia.Logic.util import containsAny
import Avasia.Logic.config as config
from random import randrange
enemy_wounded = False
enemy_stunned = False
turns_wounded = -1
turns_stunned = -1
attack = ""


def choose_attack():
    print("Choose an attack!")
    attacks = ["BITE", "WOUND", "STUN", "SCHEME"]
    print("Attacks: " + str(attacks).replace("[]", "").replace("'", ""))
    attack = input()
    attack = attack.upper()

    bitevar = ["BITE"]
    woundvar = ["WOUND"]
    stunvar = ["STUN"]
    schemevar = ["SCHEME"]

    # Player attack

    # Base Attack Stat
    if containsAny(attack, bitevar):
        return attack

    # First Attack
    elif containsAny(attack, woundvar):
        return attack

    # Second Attack
    elif containsAny(attack, stunvar):
        return attack

    # Third Attack
    elif containsAny(attack, schemevar):
        return attack

    else:
        return False


def enemy_attack():
    print()
    if config.enemy.getAtk() <= config.player.getDef():
        print(config.enemy.getName() + " attacks you!")
        print("Your defense completely absorbs the blow!")
        print()
    else:
        amt = config.enemy.getAtk() - config.player.getDef()
        config.player.take_hit(amt)
        print(config.enemy.getName() + " hits you for " + str(amt) + " !")
        print("Your defense softens the blow by " + str(config.player.getDef()) + "!")
        print()


def player_attack(attack):
    global enemy_wounded
    global turns_wounded
    global turns_stunned
    global enemy_stunned

    bitevar = ["BITE"]
    woundvar = ["WOUND"]
    stunvar = ["STUN"]
    schemevar = ["SCHEME"]
    filler3 = ["filler3"]

    # Player attack

    # Base Attack Stat
    if containsAny(attack, bitevar):
        bite()

    # First Attack
    elif containsAny(attack, woundvar):
        if enemy_wounded is True:
            print(config.enemy.getName() + " is already wounded!")
            print()
            return False
        else:
            turns_wounded = wound()
            if turns_wounded is False:
                return "false"
            else:
                enemy_wounded = True

    # Second Attack
    elif containsAny(attack, stunvar):
        if enemy_stunned is True:
            print(config.enemy.getName() + " is already stunned!")
            print()
            return False
        else:
            turns_stunned = stun()
            if turns_stunned is False:
                return "false"
            else:
                enemy_stunned = True

    # Third Attack
    elif containsAny(attack, schemevar):
        scheme()

    # Four Attack
    elif containsAny(attack, filler3):
        pass

    else:
        print("Attack not found")
        return False


def player_first():
    global attack

    player_attack(attack)

    # Enemy attack
    if enemy_stunned is True:
        stun_enemy()
    else:
        if config.enemy.getHp() <= 0:
            pass
        else:
            enemy_attack()


def enemy_first():
    global attack

    # Enemy Attack
    if enemy_stunned is True:
        stun_enemy()
    else:
        if config.enemy.getHp() <= 0:
            pass
        else:
            enemy_attack()

    # Player Attack
    player_attack(attack)


def Wolf_Combat():
    global enemy_wounded
    global turns_wounded
    global turns_stunned
    global enemy_stunned
    global attack

    print("You transform into your wolf form.")
    print()

    while config.enemy.getHp() > 0:

        # Set Speed randomly every loop
        tempplayerspeed = randrange(config.player.getSpeed(), config.player.getSpeed() * 2)
        tempespeed = randrange(config.enemy.getSpeed(), config.enemy.getSpeed() * 2)

        # Multiple deaths form a list. Choose random -----------------------
        if config.player.getHp() <= 0:
            config.enemy.killPlayer()
            quit()

        # ------------------------------------------------------------------
        elif config.enemy.getHp() <= 0:
            break

        else:

            attack = choose_attack()
            if attack is False:
                print("Attack not found")
                print()
                continue

            # Enemy attacks first
            if tempespeed > tempplayerspeed:
                print(config.enemy.getName() + " attacks first!")
                enemy_first()

            # Player attacks first
            elif tempplayerspeed >= tempespeed:
                player_first()

            # Check conditionals
            if enemy_wounded is True:
                wound_enemy()
                turns_wounded = turns_wounded - 1

            elif enemy_stunned is True:
                turns_stunned = turns_stunned - 1

            elif turns_wounded == 0:
                enemy_wounded = False
                print(config.enemy.getName() + " is no longer wounded!")
                turns_wounded = -1

            elif turns_stunned == 0:
                enemy_stunned = False
                print(config.enemy.getName() + " is no longer stunned!")
                turns_stunned = -1

            # Display stats
            print()
            config.enemy.display_stats()
            config.player.display_stats()
            print()

    print()
    print("The " + config.enemy.getName() + " has been defeated!")

    # Set everything back to normal for next combat
    config.player.setAtk(config.player.getMaxAtk())
    enemy_wounded = False
    enemy_stunned = False
    turns_wounded = -1
    turns_stunned = -1

    print()
