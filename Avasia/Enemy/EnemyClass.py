class Enemy:
    def __init__(self, atk, defense, spd, hp, name):
        self.atk = atk
        self.defense = defense
        self.spd = spd
        self.hp = hp
        self.name = name

    def take_hit(self, damage):
        self.hp -= damage
        if self.defense > 0:
            self.hp += self.defense

    def display_stats(self):
        output = ""
        output += str(self.name) + ": HP: " + str(self.hp) + ", Atk: " + str(self.atk) + ", Def: " + str(self.defense)
        print(output)

    def setStats(self, nameIn, atkIn, defIn, hpIn, spdIn):
        self.name = nameIn
        self.atk = atkIn
        self.defense = defIn
        self.hp = hpIn
        self.spd = spdIn

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