import Avasia.Logic.config as config
import Avasia.Logic.Item_Storage as item


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
    print("It has been 7 years since Vashirr, the old king of Nacastrum, betrayed Avasia."
          "\nThe Agromanians, a vicious people of the northwest, have remained idle since their attack on Oceandale."
          "\nNacastrum, the city of the Mage, is still being rebuilt under the diligent leadership of its new king."
          "\nRecently, news was brought to King Kaefden IV that Vashirr is teaching Agromanians magic."
          "\nWith this knowledge, King Kaefden IV has begun to recruit an army to march on the Agromanians before they have a chance to muster."
          "\n\nYou are a druid living in the peaceful city of Cataracta."
          "\nCataracta has formed a pact with the people of Aylova to join the fight when the time comes."
          "\nTh leader of Cataracta is drafting an army for the upcoming war and you have decided to volunteer."
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
    print("Today is the day you join Cataracta's Legion.")
    print("To join, you must head to the Legion's courtyard.")
    print("You collect your belongings and leave your home with a sense of pride.")
    print("\nType 'help' any time for a list of commands!")
    config.player_gold.add_gold(100)
    config.player.give_item(item.potion)
    print()
    config.current_room_id = "southwest_c"
