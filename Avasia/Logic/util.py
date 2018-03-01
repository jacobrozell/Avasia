import Avasia.Logic.config as config
import Avasia.Logic.Item_Storage as item
from Avasia.Player.PlayerClass import Player


def containsAny(string, options):
    for option in options:
        if option.upper() in string.upper():
            return True
    return False


def talk(message):
    print("\"" + message + "\"")


def intro():
    print()
    print("---------Avasia: Sword of Courage---------")
    print()
    print()
    print("History: It's been 7 years since Vashirr betrayed Kaefden."
          "\nThe Agromanians have remained idle since the attack on Oceandale."
          "\nNacastrum is still being rebuilt with the diligent leadership of its new king."
          "\nRecently, news was brought to King Kaefden that Vashirr is teaching Agromanians magic."
          "\nWith this knowledge, King Kaefden has begun to recruit an army to stand up against the Agromanians."
          "\n\nYou are a druid living in the great city of Cataracta."
          "\nCataracta's king is recruiting an army for the upcoming war and your name was the first on the list."
          "\nThis is where your story begins..."
          "\n")
    print("\n"
          "\n")
    while True:
        name = input("What is your name?")
        if name == "":
            print()
        else:
            yes = ["YES", "yes", "y", "Y"]
            print()
            print("Your name is " + name.title() + "? (yes/no)")
            ans = input("You can't change it once it's set.")
            print()
            if containsAny(ans, yes):
                config.player.setName(name.title())
                break
    print()
    print()
    print(">>>" + config.player.getName() + "'s House<<<")
    print()
    print()
    print("Today is the day you join the Cataractan Army."
          "\nYou'll have to make your way to the courtyard to begin training."
          "\nYou collect your belongings and leave your home with a new sense of duty to your fellow Cataractan.")
    config.player_gold.add_gold(100)
    config.player.give_item(item.potion)
    print()
    config.current_room_id = "southwest_c"
