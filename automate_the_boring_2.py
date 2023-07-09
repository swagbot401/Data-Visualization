import math, sys
import time
import random
import pyperclip 

#Guessing number game

print("This is a guessing game. How lucky will you be?")

#Input from user: Max number, guesses
try_count = 1
MAX_TRY_COUNT = 5

while True: 
    max_range = input ("Please Enter a real number. Try 10:    ")
    try: 
        max_range_int = int(max_range)
        break

    except ValueError:
        print("Please Enter a real number. Try 10")

correct_answer = random.randrange(0, int(max_range), 1)

print(f"Try to get a number between 0 and {max_range_int} \n")

while try_count <= MAX_TRY_COUNT: 
    guess_input = int(input("What is your guess?  "))
    
    if isinstance(guess_input, int) == False:
        print("Please input a real number")
    
    elif guess_input == correct_answer: 
        print(f"You Won! You won with only using {try_count} try")
        break
    
    elif (guess_input != correct_answer) and (guess_input > correct_answer):
        print(f"Wrong! The correct answer is lower. You have {MAX_TRY_COUNT - try_count} tries left")
        try_count = try_count + 1

    elif (guess_input != correct_answer) and (guess_input < correct_answer):
        print(f"Wrong! The correct answer is higher. You have {MAX_TRY_COUNT - try_count} tries left")
        try_count = try_count + 1
    
    if try_count > MAX_TRY_COUNT: 
        print(f"\n---------------- You LOSE! The correct answer was {correct_answer} ----------------")



