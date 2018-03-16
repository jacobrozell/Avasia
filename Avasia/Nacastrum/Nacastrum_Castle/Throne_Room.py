from Avasia.Room.Room import Room
from Avasia.Logic.util import talk, containsAny
import Avasia.Logic.config as config


def tr_logic():
    throne_room.print_name()
    print()


    # Input
    ans = input("What do you want to do?")
    ans.upper()
    south = ["SOUTH"]


throne_room = Room(des="",
                   directions="",
                   name="Nascastrum Trone Room",
                   id="throne_room",
                   on_enter=tr_logic)
