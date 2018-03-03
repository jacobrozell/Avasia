from Avasia.Room.Room import Room
from Avasia.Logic.util import talk


def portal_logic():
    c_portal_room.print_name()
    print("You stand in a room glimmering in red and blue light.")
    print("You look behind you and see the source of the light.")
    print("The Cataractan portal lies before you.")
    print("You look away in sadness.")

    talk("It's time to serve my people.\n")

    print("You look around the room.")
    print("It appears as this portal is rarely used, given by the condition of the room.")
    print("")
    print()

    # Add some options here
    # Maybe you can find a potion or some shit

    print("To the east is a door that appears to lead into a hallway.")

c_portal_room = Room(des="",
                     directions={"E": "west_hallway"},
                     name="Cataractan Portal Room",
                     id="c_portal_room",
                     on_enter=portal_logic)
