from random import randint


class Weapon:
    def __init__(self, name, des, value, atk, spd):
        self.name = name
        self.des = des
        self.value = value
        self.atk = atk
        self.spd = spd
        self.type = "equipable"
        self.self = "weapon"

    def print_value(self):
        print("It's worth " + str(self.value) + " gold!")

    def print_stats(self):
        print(self.name + ": attack = " + str(self.atk) + ", speed = "
            + str(self.spd) + ", value = " + str(self.value) + ".")
        print(self.name + ": " + self.des)

