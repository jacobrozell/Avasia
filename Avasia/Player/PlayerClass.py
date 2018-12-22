from random import randint
from math import floor


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
        self.forms = []

        # Level
        self.player_level = 1

        # Exp
        self.exp = 0

        # LevelUp Points
        self.levels = {2: 100, 3: 500, 4: 1500, 5: 5000, 6: 7500, 7: 10000, 8: 15000}

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

    def printPlayerInventory(self):
        print("Inventory: ")
        for item in self.printInventory:
            print(str(item.replace("'", "").replace("{}", "")))

    def take_hit(self, damage):
        self.hp -= damage

    def eat_food(self, amount):
        self.hp += amount
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def display_stats(self):
        output = ""
        output += str(self.getName()) + ": Hp: " + str(self.getHp()) + ", Atk: " + str(
            self.getAtk()) + ", Def: " + str(self.getDef())
        output += ", Class: " + str(self.getClass().title())
        print(output)

    def addForm(self, formString):
        self.forms.append(formString)

    def searchForm(self, formString):
        for i in self.forms:
            if i.lower() == formString:
                return True
        return False

    def printForms(self):
        print("Known Forms: " + str(self.forms).replace("'", "").replace("[", "").replace("]", ""))

    def checkHit(self, player_luck):
        if player_luck == 0 or player_luck == 1:
            return True
        else:
            chance = randint(1, player_luck)
            if chance >= floor(player_luck * .5):
                return True
            else:
                return False

    def resetStats(self):
        self.atk = self.maxAtk
        self.spd = self.maxSpd
        self.hp = self.maxHp
        self.luck = self.maxLuck
        self.defense = self.maxDef

    def combatExp(self):
        if self.player_level <= 3:
            amt = (self.player_level * 50)
        else:
            amt = (self.player_level * 100)

        self.exp += amt
        print("You gain " + str(amt) + " exp!")
        print("You now have " + str(self.exp) + " exp!")

        # See how much exp is needed for the next level and if we have enough levelUp
        if self.exp >= self.levels[self.player_level + 1]:
            self.levelUp()

    def questExp(self, amt):
        self.exp += amt
        print("You gain " + str(amt) + " exp!")
        if self.exp >= self.levels[self.player_level + 1]:
            self.levelUp()

    def levelUp(self):
        # Conditionals for each class
        self.player_level += 1
        print("You leveled up!")
        print("You are now level " + str(self.player_level) + "!")
        if self.class_id == "scout":
            self.scout_levelUp()

        elif self.class_id == "hunter":
            self.hunter_levelUp()

        else:
            self.guardian_levelUp()

    def scout_levelUp(self):
        if self.player_level == 2 or self.player_level == 3:
            self.maxAtk += 5
            self.maxDef += 3
            self.maxSpd += 5
            self.maxHp += 10
            # self.maxLuck -= 1

        elif self.player_level == 4 or self.player_level == 5:
            self.maxAtk += 10
            self.maxDef += 4
            self.maxSpd += 8
            self.maxHp += 10
        self.resetStats()

    def hunter_levelUp(self):
        if self.player_level == 2 or self.player_level == 3:
            self.maxAtk += 8
            self.maxDef += 3
            self.maxSpd += 2
            self.maxHp += 5
            self.maxLuck -= 1
        elif self.player_level == 4:
            self.maxAtk += 10
            self.maxDef += 4
            self.maxSpd += 3
            self.maxHp += 10
            self.maxLuck -= 2
        elif self.player_level == 5:
            self.maxAtk += 10
            self.maxDef += 5
            self.maxSpd += 4
            self.maxHp += 15
            self.maxLuck -= 2
        self.resetStats()

    def guardian_levelUp(self):
        if self.player_level == 2 or self.player_level == 3:
            self.maxAtk += 5
            self.maxDef += 3
            self.maxSpd += 3
            self.maxHp += 10
            self.maxLuck -= 1

        elif self.player_level == 4:
            self.maxAtk += 8
            self.maxDef += 4
            self.maxSpd += 4
            self.maxHp += 10
            self.maxLuck -= 2

        elif self.player_level == 5:
            self.maxAtk += 10
            self.maxDef += 5
            self.maxSpd += 5
            self.maxHp += 15
            self.maxLuck -= 2

        self.resetStats()

    # Getters and Setters
    
    # Name
    def setName(self, namein):
        self.name = namein

    def getName(self):
        return self.name
    
    # Attack
    def setAtk(self, atkin):
        self.atk = atkin

    def getAtk(self):
        return self.atk
    
    def getMaxAtk(self):
        return self.maxAtk

    def setMaxAtk(self, atkIn):
        self.maxAtk = atkIn

    # Hp
    def setHp(self, hpin):
        self.hp = hpin

    def getHp(self):
        return self.hp
    
    def setMaxHp(self, hpIn):
        self.maxHp = hpIn
        
    def getMaxHp(self):
        return self.maxHp

    # Defense
    def setDef(self, defin):
        self.defense = defin

    def getDef(self):
        return self.defense
    
    def setMaxDef(self, defIn):
        self.maxDef = defIn
    
    def getMaxDef(self):
        return self.maxDef

    # Speed
    def setSpeed(self, int):
        self.spd = int

    def getSpeed(self):
        return self.spd

    def setMaxSpeed(self, spdIn):
        self.maxSpd = spdIn
        
    def getMaxSpeed(self):
        return self.maxSpd
    
    # Luck
    def setLuck(self, luckIn):
        self.luck = luckIn

    def getLuck(self):
        return self.luck

    def getMaxLuck(self):
        return self.maxLuck

    def setMaxLuck(self, maxLuckIn):
        self.maxLuck = maxLuckIn

    # Gold

    def getGold(self):
        return self.gold

    def getMaxGold(self):
        return self.maxGold

    def subtractGold(self, goldIn):
        self.gold -= goldIn
        if self.gold < 0:
            self.gold = 0

    def addGold(self, goldIn):
        self.gold += goldIn

    def printGold(self):
        print("You have " + str(self.gold) + " gold.")

    # Exp
    def setExp(self, expIn):
        self.exp = expIn

    def getExp(self):
        return self.exp

    # Class
    def setClass(self, string):
        self.class_id = string

    def getClass(self):
        return self.class_id
