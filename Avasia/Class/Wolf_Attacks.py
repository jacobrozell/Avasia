import Avasia.Logic.config as config
from random import randint
from math import floor

# Wolf
# Theme: Damage over time
# 1. BASE ATTACK - BITE
# 2. Wound: enemy takes damage for 2-4 turns based off your current atk stat * .75
# 3. Stun: Stun target for 2-3 turns
# 4. Raise Stat Move


# Standard attack stat
def bite():
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
        print("You bite " + config.enemy.getName() + "!")
        print("The " + config.enemy.getName() + " took " + str(amt) + " damage!")
        print("The " + config.enemy.getName() + "'s defense softened the blow by " + str(config.enemy.getDef()) + "!")
        print()


# Wounds target fr 1-4 rounds
def wound():
    bool = config.player.checkHit(config.player.getLuck())
    if bool is False:
        print()
        print("You missed!")
        print()
        return False
    else:
        turns = randint(1, 4)
        print()
        print("You wound " + config.enemy.getName() + "!")
        print("The " + config.enemy.getName() + " will take damage every turn for " + str(turns) + " turns!")
        print()
        return turns


# Additional Logic for wound() attack
def wound_enemy(time):
    print()
    print("The " + config.enemy.getName() + " is still wounded for another " + str(time) + " rounds!")
    print("The " + config.enemy.getName() + " took " + str(floor((config.player.getAtk() * .75))) + " damage!")
    amt = floor((config.player.getAtk() * .75))
    config.enemy.take_hit(amt)
    print()


def stun():

    # Add to make it a lot harder to hit with this certain attack
    bool = config.player.checkHit(config.player.getLuck() + 5)
    if bool is False:
        print()
        print("You missed!")
        print()
        return False
    else:
        turns = randint(1, 3)
        print()
        print("You stun " + config.enemy.getName() + "!")
        print("The " + config.enemy.getName() + " will be unable to attack for " + str(turns) + " turns!")
        print()
        return turns


# Additional Logic for stun() attack
def stun_enemy():
    print()
    print("The " + config.enemy.getName() + " is still stunned!")
    print()


def scheme():
    bool = config.player.checkHit(config.player.getLuck() + 3)
    if bool is False:
        print()
        print("Scheme failed!")
        print()

    else:
        print()
        print("You look for weaknesses in the " + config.enemy.getName() + ".")
        print("Your attack has increased.\n")
        config.player.setAtk(config.player.getAtk() + 5)

