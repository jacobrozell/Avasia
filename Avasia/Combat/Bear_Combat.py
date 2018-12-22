from Logic.util import containsAny
from Class.Bear_Attacks import *
double = 0
storeActive = False
attack = ""
tempMaxAtk = config.player.getMaxAtk()
tempMaxDef = config.player.getMaxDef()


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


def choose_attack():
    global attack
    print("Choose an attack!")
    attacks = ["SWIPE", "STORE", "ROAR", "GUARD"]
    print("Attacks: " + str(attacks).replace("[]", "").replace("'", ""))
    attack = input()
    attack = attack.upper()
    swipevar = ["SWIPE", "1"]
    storevar = ["STORE", "2"]
    roarvar = ["ROAR", "3"]
    guardvar = ["GUARD", "4"]

    if containsAny(attack, swipevar):
        return attack

    # First Attack
    elif containsAny(attack, storevar):
        return attack

    # Second Attack
    elif containsAny(attack, roarvar):
        return attack

    # Third Attack
    elif containsAny(attack, guardvar):
        return attack

    else:
        return False


def player_attack(attack):
    global double
    global storeActive
    global tempMaxAtk
    global tempMaxDef

    swipevar = ["SWIPE"]
    storevar = ["STORE"]
    roarvar = ["ROAR"]
    guardvar = ["GUARD"]

    # Player attack

    # Base Attack Stat
    if containsAny(attack, swipevar):
        swipe()

    # First Attack
    elif containsAny(attack, storevar):
        if storeActive is True:
            print()
            print("You can't use store again!")
            print()
        else:
            # Store is now active == True
            storeActive = store()
            if storeActive is False:
                return "false"
            else:
                # Lower defense and take full enemy hit
                config.player.setDef(0)

                # Double attack for next turn
                config.player.setAtk(config.player.getAtk() * 2)
                double = 2

                # Set luck to 1 so the attack will guarantee to hit
                config.player.setLuck(1)

    # Second Attack
    elif containsAny(attack, roarvar):
        roar()
        tempMaxAtk = config.player.getAtk()
        tempMaxDef = config.player.getDef()

    # Third Attack
    elif containsAny(attack, guardvar):
        guard()
        tempMaxDef = config.player.getDef()

    else:
        return False


def Bear_Combat():
    global double
    global storeActive
    global tempMaxAtk
    global tempMaxDef

    print("You transform into your bear form.")
    print()
    config.enemy.display_stats()
    config.player.display_stats()
    print()

    tempMaxAtk = config.player.getMaxAtk()
    tempMaxDef = config.player.getMaxDef()

    while config.enemy.getHp() > 0:

        # Multiple deaths form a list. Choose random -----------------------
        if config.player.getHp() <= 0:
            config.enemy.killPlayer()
            quit()

        # ------------------------------------------------------------------
        elif config.enemy.getHp() <= 0:
            print(config.enemy.getName() + " was defeated!")
            break

        else:

            double -= 1
            # Enemy Attack (ALWAYS FIRST)
            attack = choose_attack()
            if attack is False:
                print("Attack not found\n")
                config.enemy.display_stats()
                config.player.display_stats()
                print()
                continue

            enemy_attack()

            # Player Attacks
            bool = player_attack(attack)
            if bool is False:
                print("Attack not found\n")
                config.enemy.display_stats()
                config.player.display_stats()
                print()
                continue

            if double == 0:
                config.player.setAtk(tempMaxAtk)
                config.player.setDef(tempMaxDef)
                config.player.setLuck(config.player.getMaxLuck())
                storeActive = False
                print("Store wore off.")
                print()
                double = -1
            else:
                double -= 1

            print()
            config.enemy.display_stats()
            config.player.display_stats()
            print()
    print()
    config.player.setAtk(config.player.getMaxAtk())
    config.player.setDef(config.player.getMaxDef())
    print("The " + config.enemy.getName() + " has been defeated!")
    print()
