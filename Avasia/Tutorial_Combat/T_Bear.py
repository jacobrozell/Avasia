from Avasia.Logic.util import containsAny
from Avasia.Class.Bear_Attacks import *
double = 0
storeActive = False
attack = ""
tempMaxAtk = config.player.getMaxAtk()
tempMaxDef = config.player.getMaxDef()


def choose_attack():
    global attack
    print("Choose an attack!")
    attacks = ["SWIPE", "STORE", "ROAR", "GUARD"]
    print("Attacks: " + str(attacks).replace("[]", "").replace("'", ""))
    attack = input()
    attack = attack.upper()
    swipevar = ["SWIPE"]
    storevar = ["STORE"]
    roarvar = ["ROAR"]
    guardvar = ["GUARD"]
    breakvar = ["QUIT"]
    helpvar = ["HELP"]

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

    elif containsAny(attack, breakvar):
        return "quit"

    elif containsAny(attack, helpvar):
        return "help"

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
    while True:

        double -= 1
        attack = choose_attack()

        if attack is False:
            print("Attack not found")
            continue

        elif attack == "quit":
            break

        elif attack == "help":
            print("\nSwipe simply does your attack stat on the target.")
            print("Store lowers your defense to 0, and doubles your attack stat for one turn.")
            print("Roar lowers your defense by 5, and raises your attack by 5.")
            print("Guard raises your defense by 5.\n")
            continue

        # Player Attacks
        bool = player_attack(attack)
        if bool is False:
            print("Attack not found")
            continue

        if double == 0:
            config.player.setAtk(tempMaxAtk)
            config.player.setDef(tempMaxDef)
            config.player.setLuck(config.player.getMaxLuck())
            storeActive = False
            print("Store wore off.")
            print()
        else:
            double -= 1

        print()
        config.enemy.display_stats()
        config.player.display_stats()
        print()

    print()
    config.player.setAtk(config.player.getMaxAtk())
    config.player.setDef(config.player.getMaxDef())
    print("You quit fighting the training dummy.")
    print()

