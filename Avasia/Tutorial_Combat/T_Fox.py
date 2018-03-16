from Avasia.Class.Fox_Attacks import *
from Avasia.Logic.util import containsAny
import Avasia.Logic.config as config


def choose_attack():
    print("Choose an attack!")
    attacks = ["CLAW", "FOCUS", "EXECUTE", "FATALITY"]
    print("Attacks: " + str(attacks).replace("[]", "").replace("'", ""))
    attack = input()
    attack = attack.upper()
    clawvar = ["CLAW"]
    focusvar = ["FOCUS"]
    executevar = ["EXECUTE"]
    fatalityvar = ["FATALITY"]
    breakvar = ["QUIT"]
    helpvar = ["HELP"]

    if containsAny(attack, clawvar):
        return attack

    # First Attack
    elif containsAny(attack, focusvar):
        return attack

    # Second Attack
    elif containsAny(attack, executevar):
        return attack

    # Third Attack
    elif containsAny(attack, fatalityvar):
        return attack

    elif containsAny(attack, breakvar):
        return "quit"
    
    elif containsAny(attack, helpvar):
        return "help"

    else:
        return False


def player_attack(attack):
    clawvar = ["CLAW"]
    focusvar = ["FOCUS"]
    executevar = ["EXECUTE"]
    fatvar = ["FATALITY"]

    # Player attack

    # Base Attack Stat
    if containsAny(attack, clawvar):
        claw()

    # First Attack
    elif containsAny(attack, focusvar):
        focus()

    # Second Attack
    elif containsAny(attack, executevar):
        execute()

    # Third Attack
    elif containsAny(attack, fatvar):
        fatality()

    else:
        return False


def Fox_Combat():
    print("You transform into your Fox form.")
    print()
    config.enemy.display_stats()
    config.player.display_stats()
    print()

    while True:

        # Player (Fox) ALWAYS attacks first

        # Player Attacks
        attack = choose_attack()
        if attack is False:
            print("Attack not found.")

        elif attack == "quit":
            break

        elif attack == "help":
            print("\nClaw simply does your attack stat on the enemy.")
            print("Focus increases your chance of hitting the enemy.")
            print("Execute will one shot the enemy, if and only if it hits.")
            print("Fatality will kill an enemy automatically that is near death.\n")
            continue

        else:
            player_attack(attack)

            if config.enemy.getHp() <= 0:
                print("\nTraining dummy has been reset.\n")
                config.enemy.setHp(1000)

        # Display stats
        print()
        config.enemy.display_stats()
        config.player.display_stats()
        print()

    print()
    print("You quit fighting the training dummy.")

    # Always sets luck back to max at the end of combat.
    config.player.setLuck(config.player.getMaxLuck())
    print()
