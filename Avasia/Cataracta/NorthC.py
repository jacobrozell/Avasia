from Avasia.Room.Room import *


north_c = Room(name="Northern Cataracta",
               des="To the NORTH is the Northern Gate."
                   "\nTo the EAST is the Cataractan Legion courtyard, where you will begin your training."
                   "\nTo the WEST is the closed upper trading district." #we should find a use for this.
                   "\nTo the SOUTH is middle Cataracta.",
               id="north_c",
               directions={"S": "middle_c", "N": "nGate", "W": "west_cataracta", "E": "courtyard"})



