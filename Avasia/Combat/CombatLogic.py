import Avasia.Logic.config as config
from Avasia.Logic.util import containsAny
from Avasia.Combat.Bear_Combat import Bear_Combat
from Avasia.Combat.Fox_Combat import Fox_Combat
from Avasia.Combat.Wolf_Combat import Wolf_Combat


def combat():
    print("An " + config.enemy.getName() + " appeared!")
    print("Which form would you like to shift into for this battle?")
    config.player.printForms()
    form = input()
    form.upper()
    bear = ["BEAR"]
    fox = ["FOX"]
    wolf = ["WOLF"]

    if containsAny(form, bear):
        if config.player.searchForm("bear") is True:
            Bear_Combat()
            config.player.comabtExp()
        else:
            print("You don't know that form!")
            print()
            return False

    elif containsAny(form, fox):
        if config.player.searchForm("fox") is True:
            Fox_Combat()
            config.player.comabtExp()
        else:
            print("You don't know that form!")
            print()
            return False

    elif containsAny(form, wolf):
        if config.player.searchForm("wolf") is True:
            Wolf_Combat()
            config.player.comabtExp()
        else:
            print("You don't know that form!")
            print()
            return False

    else:
        print("Invalid command")
        print()
        return False


