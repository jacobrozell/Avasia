import Logic.config as config
from Logic.util import containsAny
import Logic.save_game as save


class Bear():
    def __init__(self):
        self.classID = "bear"

    def swipe(self):
        bool = config.player.checkHit(config.player.getLuck())
        if bool is False:
            print()
            print("You missed!")
            print()

        else:
            amt = config.player.getAtk() - config.enemy.getDef()
            if amt < 0:
                amt = 0
            config.enemy.take_hit(amt)
            print()
            print("You swipe the " + config.enemy.getName() + " with your claws!")
            print("The " + config.enemy.getName() + " took " + str(amt) + " damage!")
            print("The " + config.enemy.getName() + "'s defense softened the blow by " + str(config.enemy.getDef()) + "!")
            print()

    def store(self):
        bool = config.player.checkHit(config.player.getLuck())
        if bool is False:
            print()
            print("Store failed!")
            print()
            return False
        else:
            print()
            print("You let your defense completely down and focus on exploiting " + config.enemy.getName() + "'s weaknesses.")
            print("Next turn, you have no defense but your attack is doubled.")
            print()
            return True

    def roar(self):
        bool = config.player.checkHit(config.player.getLuck() + 3)
        if bool is False:
            print()
            print("Roar failed!")
            print()
        else:
            print()
            print("You roar with all your might!")
            print()
            config.player.setDef(config.player.getDef() - 5)
            if config.player.getDef() < 0:
                print("Your defense is completely lowered!")
                print("Your attack stays the same!")
                print()
                config.player.setDef(0)
            else:
                config.player.setAtk(config.player.getAtk() + 5)
                print("Your defense has lowered!")
                print("Your attack has risen!")
                print()

    def guard(self):
        bool = config.player.checkHit(config.player.getLuck() + 3)
        if bool is False:
            print()
            print("Guard failed!")
            print()
        else:
            print()
            print("You focus and guard against enemy attacks.")
            print("Defense increased!")
            config.player.setDef(config.player.getDef() + 5)
            print()

    def enemy_attack(self):
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

    def choose_attack(self):
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

    def player_attack(self, attack):
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
            self.swipe()

        # First Attack
        elif containsAny(attack, storevar):
            if storeActive is True:
                print()
                print("You can't use store again!")
                print()
            else:
                # Store is now active == True
                storeActive = self.store()
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
            self.roar()
            tempMaxAtk = config.player.getAtk()
            tempMaxDef = config.player.getDef()

        # Third Attack
        elif containsAny(attack, guardvar):
            self.guard()
            tempMaxDef = config.player.getDef()

        else:
            return False

    def Bear_Combat(self):
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

            # Player dies ------------------------------------------------------
            if config.player.getHp() <= 0:
                config.enemy.killPlayer()

                while True:
                    ans = input("\nWould you like to start at the last save?\n")
                    if containsAny(ans, "yes"):
                        save.loadParameters()
                        return
                    elif containsAny(ans, "no"):
                        print("Thank you for playing!")
                        quit()
                    else:
                        pass

            # ------------------------------------------------------------------
            elif config.enemy.getHp() <= 0:
                print(config.enemy.getName() + " was defeated!")
                break

            else:

                double -= 1
                # Enemy Attack (ALWAYS FIRST)
                attack = self.choose_attack()
                if attack is False:
                    print("Attack not found\n")
                    config.enemy.display_stats()
                    config.player.display_stats()
                    print()
                    continue

                self.enemy_attack()

                # Player Attacks
                bool = self.player_attack(attack)
                if bool is False:
                    print("\nAttack not found\n")
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

