

class Player:
    def __init__(self, atk, spd, hp, defense, name, class_id):
        self.name = name
        self.atk = atk
        self.spd = spd
        self.hp = hp
        self.defense = defense
        self.maxhp = hp
        self.inventory = {}
        self.class_id = class_id
        self.attacks = []
        self.equipped_weapon = {}

    def give_item(self, item):
        if item.type == "equipable":
            self.inventory[item.name] = "Attack:" + str(item.atk) + " Speed:" + str(item.spd)

        elif item.type == "edible":
            self.inventory[item.name] = "Restored Amount:" + str(item.restored_ammount) + "; " + str(item.des)

        elif item.type == "junk":
            self.inventory[item.name] = "Value:" + str(item.value) + "; " + str(item.des)

    def printplayerinventory(self):
        print(str(self.inventory))

    def take_hit(self, damage):
        self.hp -= damage
        if self.defense > 0:
            self.hp += self.defense

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

    def equip_weapon(self, weapon):
        if weapon in self.inventory:
            self.atk += weapon.atk
            print("You equipped " + str(weapon) + "!")
        else:
            print("You don't have that item.")
            if len(self.equipped_weapon) > 0:
                print("You have " + str(self.equipped_weapon) + " equipped!")
            else:
                print("You have no weapon equipped.")

    def unequip_weapon(self, weapon):
        if weapon in self.equipped_weapon:
            self.atk -= weapon.atk
            self.equipped_weapon.pop(weapon)
        else:
            print("That weapon isn't equipped!")
            print("You have " + str(self.equipped_weapon) + " equipped!")

    def eat_food(self, ammount):
        self.hp += ammount
        if self.hp > self.maxhp:
            self.hp = self.maxhp

