from Avasia.Room.Room import Room


west_hallway = Room(name="West Castle Hallway",
                    des="To the NORTH is the Nacastrum Library."
                        "To the EAST is a grand luxurious door that is encrusted in jewels."
                        "To the WEST is the Cataractan portal room.",
                    id="west_hallway",
                    directions={"N": "n_library", "E": "throne_room", "W": "c_portal_room"})



