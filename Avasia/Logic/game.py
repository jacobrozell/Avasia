# --------- Things to do ---------
# Add more story -JR
# Make next city - JR
# Destroy all paths to cataracta - JR
#
# Change Combat to be outside of Cataracta and leave cataracta NOT destroyed?
#
# --------------------------------

# Rooms
from Avasia.Logic.Room_Storage import *

# Util
import Avasia.Logic.util as util
import Avasia.Logic.config as config
# ----------------------------------------------------------------


# READ COMMENTS FOR EXPLANATION OF WHAT IS GOING ON


# Dictionary that holds every room object
# Its in Key, Value pairs.
# The unique id of the room points to the room itself
# So instead of making importing the specific room every time we want to change, we can just point to its id
all_rooms_id = {}


# This is where the id get's set to the room itself.
def register_area(room):
    all_rooms_id[room.id] = room


# Where the magic truly happens:
def mainloop():
    inventory = ["INVENTORY"]
    all_commands = ["INVENTORY", "EAT", "DRINK"]
    eat = ["EAT", "DRINK"]
    help = ["HELP", "COMMANDS"]
    current_room = None

    while True:

        # Keep track of the old room if and only if there was an old room
        old_room_id = None if current_room is None else current_room.id

        # Current room = look for the id of the current room and return the room itself
        current_room = all_rooms_id[config.current_room_id]

        # does the room return anything?
        # Such as "reload" or "go back"
        event_result = current_room.event()

        # Reload skips over the "Which way would you like to investigate?" and reloads the room.
        # If you don't reload between room changes (in certain cases)
        # then the room A to room B will have the "which way would you..." in between switches

        # ^^^^ You'll know this bug when you see it.
        if event_result == "reload":
            continue

        # return "go back" in a room to return to the old_room_id.
        # This is useful for rooms that have no directions in them. (Don't go anywhere)
        elif event_result == "go back":
            config.current_room_id = old_room_id
            continue

        print()
        command = input("Which way would you like to investigate?")
        command.upper()

        # Show list of all commands
        if containsAny(command, help):
            print(str(all_commands).replace("'", ""))
            print("Enter these anywhere!")
            print()

        # Print the players inventory
        elif containsAny(command, inventory):
            print()
            config.player.printplayerinventory()
            print()

        # Eat food / drink potion:
        elif containsAny(command, eat):

            if config.player.hp < config.player.maxhp:

                print("What item do you want to eat/drink?")
                print()

                # Get input for which item_id the user wants to eat/drink
                itemToBeEaten = input(str(config.player.printplayerinventory()))

                # Search for item_id and RETURN THE ITEM ITSELF and set it to item_object
                item_object = config.player.return_item(itemToBeEaten)

                # If the Item wasn't actually found:
                if item_object == "false":
                    print("Item not found!")
                    print()
                    continue

                # We found the object but let's check and make sure the user isn't trying to eat gold or some shit
                if item_object.type == "edible":
                    config.player.eat_food(item_object.getAmt())
                    print("Health restored by " + str(item_object.getAmt()) + "!")
                    config.player.display_stats()
                    print()

            # Health is full
            else:
                print()
                print("Health is full!")
                print()

        else:

            # If the command isn't any of those... Then it must be a direction
            # The direction function is found in Room Class
            current_room.direction(command)
            print()


# To make a new room,
# 1. you need to register it here,
# 2. add the import to Room_Storage
# 3. make the room,
# 4. and make sure you set the path in the directions in the room that leads to it.


# When this inevitably gets super huge... Add new file and import the registers.
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
register_area(fishing_room)
# -------------------------------------------------------------------------------


# Call the intro()
# Start the mainloop()
util.intro()
while True:
    mainloop()
