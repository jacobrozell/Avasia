import Logic.config as config


class Enemy:
    def __init__(self, atk, defense, speed, hp, name):

        # Name
        self.name = name

        # Attack
        self.atk = atk
        self.maxAtk = atk

        # Speed
        self.speed = speed
        self.maxSpeed = speed

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

    def did_appear(self):
        print("A" + str(self.name) + " appeared!\n")

    def display_stats(self):
        output = ""
        output += str(self.name) + ": HP: " + str(self.hp) + ", Atk: " + str(self.atk) + ", Def: " + str(self.defense)
        print(output)

    def set_stats(self, name, atk, defense, hp, speed, text=""):

        # Name
        self.name = name

        # Attack
        self.atk = atk
        self.maxAtk = atk

        # Speed
        self.speed = speed
        self.maxSpeed = speed

        # Hp
        self.hp = hp
        self.maxHp = hp

        # Defense
        self.defense = defense
        self.maxDef = defense

        # Kill player text
        self.text = text

    def kill_player(self):
        print(config.die_color, self.text + "\nYou have died.\n")
        print(config.base_color)

    # Getters and Setters
    # Name
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # Attack
    def set_atk(self, atk):
        self.atk = atk

    def get_atk(self):
        return self.atk

    def get_max_atk(self):
        return self.maxAtk

    def set_max_atk(self, atk):
        self.maxAtk = atk

    # Hp
    def set_hp(self, hpin):
        self.hp = hpin
        self.maxHp = hpin

    def get_hp(self):
        return self.hp

    def set_max_hp(self, hp):
        self.maxHp = hp

    def get_max_hp(self):
        return self.maxHp

    # Defense
    def set_def(self, defense):
        self.defense = defense

    def get_def(self):
        return self.defense

    def set_max_def(self, defense):
        self.maxDef = defense

    def get_max_def(self):
        return self.maxDef

    # Speed
    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_max_speed(self, speed):
        self.maxSpeed = speed

    def get_max_speed(self):
        return self.maxSpeed

    def set_text(self, text):
        self.text = text
