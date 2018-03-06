import Avasia.Logic.config as config

# Bear
# Theme: Slow, powerful.  Take hits and unleash them back in full force.
# 1. BASE ATTACK BASED OFF ATTACK STAT
# 2. Take hits for 2 turns and unleash them back doubled
# 3. The more faster the enemy, the more this attack does
# 4. Raise Def
# 5. ONCE PER ENCOUNTER - DOUBLE ATTACK STAT


# Standard attack stat
def swipe():
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


# Defense is 0, attack is doubled next turn
def store():
    bool = config.player.checkHit(config.player.getLuck())
    if bool is False:
        print()
        print("Store failed!")
        print()
    else:
        print()
        print("You let your defense completely down and focus on exploiting " + config.enemy.getName() + "'s weaknesses.")
        print("Next turn, you have no defense but your attack is doubled.")
        print()
        return True


# Lower defense by 5, raise attack by 5
def roar():
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


# Raise defense by 5
def guard():
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
