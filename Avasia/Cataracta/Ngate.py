from Room.Room import Room


def nGate():
    print("You can't leave Cataracta now!")
    print("Head over to the Legion's courtyard to begin your training.")
    print()
    return "go back"


nGate = Room(name="", des="", id="nGate", directions="", on_enter=nGate)
