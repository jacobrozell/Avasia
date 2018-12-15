from Class.Wolf_Attacks import *
from Logic.util import containsAny
import Logic.config as config
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
    breakvar = ["QUIT"]
    helpvar = ["HELP"]

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

    elif containsAny(attack, breakvar):
        return "quit"

    elif containsAny(attack, helpvar):
        return "help"

    else:
        return False


def player_attack(attack):
    global enemy_wounded
    global turns_wounded
    global turns_stunned
    global enemy_stunned

    bitevar = ["BITE"]
    woundvar = ["WOUND"]
    stunvar = ["STUN"]
    schemevar = ["SCHEME"]

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
                enemy_wounded = False
                turns_wounded = -1
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

    else:
        print("Attack not found")
        return False


def Wolf_Combat():
    global enemy_wounded
    global turns_wounded
    global turns_stunned
    global enemy_stunned
    global attack

    print("You transform into your wolf form.")
    print()
    config.enemy.display_stats()
    config.player.display_stats()
    print()

    while True:

        attack = choose_attack()
        if attack is False:
            print("Attack not found")
            print()
            continue

        elif attack == "quit":
            break

        elif attack == "help":
            print("\nBite simply does your attack stat on the target.")
            print("Wound will wound your enemy for 1 to 4 turns, for 75% of your attack stat.")
            print("Stun stuns your enemy for 1 to 3 turns.")
            print("Scheme increases your attack by 5.\n")
            continue

        player_attack(attack)

        # Check conditionals

        if turns_wounded == 0:
            enemy_wounded = False
            print(config.enemy.getName() + " is no longer wounded!")
            turns_wounded = -1

        elif turns_stunned == 0:
            enemy_stunned = False
            print(config.enemy.getName() + " is no longer stunned!")
            turns_stunned = -1

        elif enemy_wounded is True:
            wound_enemy(turns_wounded)
            turns_wounded = turns_wounded - 1

        elif enemy_stunned is True:
            turns_stunned -= 1

        # Display stats
        print()
        config.enemy.display_stats()
        config.player.display_stats()
        print()

    print()
    print("You quit fighting the training dummy.")

    # Set everything back to normal for next combat
    config.player.setAtk(config.player.getMaxAtk())
    enemy_wounded = False
    enemy_stunned = False
    turns_wounded = -1
    turns_stunned = -1

    print()
