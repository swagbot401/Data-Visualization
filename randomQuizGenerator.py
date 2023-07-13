import random as Ran
import os
from pathlib import Path

# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
# The quiz data. Keys are states and values are their capitals.

quiz_folder = r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\random_quiz_project"


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# test_dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(test_dict)

# list_items = list(test_dict.keys())




# TODO: Create the quiz and answer key files.
"""
1 - Change dir to a folder (Done)
2 - Get a list of the keys
3 - Shuffle the list 
4 - Create a new quiz file 
5 - Ask question Traverse through shuffled list and ask question 
6 - Create a temp right answer location (0-3)
7 - 

"""



os.chdir(quiz_folder)
state_list = list(capitals.keys())

file_quiz_name = "Quiz"
file_ans_name = "Answer Key for Quiz"



for i in range(49):
    Ran.shuffle(state_list)
    file_quiz_name = file_quiz_name + " " + str(i)
    file_ans_name = file_ans_name + " " + str(i)

    right_ans_pos = Ran.randint(0, 3)
    
    file_gen = open(file_quiz_name, "w")
    file_gen.write(f"{file_quiz_name} \n\nAnswer the capitals for each state\n\n")

    for question in range(len(state_list)):
      cur_question = state_list[question]
      correct_ans = capitals[state_list[question]]
      question_num = question + 1
      print(f"What is the capital of {cur_question}")
      
      file_gen.write(f"{question_num}. What is the capital of {cur_question}\n")
      
      for pos in range(4):
        if pos == 0:
          file_gen.write("  A. ")
          if pos == right_ans_pos:
            file_gen.write(f" {correct_ans}\n")
          else:
            file_gen.write(f" {capitals[state_list[Ran.randint(0,49)]]}\n")

        elif pos == 1:
          file_gen.write("  B. ")
          if pos == right_ans_pos:
            file_gen.write(f" {correct_ans}\n")
          else:
            file_gen.write(f" {capitals[state_list[Ran.randint(0,49)]]}\n")
          
        elif pos == 2:
          file_gen.write("  C. ")
          if pos == right_ans_pos:
            file_gen.write(f" {correct_ans}\n")
          else:
            file_gen.write(f" {capitals[state_list[Ran.randint(0,49)]]}\n")
        
        elif pos == 3:
          file_gen.write("  D. ")
          if pos == right_ans_pos:
            file_gen.write(f" {correct_ans}\n\n")
          else:
            file_gen.write(f" {capitals[state_list[Ran.randint(0,49)]]}\n\n")
    file_gen.close()

    file_ans_key = open(file_ans_name, "w")
    file_ans_key.write(f"\n\nAnswers for {file_ans_name}\n\n")
    
    for answers in range(len(state_list)):
      cur_question = state_list[answers]
      answers_num = answers + 1
      correct_ans = capitals[state_list[answers]]

      file_ans_key.write(f"{answers_num}. Answer to What is the capital of {cur_question} is: {correct_ans} \n")

    file_ans_key.close()

    file_ans_name = "Answer Key for Quiz"
    file_quiz_name = "Quiz"
    
