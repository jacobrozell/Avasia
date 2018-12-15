import Logic.config as config
from Logic.util import containsAny

# Set new links
from Tutorial_Combat.T_Wolf import Wolf_Combat
from Tutorial_Combat.T_Bear import Bear_Combat
from Tutorial_Combat.T_Fox import Fox_Combat


def T_combat():
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
        else:
            print("You don't know that form!")
            print()
            return False

    elif containsAny(form, fox):
        if config.player.searchForm("fox") is True:
            Fox_Combat()
        else:
            print("You don't know that form!")
            print()
            return False

    elif containsAny(form, wolf):
        if config.player.searchForm("wolf") is True:
            Wolf_Combat()
        else:
            print("You don't know that form!")
            print()
            return False

    else:
        print("Invalid command")
        print()
        return False


