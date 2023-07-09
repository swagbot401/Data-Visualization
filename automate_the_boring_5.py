import math, sys, random
import automate_the_boring_4
import pyinputplus 


print("Hello. This should run code from a different file")

items_test = {"Rope": 3, "Potions": 45, "Ice_Blast": 8}

ans = automate_the_boring_4.print_inventory(items_test)



name = pyinputplus.inputStr("Please enter your name? ")
print(f"Your name is {name}")

users = ["user1", "user2", "user3", "user4"]
# game_choice = pyinputplus.inputChoice(users, "Please pick a choice:  ", caseSensitive=False)
users[0] = users[0].capitalize()
user_choice = pyinputplus.inputMenu(users, prompt= "Choose one: \n", caseSensitive= False, )
print(type(user_choice))

name = "chris"
print(f"Name is {name.capitalize()}")
print(f"You have choose {user_choice}")
# help(pyinputplus.parameters)