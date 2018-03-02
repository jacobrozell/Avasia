from Avasia.Room.Room import *


def alt_house_logic():
    print()
    print(">>>Althalos' Wares<<<")
    print("\n\n")
    print("\nYou approach Althalos' shop.")
    print("\nThe sight of the " + """ "Althalos' Wares" """ + "sign sparks past memories of the eccentric shopkeeper.\n")
    print("\nYou enter and immediately notice the shop is completely absent of people, yet overstocked in goods.")
    print("\nDespite the lack of business, Althalos greets you kindly.\n")
    talk("Ah, " + config.player.getName() + ", I hear you're joining the Cataractan Legion!")
    talk("\nIt's mighty brave of you to volunteer!")
    talk("\nMost would wait to be drafted, but not you!")
    talk("\nI wish I had something to give you, but business hasn't been so good lately.")
    talk("\nIf you ever need anything, you know exactly where to find me!")
    talk("\nThe shopkeepers life is the life for me! Even if it's a cruel one.")
    talk("\nI wish you a safe and peaceful service to the Cataractan army.")
    print("\n\n")
    print("You thank Althalos and leave with a smile.")
    print()
    return "go back"   # return


althalos_house = Room(name="", des="", id="althalos_house", directions="", on_enter=alt_house_logic)
