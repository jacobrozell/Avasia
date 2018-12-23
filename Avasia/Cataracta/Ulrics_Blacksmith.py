from Room.Room import Room
import Logic.config as config
from Logic.util import talk


def ulric_logic():
    if config.ulric is False:
        ulric_house.print_name()
        print(
            "You go south to Ulric's Blacksmith, a small building, with clutters of metal and materials everywhere.")
        print("You approach Ulric, who is sitting on the steps of his house.")
        print("He begins talking to you.")
        print()
        talk("So, you've decided to join the Cataractan army? More business for me I suppose, heh.")
        talk("Tell you what, go see my brother Doran at the pier.")
        talk("As you know, he rents out fishing poles.")
        talk("I bet you can find some pretty interesting stuff out there.", "\n")
        talk("What I wouldn't give to be able to fish all day.")
        talk("But, there is always work to be done.")
        talk("Not that the work ever bothered me.")
        talk("Now go bother my brother Doran at the pier.", "\n")
        if config.doran is False:
            config.ulric = True
        return "go back"
    else:
        ulric_house.print_name()
        talk("Go bother my brother. I need to get back to work.")
        print()
        return "go back"


ulric_house = Room(name="Ulric's House", des="", id="ulric_house", directions="", on_enter=ulric_logic)


