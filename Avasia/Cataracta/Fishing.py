from Avasia.Logic.util import *
import Avasia.Logic.config as config
import Avasia.Logic.Item_Storage as Item_Storage
from random import randint


def fishing():
    print()
    print(">>>Fishing<<<")
    print()
    print("You see the rippling water surrounding you.")
    print("You feel the cool breeze of you the wind over the water.")
    bait = randint(4, 7)
    while True:
        bait -= 1
        print("It seems you have enough bait to last " + str(bait) + " casts.")
        print()

        # When you run out of bait
        if bait == 0:
            print("You ran out of bait!")
            print("You return your rod to Doran!")
            print("Get more bait and try again!")
            print()
            break

        ans = input("Throw your cast in the water?")
        print()
        ans.upper()
        y = ["YES", "Y"]
        no = ["NO", "N"]
        if containsAny(ans, y):
            item = randint(1, 10)

            # Old shoe
            if item == 1:
                print("You fish up an " + Item_Storage.oldshoe.name + "!")
                Item_Storage.oldshoe.print_stats()
                config.player.give_item(Item_Storage.oldshoe)
                print()
                continue

            # Small Fish
            if item == 2:
                print("You fish up a " + Item_Storage.smallfish.name + "!")
                Item_Storage.smallfish.print_stats()
                config.player.give_item(Item_Storage.smallfish)
                print()
                continue

            # Rusty Sword
            if item == 3 and config.varrustysword == 0:
                print("You fish up a " + Item_Storage.rustysword.name + "!")
                Item_Storage.rustysword.print_stats()
                config.player.give_item(Item_Storage.rustysword)
                print()
                config.varrustysword = 1
                continue
            if item == 3 and config.varrustysword == 1:
                print("You wait a few minutes but catch nothing.")
                print()
                continue

            # Money Purse
            if item == 4:
                print("You fish up a Soggy-Money Purse!")
                ammount = randint(1, 30)
                print("You add " + str(ammount) + " gold to your backpack!")
                config.player_gold.add_gold(ammount)
                config.player_gold.gold_count()
                print()
                continue

            # Broken Axe
            if item == 5 and config.varbrokenaxe == 0:
                print("You fish up an " + Item_Storage.brokenaxe.name + "!")
                Item_Storage.brokenaxe.print_stats()
                config.player.give_item(Item_Storage.brokenaxe)
                print()
                config.varbrokenaxe = 1
                continue
            if item == 5 and config.varbrokenaxe == 1:
                print("You wait a few minutes but catch nothing.")
                print()
                continue

            # Big fish
            if item == 6:
                print("You fish up a " + Item_Storage.bigfish.name + "!")
                Item_Storage.bigfish.print_stats()
                config.player.give_item(Item_Storage.bigfish)
                print()
                continue

            # Catch Nothing
            if item == 7 or item == 8 or item == 9 or item == 10:
                print("You fish up a heavy amount of seaweed.")
                print("You throw it back over the pier.")
                print()
                continue
        elif containsAny(ans, no):
            print("You thank Doran and return the fishing pole.")
            print("You leave the pier.")
            print()
            config.current_room_id = "southeast_c"
            break
        else:
            print()
