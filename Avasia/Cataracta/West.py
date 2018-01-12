from Avasia.Room.Room import *


def west():
    print("The Trading District is closed today.")
    print()
    return "go back"


west_cataracta = Room(name="", des="", id="west_cataracta", directions="", on_enter=west)
