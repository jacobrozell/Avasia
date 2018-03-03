from Avasia.Room.Room import Room


def hunter_path():
    print("That's the trail hunters use to go hunt.")
    print("You should make your way to the courtyard.")
    print()
    return "go back"

hunter_path = Room(name="", des="", id="hunter_path", directions="", on_enter=hunter_path)
