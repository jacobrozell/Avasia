from Room.Room import Room
from Logic.util import talk, containsAny
import Logic.config as config


def library_logic():

    # No print() after print_name()
    n_library.print_name()
    print("The library is covered from wall to wall with seemingly endless shelves of books.")
    print("Some of the texts are as ancient, as they are endless.")
    print("Suddenly, a woman in ornate purple robes approaches you.")

    talk("What are you doing here, druid? How did you get here?")
    print()
    print("You don't want any confrontation with the woman, so you tell her everything.")
    print("How you are a recruit for the once, and now, all dead Cataractan army.")
    print("You tell her about Vashirr and how he teleported, in mass, all the Agromanians.")
    print()
    print("The woman is speechless.")
    print("She puts her hands on head and looks down.")
    print("Abruptly, she says:")
    talk("We must go and alert the king!")
    talk("Follow me.")
    print()
    print("The woman goes out a grand door to the SOUTH of you.")
    print()
    ans = input("What do you want to do?")
    ans.upper()
    south = ["SOUTH"]

    if containsAny(ans, south):
        print("You run out the southern door to follow the woman.")
        print()
        config.current_room_id = "west_hallway"


n_library = Room(des="",
                     directions="",
                     name="Nascastrum Library",
                     id="n_library",
                     on_enter=library_logic)