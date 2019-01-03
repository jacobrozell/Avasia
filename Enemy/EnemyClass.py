import Logic.config as config


class Enemy:
    def __init__(self, atk, defense, spd, hp, name):

        self.name = name

        # Attack
        self.atk = atk
        self.maxAtk = atk

        # Speed
        self.spd = spd
        self.maxSpd = spd

        # Hp
        self.hp = hp
        self.maxHp = hp

        # Defense
        self.defense = defense
        self.maxDef = defense

        # Kill player text
        self.text = ""

    def take_hit(self, damage):
        self.hp -= damage

    def display_stats(self):
        output = ""
        output += str(self.name) + ": HP: " + str(self.hp) + ", Atk: " + str(self.atk) + ", Def: " + str(self.defense)
        print(output)

    def setStats(self, nameIn, atkIn, defIn, hpIn, spdIn, text=""):

        self.name = nameIn

        # Attack
        self.atk = atkIn
        self.maxAtk = atkIn

        # Speed
        self.spd = spdIn
        self.maxSpd = spdIn

        # Hp
        self.hp = hpIn
        self.maxHp = hpIn

        # Defense
        self.defense = defIn
        self.maxDef = defIn

        # Kill player text
        self.text = text

    def killPlayer(self):
        print(config.die_color, self.text + "\nYou have died.\n")
        print(config.base_color)

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
        self.maxHp = hpin

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

    def setText(self, text):
        self.text = text