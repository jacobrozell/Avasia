import Avasia.Logic.config as config

# Wolf


# Standard attack stat
def strike():
    config.enemy_hp -= config.player_atk + config.enemy_defense
    print()
    print("You use strike!")
    print("The " + config.enemy_name + " took " + str(config.player_atk - config.enemy_defense) + " damage!")
    print("The " + config.enemy_name + "'s defense softened the blow by " + str(config.enemy_defense) + "!")
    print(config.enemy_name + " has " + str(config.enemy_hp) + " left!")
    print()


# lowers enemy defense by 5
def pounce():
    new_atk = config.player_atk - 5
    print()
    print("You use pounce!")
    if config.enemy_defense > 0:
        config.enemy_defense -= 5
        print(config.enemy_name + " had his defense lowered to " + str(config.enemy_defense) + "!")
    if config.enemy_defense == 0:
        print(config.enemy_name + " can't have his defense lowered anymore!")

    config.enemy_hp -= new_atk
    print("The " + config.enemy_name + " took " + str(new_atk) + " damage!")
    print(config.enemy_name + " has " + str(config.enemy_hp) + " left!")
    print()


# raises attack
def filler():
    pass
