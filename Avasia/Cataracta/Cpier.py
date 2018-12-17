from Room.Room import Room
from Logic.util import talk, containsAny
import Logic.config as config


def pier_logic():
    c_pier.print_name()
    print("You enter the fishing hut posted along side the Varatho river.")
    print("The hut reeks of fish and bait.")
    print("Various fishing poles line the walls in all shapes, sizes, and colors.")
    print()

    if config.doran == 0:
        print("Doran, who appears to be the owner, hears you enter and calls from a back room with a rough, agitated voice.")
        talk("Oi! Whatya be doin' in my hut?")
        print()
        print("You explain that you saw the pier and wanted to take a closer look.")
        print()
        talk("Hmm.. Doran hums before responding. I don't allow many people to come visit.")
        talk("To many of these landfolk don't have any appreciation for the river or my pier.")
        talk("Perhaps for a few gold, you can take a look. Think of it as insurance.")
        talk("I'll even let you borrow a fishing rod and some bait.")
        config.doran = 1
    elif config.doran == 1:
        talk("Welcome back! You here to fish or just stand there?")
    while True:
        talk("What do ye say? 15 gold?")
        ans = input()
        print()
        ans.upper()
        yes = ["YES"]
        no = ["NO", "LEAVE"]
        if containsAny(ans, yes):
            if config.ulric == 0:
                print("You pay Doran 15 gold.")
                config.player_gold.subtract_gold(15)
                config.player_gold.gold_count()
                print("He hands you an old fishing rod and some bait then points toward the door to the pier.")
                print()
                talk("Becareful not to fall in the river.")
                talk("Varatho ain't a kind beast to those who swim her rapids.")
                config.current_room_id = "fishing_id"
                return "reload"
            if config.ulric == 1:
                print("You explain to Doran that his brother, Ulric, sent you.")
                print()
                talk("Ay', you spoke to Ulric, did ye?")
                talk("He's always leading people over here to 'help the business out', as he puts it.")
                talk("I think he sends 'em here so he isn't bothered.")
                talk("I'm sure he told you that I'd let you borrow a fishing pole to fish for a bit.")
                talk("Fine, here. Go ahead. Just make sure you're kind to the river and don't ruin my pier!")
                print()
                print("Doran hands you an old fishing rod and some bait then points you towards the door to the pier.")
                print()
                config.current_room_id = "fishing_id"
                config.ulric = 0
                return "reload"
        elif containsAny(ans, no):
            print()
            talk("Then what're you doin' standin' around here for?")
            talk("You change your mind, you come see me.")
            print()
            print("You leave the pier.")
            print()
            config.current_room_id = "southeast_c"
            return "reload"
        else:
            print("I don't understand")


c_pier = Room(name="Doran's Pier", des="", id="c_pier", directions="", on_enter=pier_logic)
