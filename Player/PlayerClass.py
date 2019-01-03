from random import randint
from math import floor
import Logic.config as config


class Player:
    def __init__(self, atk, spd, hp, luck, defense, name, gold, class_id):
        self.name = name

        # Attack
        self.atk = atk
        self.maxAtk = 0

        # Speed
        self.spd = spd
        self.maxSpd = 0
        
        # Hp
        self.hp = hp
        self.maxHp = 0

        # Defense
        self.defense = defense
        self.maxDef = 0

        # Luck
        self.luck = luck
        self.maxLuck = 0

        # Gold
        self.gold = gold
        self.maxGold = 1000

        # Inventory (Inventory associates item with item.typeID) (printInventory is just used for a UI standpoint)
        self.printInventory = {}
        self.inventory = {}
        
        # Class/ Forms
        self.class_id = class_id
        self.hunterId = "hunter"
        self.guardianId = "guardian"
        self.scoutId = "scout"

        # Level
        self.playerLevel = 1

        # Exp
        self.exp = 0
        self.questDialogue = False
        self.smallQuestExp = 15
        self.mediumQuestExp = 50
        self.largeQuestExp = 100

        # LevelUp Points
        self.levels = {2: 100, 3: 500, 4: 1500, 5: 5000, 6: 7500, 7: 10000, 8: 15000}

        # Achievements
        self.trophies = {"startedAdventure": {"name": "Started the Adventure", "value": False},
                         "fished": {"name": "Gone Fishin'", "value": False},
                         "brother": {"name": "Brotherly Love", "value": False}
                         }

        self.trophyCount = 0
        self.maxTrophyCount = len(self.trophies)

    def return_item(self, string):
        for item in self.inventory:
            if string.replace(" ", "").lower() == item.id:
                return item
            else:
                return False

    def give_item(self, item):
        self.inventory[item] = item.typeID

        if item.typeID == "food":
            self.printInventory[item.name] = "Restored Amount = " + str(item.restored_amount)

        elif item.typeID == "junk":
            self.printInventory[item.name] = "Value: " + str(item.value) + "; " + str(item.des)

    def print_player_inventory(self):
        count = 0
        for item in self.printInventory:
            count += 1
            print("Inventory " + str(count) + ": "
                  + str(item.replace("'", "").replace("{}", ""))
                  + ", " + str(self.printInventory[item]))

    def take_hit(self, damage):
        self.hp -= damage

    def eat_food(self, amount):
        self.hp += amount
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def display_stats(self):
        output = ""
        output += str(self.get_name()) + ": Hp: " + str(self.get_hp()) + ", Atk: " + str(
            self.get_atk()) + ", Def: " + str(self.get_def())
        output += ", Class: " + str(self.get_class().title())
        print(output)

    def check_hit(self, player_luck):
        if player_luck == 0 or player_luck == 1:
            return True
        else:
            chance = randint(1, player_luck)
            if chance >= floor(player_luck * .5):
                return True
            else:
                return False

    def reset_stats(self):
        self.atk = self.maxAtk
        self.spd = self.maxSpd
        self.hp = self.maxHp
        self.luck = self.maxLuck
        self.defense = self.maxDef

    def give_combat_exp(self):
        if self.playerLevel <= 3:
            amt = (self.playerLevel * 50)
        else:
            amt = (self.playerLevel * 100)

        self.exp += amt
        print("You gain " + str(amt) + " exp!")
        print("You now have " + str(self.exp) + " exp!")

        # See how much exp is needed for the next level and if we have enough levelUp
        if self.exp >= self.levels[self.playerLevel + 1]:
            self.level_up()

    def give_quest_exp(self, amt):
        if self.questDialogue is False:
            print("\nYou can occasionally get bonus exp from doing hidden or uncommon choices.")
            print("The more uncommon, the more bonus experience.")
            self.questDialogue = True

        self.exp += amt
        print("\nYou gain " + str(amt) + " exp!")
        print("You now have " + str(self.exp) + " exp!")
        if self.exp >= self.levels[self.playerLevel + 1]:
            self.level_up()

    def level_up(self):
        # Conditionals for each class
        self.playerLevel += 1
        print("You leveled up!")
        print("You are now level " + str(self.playerLevel) + "!")
        self.maxAtk += 1
        self.maxDef += 1
        self.maxSpd += 1
        self.maxHp += 1
        self.reset_stats()

    def unlocked_trophy(self, id):
        if id in self.trophies:
            trophyObject = self.trophies[id]
            trophyObject["value"] = True

            print(config.trophy_color, end='')
            print("Trophy unlocked: " + str(trophyObject["name"]) + "!")

            self.trophyCount += 1

            print("\nYou have found " + str(self.trophyCount) + " trophy out of " + str(self.maxTrophyCount) + "!")
            print(config.base_color, end='')

    def print_obtained_trophies(self):
        print(config.trophy_color, end='')
        print("\n---Current Trophies (" + str(self.trophyCount) + "/" + str(self.maxTrophyCount) + ")---")
        for _, value in self.trophies.items():
            if value["value"] is True:
                print(value["name"])
        print(config.base_color, end='')

    # ------Getters and Setters-----
    # Name
    def set_name(self, namein):
        self.name = namein

    def get_name(self):
        return self.name
    
    # Attack
    def set_atk(self, atkin):
        self.atk = atkin

    def get_atk(self):
        return self.atk
    
    def get_max_atk(self):
        return self.maxAtk

    def set_max_atk(self, atkIn):
        self.maxAtk = atkIn

    # Hp
    def set_hp(self, hpin):
        self.hp = hpin

    def get_hp(self):
        return self.hp
    
    def set_max_hp(self, hpIn):
        self.maxHp = hpIn
        
    def get_max_hp(self):
        return self.maxHp

    # Defense
    def set_def(self, defin):
        self.defense = defin

    def get_def(self):
        return self.defense
    
    def set_max_def(self, defIn):
        self.maxDef = defIn
    
    def get_max_def(self):
        return self.maxDef

    # Speed
    def set_speed(self, int):
        self.spd = int

    def get_speed(self):
        return self.spd

    def set_max_speed(self, spdIn):
        self.maxSpd = spdIn
        
    def get_max_speed(self):
        return self.maxSpd
    
    # Luck
    def set_luck(self, luckIn):
        self.luck = luckIn

    def get_luck(self):
        return self.luck

    def get_max_luck(self):
        return self.maxLuck

    def set_max_luck(self, maxLuckIn):
        self.maxLuck = maxLuckIn

    # Gold
    def get_gold(self):
        return self.gold

    def get_max_gold(self):
        return self.maxGold

    def subtract_gold(self, goldIn):
        self.gold -= goldIn
        if self.gold < 0:
            self.gold = 0

    def add_gold(self, goldIn):
        self.gold += goldIn

    def print_gold(self):
        print("You have " + str(self.gold) + " gold.")

    # Exp
    def set_exp(self, expIn):
        self.exp = expIn

    def get_exp(self):
        return self.exp

    # Class
    def set_class(self, string):
        self.class_id = string

    def get_class(self):
        return self.class_id

    # Level
    def get_level(self):
        return self.playerLevel

    def set_level(self, levelIn):
        self.playerLevel = levelIn

    # Get all --Used for save
    def get_all_stats(self):
        return {"name": self.get_name(),
                "class": self.get_class(),
                "gold": self.get_gold(),
                "atk": self.get_atk(),
                "def": self.get_def(),
                "speed": self.get_speed(),
                "luck": self.get_luck(),
                "hp": self.get_hp(),
                "level": self.get_level(),
                "exp": self.get_exp(),
                # "inventory": self.inventory,
                "printInventory": self.printInventory,
                "maxAtk": self.get_max_atk(),
                "maxDef": self.get_max_def(),
                "maxSpeed": self.get_max_speed(),
                "maxLuck": self.get_max_luck(),
                "maxHp": self.get_max_hp(),
                "currentRoom": config.current_room_id,
                "fountain": config.fountain,
                "ulric": config.ulric,
                "doran": config.doran,
                "rustySword": config.varrustysword,
                "brokenAxe": config.varbrokenaxe,
                "courtyard": config.courtyard,
                "returnFish": config.returnfish,
                "portalRoom": config.portalRoom,
                "trophies": self.trophies,
                "trophyCount": self.trophyCount}


