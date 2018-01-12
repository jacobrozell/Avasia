# --------- Things to do ---------
# Add more story -JR
# Make next city - JR
# Destroy all paths to cataracta - JR
# Fix equip weapon - JR
# Fix un-equip weapon -JR
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# --------------------------------

# Rooms
from Avasia.Logic.Room_Storage import *

# Util
import Avasia.Logic.util as util
import Avasia.Logic.config as config

# ----------------------------------------------------------------


def search_item(item):
    item.replace(" ", "").title()
    if item in config.player.inventory:
        return item
    else:
        print("404: Item not found.")

rooms_id = {}


def register_area(room):
    rooms_id[room.id] = room


def mainloop():
    inventory = ["INVENTORY"]
    equip = ["EQUIP"]
    all_commands = ["INVENTORY", "EQUIP", "EAT"]
    eat = ["EAT"]
    help = ["HELP", "COMMANDS"]
    current_room = None
    while True:
        old_room_id = None if current_room is None else current_room.id
        current_room = rooms_id[config.current_room_id]
        event_result = current_room.event()
        if event_result == "reload":  # Room Conditional
            continue
        elif event_result == "go back":
            config.current_room_id = old_room_id
            continue

        print()
        command = input("Which way would you like to investigate?")
        command.upper()

        if containsAny(command, help):
            print(str(all_commands))
            print("Enter these anywhere!")
            print()

        elif containsAny(command, inventory):
            print()
            config.player.printplayerinventory()
            print()

        # Doesnt work yet.
        elif containsAny(command, equip):
            if len(config.player.inventory) == 0:
                print("You have no items in your inventory.")
                continue
            print("Which item would you like to equip?")

            item = input(config.player.printplayerinventory())
            item.upper()
            nitem = search_item(item)
            if nitem.type == "equipable":

                if nitem.self == "weapon":
                    config.player.equip_weapon(nitem)
                else:
                    print("THEN ITS ARMOR.")
            else:
                print("That item is not equipable!")
                print()

        # Doesnt work yet.
        elif containsAny(command, eat):
            if config.player.hp < config.player.maxhp:
                print("What item do you want to eat?")
                item = input(config.player.printplayerinventory())
                nitem = search_item(item)
                if nitem in config.player.inventory:
                    if nitem.type == "edible":
                        config.player.eat_food(nitem.restored_ammount)
            else:
                print()
                print("Health is full!")
                print()

        else:
            current_room.direction(command)
            print()

# To make a new room,
# 1. you need to register it here,
# 2. add the import to Room_Storage
# 3. make the room,
# 4. and make sure you set the path in the directions in the room that leads to it.

register_area(southwest_c)
register_area(althalos_house)
register_area(southeast_c)
register_area(ulric_house)
register_area(c_pier)
register_area(middle_c)
register_area(c_fountain)
register_area(north_c)
register_area(courtyard)
register_area(hunter_path)
register_area(west_cataracta)
register_area(nGate)


util.intro()
while True:
    mainloop()
