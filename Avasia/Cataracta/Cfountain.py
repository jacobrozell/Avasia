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
        "\nThe fountain is filled with gold pieces, scattered around the base, "
        "most of which are on tails."
        "\n")
    while True:
        ans = input("What would you like to do?")
        print()
        coin = ["COIN", "THROW"]
        tal = ["TALK", "APPROACH", "SPEAK", "PEOPLE"]
        leave = ["LEAVE", "BACK", "RETURN", "WEST"]
        if containsAny(ans, coin) and config.fountain == 0:
            roll = randint(0, 1)
            print()
            if roll == 0:
                config.player_gold -= 1
                print("You toss a gold piece into the water and it lands on tails.")
                print("Nothing happens.")
                print()
                config.fountain = 1
            if roll == 1:
                config.player_gold -= 1
                print("You toss a gold piece into the water and it lands on heads!")
                print("Nothing happens.")
                print()
                config.fountain = 1
        elif containsAny(ans, coin):
            print()
            print("You already tossed a coin in the water.")
            print()
        elif containsAny(ans, tal):
            print()
            print("You approach someone a young boy by the crystal fountain.")
            print()
            talk("My parents say that if you toss some gold in the fountain, it brings good luck!")
            talk("I don't know if I believe in stuff like that though...")

            print()
        elif containsAny(ans, leave):
            return "go back"


c_fountain = Room(name="", des="", id="c_fountain", directions="", on_enter=c_fountain_logic)


