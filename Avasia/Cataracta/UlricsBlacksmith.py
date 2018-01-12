from Avasia.Room.Room import *
import Avasia.Logic.config as config


def ulric_logic():
    if config.ulric == 0:
        print()
        print(">>>Ulric's House<<<")
        print()
        print()
        print(
            "You go south to Ulric's Blacksmith, a small building, with clutters of metal and materials everywhere.")
        print("You approach Ulric, who is sitting on the steps of his house.")
        print("He begins talking to you.")
        print()
        print(""""So, you've decided to join the Cataractan army? More business for me I suppose, heh." """
              "\n"
              """\n"Tell you what, go see my brother Doran at the pier." """
              """\n"As you know, he rents out fishing poles." """
              "\n"
              """\n"I bet you can find some pretty interesting stuff out there." """
              """\n"I would love to be able to fish all day..." """
              """\n"but there is always work to be done." """
              """\n"Not that the work ever bothered me too bad. """
              "\n"
              """\n"Now go bother my brother Doran at the pier." """
              "\n")
        config.ulric = 1
        return "go back"
    else:
        print()
        print(""" "Go see my brother. I need to back to work." """)
        print()
        return "go back"

ulric_house = Room(name="", des="", id="ulric_house", directions="", on_enter=ulric_logic)


