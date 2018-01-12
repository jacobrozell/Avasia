from Avasia.Items.Food import *
from Avasia.Items.Weapon import *
from Avasia.Items.Junk import *

# ------------------------Items----------------------------


# ------------------------Food----------------------------
smallfish = Food(name="Small Fish",
                 des="When consumed it restores 5hp.",
                 restored_ammount=5,
                 value=5)

bigfish = Food(name="Big Fish",
               des="When consumed it restores 10hp.",
               restored_ammount=10,
               value=10)

all_food_list = []
all_food_list.append(smallfish)
all_food_list.append(bigfish)
# ------------------------Junk----------------------------
oldshoe = Junk(name="Old-shoe",
               des="An old shoe covered in mud and seaweed.",
               value=2)

all_junk_list = []
all_junk_list.append(oldshoe)
# ------------------------Weapons----------------------------

# Common

rustysword = Weapon(name="Rusty Sword",
                    des="A rusty sword, worn from the river.",
                    value=10,
                    atk=randint(3, 4),
                    spd=randint(4, 5))

brokenaxe = Weapon(name="Broken Axe",
                   des="An axe broken by the currents of the river.",
                   value=10,
                   atk=randint(5, 6),
                   spd=randint(2, 3))
common_weapon_list = []
common_weapon_list.append(rustysword)
common_weapon_list.append(brokenaxe)

# Rare

rare_weapon_list = []

# Mythic

mythic_weapon_list = []
