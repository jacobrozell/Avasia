class Food:
    def __init__(self, name, des, restored_amount, value, id):
        self.name = name
        self.des = des
        self.restored_amount = restored_amount
        self.value = value
        self.type = "edible"
        self.id = id

    def getAmt(self):
        return self.restored_amount

    def print_stats(self):
        print(str(self.name) + ": " + str(self.value) + " gold, " + "\n" + str(self.des) + ".")