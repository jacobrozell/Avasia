from Avasia.Room.Room import *


def alt_house_logic():
    althalos_house.print_name()
    print("You approach Althalos' house."
          "\nThe sight of the " + """ "Althalos' Wares" """ + "sign sparks past memories of the eccentric shopkeeper."
          "\n"
          "\nYou enter and immediately notice the shop is completely absent of people but overstocked in goods."
          "\n"
          "\nNone-the-less, Althalos greets you kindly.")
    talk("Ah! I hear you are joining the Cataractan Army.")
    talk("It's mighty brave of you to volunteer.")
    talk("I wish I had something to give you, but business hasn't been so good lately.")
    talk("If you ever need anything, you know exactly where to find me!")
    talk("The shopkeepers life is the life for me! Even if it's a cruel one.\n")
    talk("I wish you a safe and peaceful service to the Cataractan army.\n\n")
    print("You thank Althalos and leave with a smile of nostalgia at the poor shopkeeper.\n")
    return "go back"   # return

althalos_house = Room(name="Althalos' House", des="", id="althalos_house", directions="", on_enter=alt_house_logic)
