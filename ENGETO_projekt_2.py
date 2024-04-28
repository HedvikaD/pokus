"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Hedvika Drechslerová
email: hedvika.drechsler@seznam.cz
discord: hedvika_62633
"""

import random
import time

cara = 20 * "-"

print("Hi there!")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print (cara)


number = '0123456789'
number = random.sample(number, 4)   
if number [0] == '0':
    number = random.sample(number, 4)         
number = ''.join(number)  
print("The number has been generated. Let's play!")

time_start = time.time()
attempts = 0

while True:
    bulls = 0
    cows = 0
    attempts += 1
    guess = input("Enter a number: ")
    print(cara)
     
    
    if len(guess) != 4:
        print("The number must have 4 digits.")
        continue
    if guess[0] == "0":
        print("The number must not start with 0.")
        continue
    if len(set(guess)) != 4:
        print("The number must not contain duplicates.")
        continue
    if not guess.isnumeric():
        print("The number must contain only digits.")
        continue

    for i in range(4):
        if guess[i] == number[i]:
            bulls += 1            
        elif guess[i] in number:
            cows += 1
            

    if bulls == 4:
        time_end = time.time()
        time_total = round(time_end - time_start)
        print(f"Correct, you've guessed the right number in {attempts} guesses.")
        if attempts <= 4:
            print(f"Your score is: {attempts} attempts, your time is: {time_total} seconds - Excellent!")
        elif attempts <= 8:
            print(f"Your score is: {attempts} attempts, your time is: {time_total} seconds- Very good!")
        else:
            print(f"Your score is: {attempts} attempts, your time is: {time_total} seconds - Not so good!")
        print(cara)
        break 
        
    else:
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")             
       

