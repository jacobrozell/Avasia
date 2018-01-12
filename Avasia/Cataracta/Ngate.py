from Avasia.Room.Room import *


def ngAte():
    print("You can't leave Cataracta now!")
    print("Enter the courtyard to start your training.")
    print()
    return "go back"


nGate = Room(name="", des="", id="nGate", directions="", on_enter=ngAte)
