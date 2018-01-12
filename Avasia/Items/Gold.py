class Gold:
    def __init__(self, des, name, value):
        self.des = des
        self.name = name
        self.value = value
        self.type = "currency"

    def gold_count(self):
        print("You have " + str(self.value) + " gold.")

    def add_gold(self, ammount_to_add):
        self.value += ammount_to_add

    def subtract_gold(self, amt_to_sub):
        self.value -= amt_to_sub

