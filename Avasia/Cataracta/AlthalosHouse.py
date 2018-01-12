from Avasia.Room.Room import *


def alt_house_logic():
    print()
    print(">>>Althalos' House<<<"
          "\n"
          "\n"
          "\nYou approach Althalos' house."
          "\nThe sight of the " + """ "Althalos' Wares" """ + "sign sparks past memories of the eccentric shopkeeper."
          "\n"
          "\nYou enter and immediately notice the shop is completely absent of people but overstocked in goods."
          "\n"
          "\nNone-the-less, Althalos greets you kindly."
          """\n"Ah! I hear you are joining the Cataractan Army." """
          """\n"It's mighty brave of you to volunteer." """
          """\n"I wish I had something to give you, but business hasn't been so good lately." """
          """\n"If you ever need anything, you know exactly where to find me!" """
          """\n"The shopkeepers life is the life for me! Even if it's a cruel one." """
          "\n"
          """\n"I wish you a safe and peaceful service to the Cataractan army." """)
    print()
    print()
    print("You thank Althalos and leave with a smile of nostalgia at the poor shopkeeper.")
    print()
    return "go back"   # return


althalos_house = Room(name="", des="", id="althalos_house", directions="", on_enter=alt_house_logic)
