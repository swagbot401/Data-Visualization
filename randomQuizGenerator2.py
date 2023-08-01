import random as Ran
import os
from pathlib import Path
import shelve

# randomQuizGenerator.py - Creates quizzes with question and answers in
# random order, along with the answer key.

quiz_folder = r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\random_quiz_project2"

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


os.chdir(quiz_folder)

def answer_list(correct_item, all_items):
    item_list = all_items.copy()
    answer_options = [correct_item]
    
    for i in range(3):
        possible_ans = item_list[Ran.randint(0 , len(item_list) - 1)]
        answer_options.append(possible_ans)
        item_list.remove(possible_ans)
    
    Ran.shuffle(answer_options)
    
    return answer_options


state_list = list(capitals.keys())
capital_list = list(capitals.values())



quiz_name_file = "Quiz"
ans_sheet_name_file = "Answer_Sheet"
file_ans_name = "Answer Key for Quiz"
QUIZ_COUNT = 5
answer_table = []

for files in range(QUIZ_COUNT):
    Ran.shuffle(state_list)
    
    quiz_name_file = quiz_name_file + " " + str(files + 1)
    file_gen = open(quiz_name_file, "w")
    file_gen.write(f"Quiz {files + 1} \nWhat are the capitols of each state? \n\n")

    for question in range(len(state_list)):
        cur_question = state_list[question]
        correct_ans = capitals[state_list[question]]
        
        
        file_gen.write(f"{question + 1}. What is the capital of {cur_question}? \n")
        
        answer_choices = answer_list(correct_ans, capital_list)

        for choice_num in range(len(answer_choices)):
            choice_head = "      " + "ABCD"[choice_num]
            file_gen.write(f"{choice_head}.  {answer_choices[choice_num]}\n")
            
        file_gen.write("  -------------------------------------------------\n")
        
        correct_answer_index = answer_choices.index(correct_ans)

        correct_answer_final = "ABCD"[correct_answer_index]

        answer_table.append(f"{str(question + 1)}. {correct_answer_final}")

    
    ans_sheet_name_file = ans_sheet_name_file + " " + str(files + 1)
    ans_gen = open(ans_sheet_name_file, "w")
    
    for entry in range(len(answer_table)):
        ans_gen.write(answer_table[entry] + "\n")

    ans_sheet_name_file = ans_sheet_name_file[0:12]
    answer_table.clear()
    ans_gen.close()

    

    quiz_name_file = quiz_name_file[0:4]
file_gen.close()