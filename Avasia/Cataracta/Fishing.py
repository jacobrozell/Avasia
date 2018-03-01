from Avasia.Logic.util import *
import Avasia.Logic.config as config
import Avasia.Logic.Item_Storage as Item_Storage
from random import randint
from Avasia.Room.Room import Room


def fishing():
    print()
    print(">>>Fishing<<<")
    print()
    print("You see the rippling water surrounding you.")
    print("You feel the cool breeze of you the wind over the water.")
    bait = randint(4, 7)
    oldshoe = 0
    smallfish = 0
    bigfish = 0
    while True:
        bait -= 1
        print("It seems you have enough bait to last " + str(bait) + " casts.")
        print()

        # When you run out of bait
        if bait == 0:
            print("You ran out of bait!")
            print()
            return "go back"

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
                oldshoe = 1
                continue

            if item == 1 and oldshoe == 1:
                print("Whole lot of nothing...")
                print()

            # Small Fish
            if item == 2:
                print("You fish up a " + Item_Storage.smallfish.name + "!")
                Item_Storage.smallfish.print_stats()
                config.player.give_item(Item_Storage.smallfish)
                print()
                smallfish = 1
                continue
            if item == 2 and smallfish == 1:
                print("Whole lot of nothing...")

            # Money Purse
            if item == 3 or item == 4 or item == 5:
                print("You fish up a Soggy-Money Purse!")
                amount = randint(1, 30)
                print("You add " + str(amount) + " gold to your backpack!")
                config.player_gold.add_gold(amount)
                config.player_gold.gold_count()
                print()
                continue

            # Big fish
            if item == 6:
                print("You fish up a " + Item_Storage.bigfish.name + "!")
                Item_Storage.bigfish.print_stats()
                config.player.give_item(Item_Storage.bigfish)
                print()
                bigfish = 1
                continue

            if item == 6 and bigfish == 1:
                print("Whole lot of nothing...")
                print()

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
            return "go back"
        else:
            print()

fishing_room = Room(name="", des="", id="fishing_id", directions="", on_enter=fishing)