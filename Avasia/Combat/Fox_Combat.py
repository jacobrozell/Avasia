from Class.Fox_Attacks import *
from Logic.util import containsAny
import Logic.config as config


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
    while config.enemy.getHp() > 0:

        # Player dies ------------------------------------------------------
        if config.player.getHp() <= 0:
            config.enemy.killPlayer()
            quit()

        # Enemy dies -------------------------------------------------------
        elif config.enemy.getHp() <= 0:
            print(config.enemy.getName() + " was defeated!")
            break
        else:

            # Player (Fox) ALWAYS attacks first

            # Player Attacks
            attack = choose_attack()
            if attack is False:
                print("Attack not found.")
            else:
                player_attack(attack)

            # Enemy Attack
            if config.enemy.getHp() <= 0:
                break
            else:
                enemy_attack()

            # Display stats
            print()
            config.enemy.display_stats()
            config.player.display_stats()
            print()
    print()
    print("The " + config.enemy.getName() + " has been defeated!")

    # Always sets luck back to max at the end of combat.
    config.player.setLuck(config.player.getMaxLuck())
    print()
