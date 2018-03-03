
class Player:
    def __init__(self, atk, spd, hp, defense, name, class_id):
        self.name = name
        self.atk = atk
        self.spd = spd
        self.hp = hp
        self.defense = defense
        self.maxhp = hp
        self.printinventory = {}
        self.inventory = {}
        self.class_id = class_id
        self.attacks = []
        self.equipped_weapon = {}

    def return_item(self, string):
        for item in self.inventory:
            if string.replace(" ", "").lower() == item.id:
                return item
            else:
                return "false"

    def give_item(self, item):

        self.inventory[item] = item.id

        if item.type == "edible":
            self.printinventory[item.name] = "Restored Amount = " + str(item.restored_amount)

        elif item.type == "junk":
            self.printinventory[item.name] = "Value: " + str(item.value) + "; " + str(item.des)

    def printplayerinventory(self):
        print("Inventory: " + str(self.printinventory).replace("'", "").replace("{}", ""))

    def take_hit(self, damage):
        self.hp -= damage

    def add_attack(self, attack):
        if len(self.attacks) >= 4:
            print("You can only have 4 attacks!")
        else:
            self.attacks.append(attack.upper())

    def choose_attack(self, attack):
        if attack in self.attacks:
            attack()
        else:
            print("You don't have that attack!")
            return False

    def eat_food(self, ammount):
        self.hp += ammount
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def display_stats(self):
        output = ""
        output += str(self.getName()) + ": Hp: " + str(self.getHp()) + ", Atk: " + str(
            self.getAtk()) + ", Def: " + str(self.getDef())
        output += ", Class: " + str(self.getClass().title())
        print(output)

    # Getters and Setters

    def setAtk(self, atkin):
        self.atk = atkin

    def getAtk(self):
        return self.atk

    def setName(self, namein):
        self.name = namein

    def getName(self):
        return self.name

    def setHp(self, hpin):
        self.hp = hpin
        self.maxhp = hpin

    def getHp(self):
        return self.hp

    def setDef(self, defin):
        self.defense = defin

    def getDef(self):
        return self.defense

    def setSpeed(self, int):
        self.spd = int

    def getSpeed(self):
        return self.spd

    def setClass(self, string):
        self.class_id = string

    def getClass(self):
        return self.class_id
