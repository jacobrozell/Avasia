from Avasia.Room.Room import *


middle_c = Room(name="Middle Cataracta",
                des="To the NORTH lies the castle and the North Gate."
                    "\nTo the EAST the stone path enters into the Castle Gardens."
                    "\nTo the WEST is the closed lower trading district."
                    "\nTo the SOUTH is the bridge.",
                id="middle_c",
                directions={"S": "southwest_c", "W": "west_cataracta", "E": "c_fountain", "N": "north_c"})

