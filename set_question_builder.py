import sys
import card
import set
from threading import Timer
import time

def set_builder():
    'changes text file input into a set of cards in order to work for the program'
    InputFile = input('''Input text file name in format [name].txt, make sure when you export from Quizlet you use | (pipe) as separation char. 
    Ensure that the text file is in the directory within which this program is running. ''')
    card_list = []
    f = open(InputFile, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        question = line.split('|')[0].strip()
        answer = line.split('|')[1].strip()
        tempcard = card(question,answer)
        card_list.append(tempcard)
        return set(card_list, InputFile[:-4])

def intro():
    'intro to the program, takes user input on set selection, number of answers, and questiontime'
    print("Welcome to weighted_quiz, make sure you have plugged in your macropad before you begin")
    imported_set = set_builder()
    answer_num = -1
    while answer_num <= 1:
        answer_num = int(input("Input the amount of possible answers you would like per question"))
    question_time = -1
    while question_time <= 3:
        question_time = int(input("Input the amount of time you would like per question in seconds (min 3secs)"))
    return answer_num, question_time, imported_set

def question_display(answer_num, question_time, imported_set):
    'builds questions based on weighting, takes answer numbers, question time and imported set as args'
    question, correct_ans, ans_list, selected_card = imported_set.question_builder(answer_num)
    print(question)
    time.sleep(question_time/5)
    for i in range(answer_num):
        print(str(i+1)+'.', ans_list[i])
    t = Timer(question_time, print, ['Sorry, times up!'])
    t.start()
    start_time = time.time()
    guess = int(input("Input answer position number")-1)
    answer = ans_list[guess]
    time_elapsed = time.time() - start_time
    t.cancel()
    if answer == correct_ans:
        selected_card.updateWeight(question_time, time_elapsed, True)
    else:
        selected_card.updateWeight(question_time, time_elapsed)

