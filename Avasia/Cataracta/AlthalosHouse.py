from Room.Room import Room
from Logic.util import talk, config


def alt_house_logic():
    althalos_house.print_name()
    print("\nYou approach Althalos' shop.")
    print(
        "\nThe sight of the " + """ "Althalos' Wares" """ + "sign sparks past memories of the eccentric shopkeeper.\n")
    print("\nYou enter and immediately notice the shop is completely absent of people, yet overstocked in goods.")
    print("\nDespite the lack of business, Althalos greets you kindly.\n")
    talk("Ah, " + config.player.getName() + ", I hear you're joining the Cataractan Legion!")
    talk("It's mighty brave of you to volunteer!")
    talk("Most would wait to be drafted, but not you!")
    print("\nThe man looks at you with a look you can only guess is pride.\n")
    talk("Listen. I wish I had something to give you, but business hasn't been so good lately.")
    talk("If you ever need anything, you know exactly where to find me!")
    print()
    talk("Take care, son. And, good luck!")
    print("\nYou thank Althalos and leave with a smile.\n")
    return "go back"


althalos_house = Room(name="Althalos' House", des="", id="althalos_house", directions="", on_enter=alt_house_logic)
