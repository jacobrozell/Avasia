from Avasia.Items.Food import *
from Avasia.Items.Junk import *

# ------------------------Items----------------------------


# ------------------------Food----------------------------

smallfish = Food(name="Small Fish",
                 des="When consumed it restores 5hp.",
                 restored_amount=5,
                 value=5,
                 id="smallfish")

bigfish = Food(name="Big Fish",
               des="When consumed it restores 10hp.",
               restored_amount=10,
               value=10,
               id="bigfish")

potion = Food(name="Potion",
              des="When consumed it restores 10hp.",
              restored_amount=10,
              value=25,
              id="potion")

# ------------------------Junk----------------------------
oldshoe = Junk(name="Old-shoe",
               des="An old shoe covered in mud and seaweed.",
               value=2,
               id="oldshoe")

# ------------------------Artifact Weapon----------------------------


