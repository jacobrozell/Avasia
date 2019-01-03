from Room.Room import Room

southeast_c = Room(name="Southeast Cataracta",
                   des="To the NORTH, a pier stretches out over the river."
                       "\nTo the WEST is the western housing district."
                       "\nTo the EAST is a winding path that leads outside the city, with a sign that says: Hunters Only."
                       "\nTo the SOUTH is Ulric's home, the local blacksmith.",
                   id="southeast_c",
                   directions={"N": "c_pier", "E": "hunter_path", "W": "southwest_c", "S": "ulrics_blacksmith"})