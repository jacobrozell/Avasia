from Room.Room import Room


def nGate():
    print("Leaving Cataracta now, would make you a deserter.")
    print("Head over to the Legion's courtyard to begin your training.")
    print()
    return "go back"


nGate = Room(name="", des="", id="nGate", directions="", on_enter=nGate)
