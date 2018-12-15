from Logic.util import containsAny
from Logic.Item_Storage import *


def shop(player):

    # Inventory is wrong
    print()
    print("Welcome to my shop!")
    sell = ["SELL"]
    buy = ["BUY"]
    ans = input("Are you here to sell or buy?")
    if containsAny(ans, sell):
        print("What do you want to sell?")
        if player.inventory == {}:
            print("You have nothing to sell.")
            # if item in inventory... Add value to gold_count... Del item from player.inventory
    if containsAny(ans, buy):
        rustysword.roll_for_stats_common()
        availible_items = {rustysword.name: 10}
        print()
        print("Here is what I have to sell: " + str(availible_items))
        purchase = input("What do you want to purchase?")
        strrustysword = ["RUSTY SWORD"]
        if containsAny(purchase, strrustysword):
            if player.inventory == rustysword.name:
                print("You already have that item!")
                print()
            elif player. < 10:
                print()
                print("You don't have enough money!")
                print()
            else:
                player.give_item(rustysword)
                print()
                print("You purchased " + str(rustysword.name) + "!")
                player.printplayerinventory()
                player_gold.value -= 10
                return
    else:
        print()