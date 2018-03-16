import Avasia.Logic.config as config
from math import floor

# Fox
# Theme: Quick, but little damage.
# 1. Raise user luck,
# 2. Always go first attack, # This is stupid. Fox will always go first anyway. His speed stat is stupid high
# 3. Automatically kills target if hit
# 4. Finishing move that will execute target if below 25% health
# 5. BASE ATTACK - Claw


# Standard attack stat
def claw():
    bool = config.player.checkHit(config.player.getLuck())
    if bool is False:
        print()
        print("You missed!")
        print()
    else:
        amt = config.player.getAtk() - config.enemy.getDef()
        if amt <= 0:
            print(config.enemy.getName() + " absorbs the blow!")
            print()
        else:
            config.enemy.take_hit(amt)
            print()
            print("You claw the " + config.enemy.getName() + "!")
            print("The " + config.enemy.getName() + " took " + str(config.player.getAtk() - config.enemy.getDef())
                  + " damage!")
            print("The " + config.enemy.getName() + "'s defense softened the blow by " + str(config.enemy.getDef()) + "!")
            print()


# Raise your chance of hitting
def focus():
    bool = config.player.checkHit(config.player.getLuck())
    if bool is False:
        print()
        print("Focus failed!")
        print()
    else:
        config.player.setLuck(config.player.getLuck() - 1)
        if config.player.getLuck() == 0:
            config.player.setLuck(1)
            print("Your chance of hitting is at the maximum capability.")
            print()
        else:
            print()
            print("You focus on the " + config.enemy.getName() + ".")
            print("Your chance of hitting have increased!")
            print()

    # Remember to set this back to normal after encounter!
        config.player.setLuck(config.player.getLuck() - 1)
        if config.player.getLuck() == 0:
            config.player.setLuck(1)


# Kills enemy if hit
def execute():
    bool = config.player.checkHit(config.player.getLuck() + 150)
    if bool is False:
        print()
        print("You missed!")
        print()
    else:
        print()
        print("You risk it all and lunge at the " + config.enemy.getName() + "'s head!")
        print("You execute the target on hit!")
        config.enemy.setHp(0)
        print()


# Kill enemy under 25% health if hit
def fatality():
    bool = config.player.checkHit(config.player.getLuck())
    if bool is False:
        print()
        print("You missed!")
        print()
    else:
        print()
        print("You attempt to finish off the " + config.enemy.getName() + "!")
        print()
        if (config.enemy.getHp() / config.enemy.getMaxHp()) <= .25:
            print("You attempt passed and you finish off the " + config.enemy.getName() + "!")
            print("Fatality!")
            print()
            config.enemy.setHp(0)
        else:
            amt = floor(config.player.getAtk() * .5) - config.enemy.getDef()
            if amt < 0:
                amt = 0
            config.enemy.take_hit(amt)
            print("Your attempt failed.")
            print("You managed to graze the " + config.enemy.getName() + " for " + str(amt) + ".")
            print()
