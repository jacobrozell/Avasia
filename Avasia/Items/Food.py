class Food:
    def __init__(self, name, des, restored_ammount, value):
        self.name = name
        self.des = des
        self.restored_ammount = restored_ammount
        self.value = value
        self.type = "edible"

    def print_stats(self):
        print(str(self.name) + ": " + str(self.value) + " gold, " + "\n" + str(self.des))
