import sys, math, random, time
import pyinputplus as pyip


# Multiplication Quiz project
'''
- Ask user 10 multiplication questions
- Keep track of number of correct answers
- 
'''
question_count = 5
correct_count = 0
question_max_time = 10

for question in range(question_count):
    rand_val1 = random.randint(0, 10)
    rand_val2 = random.randint(0, 10)
    correct_answer = rand_val1 * rand_val2
    
    try:
        user_ans = pyip.inputInt(prompt= f"What is {rand_val1} x  {rand_val2}?  ", timeout= question_max_time)
        if user_ans == correct_answer:
            correct_count += 1
            print("Correct!")
        else:
            print("Incorrect!")
    
    except pyip.TimeoutException:
        print(f"Time is up! You have {question_max_time} seconds to answer each question")
    
    
if correct_count > (question_count / 2 + 1):
    print(f"You did great! You got {correct_count} questions correct.")
else: 
    print(f"You could do better. You got {correct_count} questions correct")
    







