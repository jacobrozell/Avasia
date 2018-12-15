from Room.Room import Room


middle_c = Room(name="Middle Cataracta",
                des="To the NORTH lies Northern Cataracta."
                    "\nTo the EAST the stone path enters into the Castle Gardens."
                    "\nTo the WEST is the closed lower trading district."
                    "\nTo the SOUTH is the bridge which leads to SouthWest Cataracta.",
                id="middle_c",
                directions={"S": "southwest_c", "W": "west_cataracta", "E": "c_fountain", "N": "north_c"})

