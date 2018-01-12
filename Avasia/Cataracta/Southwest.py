from Avasia.Room.Room import *


southwest_c = Room(name="Southwest Cataracta",
                   des="You feel the wind on your face and smell the familiar scent of the Cataractan air."
                       "\nTo the NORTH, a large, ornate bridge leads across the deep and menacing Varatho river to the upper part of the town."
                       "\nTo the WEST, is Althalos' home, a short and stout shopkeeper with a rather unpredictable character."
                       "\nTo the EAST, the housing district continues, parallel to the Varathro River.",
                   id="southwest_c",
                   directions={"E": "southeast_c", "N": "middle_c", "W": "althalos_house"})
