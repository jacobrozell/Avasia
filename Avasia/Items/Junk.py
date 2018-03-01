class Junk:
    def __init__(self, name, des, value, id):
        self.type = "junk"
        self.name = name
        self.des = des
        self.value = value
        self.id = id

    def print_value(self):
        print("It's worth " + str(self.value) + " gold!")

    def print_stats(self):
        print(str(self.name) + ": " + str(self.value) + " gold, " + "\n" + str(self.des) + ".")
