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

