import Logic.config as config

# Wolf


# Standard attack stat
def strike():
    amt = config.player.getAtk() + config.enemy.getDef()
    config.enemy.take_hit(amt)
    print()
    print("You use strike!")
    print("The " + config.enemy.getName() + " took " + str(config.player.getAtk() - config.enemy.getDef()) + " damage!")
    print("The " + config.enemy.getName() + "'s defense softened the blow by " + str(config.enemy.getDef()) + "!")
    print()


# lowers enemy defense by 5
def pounce():
    new_atk = config.player.getAtk() - 5
    print()
    print("You use pounce!")
    if config.enemy.getDef() > 0:
        config.enemy.setDef(config.enemy.getDef() - 5)
        print(config.enemy.getName() + " had his defense lowered to " + str(config.enemy.getDef()) + "!")
    if config.enemy.getDef() == 0:
        print(config.enemy.getName() + " can't have his defense lowered anymore!")

    config.enemy.take_hit(new_atk)
    print("The " + config.enemy.getName() + " took " + str(new_atk) + " damage!")
    print()


# raises attack
def filler():
    pass
