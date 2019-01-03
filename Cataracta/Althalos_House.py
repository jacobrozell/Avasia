from Room.Room import Room
from Logic.util import talk
import Logic.config as Config


def alt_house_logic():
    althalos_house.print_name()
    print("You approach Althalos' shop.")
    print(
        "\nThe sight of the " + """ "Althalos' Wares" """ + "sign sparks memories of the eccentric shopkeeper.\n")
    print("\nYou enter and immediately notice the shop is completely absent of people, yet overstocked in goods.")
    print("\nDespite the lack of business, Althalos greets you kindly.\n")
    talk("Ah, " + Config.player.get_name() + ", I hear you're joining the Cataractan Legion!")
    talk("It's mighty brave of you to volunteer!")
    talk("Most would wait to be drafted, but not you!", "\n")
    talk("Listen. I wish I had something to give you, but business hasn't been so good lately.")
    talk("If you're ever looking to buy anything, I'll be here as always!", "\n")
    talk("Take care and good luck!")
    print("\nYou thank Althalos and leave.\n")
    return "go back"


althalos_house = Room(name="Althalos' House", des="", id="althalos_house", directions="", on_enter=alt_house_logic)
