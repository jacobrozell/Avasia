from Avasia.Room.Room import *
from random import randint
from Avasia.Logic.util import *


def c_fountain_logic():
    print()
    print(">>>Castle Gardens<<<")
    print()
    print(
        "\n"
        "\nAround the garden are young children playing while their parents socialize."
        "\nIn front of you is a fountain made of the crystal, Anula."
        "\nThe fountain is filled with gold pieces, scattered around the base,"
        "\nmost of which are on tails."
        "\n")
    while True:
        ans = input("What would you like to do?")
        print()
        coin = ["COIN", "THROW"]
        talk = ["TALK", "APPROACH", "SPEAK", "PEOPLE"]
        leave = ["LEAVE", "BACK", "RETURN", "WEST"]
        if containsAny(ans, coin) and config.fountain == 0:
            roll = randint(0, 1)
            print()
            if roll == 0:
                # gold - 1
                print("You toss a gold piece into the water and it lands on tails.")
                print("Nothing happens.")
                print()
                config.fountain = 1
            if roll == 1:
                config.player_gold -= 1
                print("You toss a gold piece into the water and it lands on heads!!!")
                print("Maybe luck will come your way!")
                print()
                config.fountain = 1
        elif containsAny(ans, coin):
            print()
            print("You already tossed a coin in the water.")
            print()
        elif containsAny(ans, talk):
            print()
            print("You approach someone standing by the crystal fountain.")
            print()
            print(""" "They say if you toss some gold in the fountain, it brings good luck!" """)
            print()
        elif containsAny(ans, leave):
            config.current_room_id = "middle_c"
            break


c_fountain = Room(name="", des="", id="c_fountain", directions="", on_enter=c_fountain_logic)


