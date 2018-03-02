from Avasia.Room.Room import *
from Avasia.Logic.util import *


def pier_logic():
    c_pier.print_name()
    print("You enter into a fishing hut along side the river.")
    print("Smells of fresh fish and bait penetrate into your nostrils.")
    print("Various fishing poles line the walls in all shapes, sizes, and colors.")
    print()
    print("Doran, the owner, calls from behind the counter with a gruff, almost agitated voice.")
    print(""" "Hello. I'm Doran. Welcome to the my pier. """)
    print()
    while True:
        print("""\n"Would you like to fish for the price of 15 gold? You can keep whatever you find." """)
        ans = input()
        print()
        ans.upper()
        yes = ["YES"]
        no = ["NO", "LEAVE"]
        if containsAny(ans, yes):
            if config.ulric == 0:
                print(""" "Enjoy your time." """)
                print()
                print("You pay Doran 15 gold.")
                config.player_gold.subtract_gold(15)
                config.player_gold.gold_count()
                print("You grab a fishing rod and bait from the wall and exit onto the pier.")
                print()
                config.current_room_id = "fishing_id"
                return "reload"
            if config.ulric == 1:
                print(""" "Oh, you know my brother Ulric?" """)
                print()
                print(""" "He's always leading people over here to help the business out." """)
                print(""" "I'll stick to the tradition this last time." """)
                print(""" "Go ahead and enjoy your one free time!" """)
                print()
                config.current_room_id = "fishing_id"
                config.ulric = 2
                return "reload"
        elif containsAny(ans, no):
            print()
            print(""" "Oh, alright. Come back later!" """)
            print("You leave the pier.")
            print()
            config.current_room_id = "southeast_c"
            return "reload"
        else:
            print(""" "Yes or no, son?" """)


c_pier = Room(name="Doran's Pier", des="", id="c_pier", directions="", on_enter=pier_logic)
