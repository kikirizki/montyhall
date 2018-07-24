import numpy as np
import random

wins = 0
loses = 0

def random_dors():
    doors = [1,2,3]
    car = random.choice(doors)
    prizes = ["goat", "goat", "goat"]
    prizes[car-1]="car"
    return prizes

def switching_strategy(person_choice, prizes):
    prizes[person_choice-1] = None
    for i in range(3):
        if prizes[i]=="goat":
            prizes[i]=None
    for prize in prizes:
        if prize == "car":
            return "car"
    return "goat"

def do_quiz(wins, loses):
    prizes = random_dors()
    person_choice = random.choice([1,2,3]) 
    prize = switching_strategy(person_choice, prizes)
    if prize == "car":
        wins = wins + 1
    if prize == "goat":
        loses = loses + 1
    return wins,loses
n_iter = 1000000
for i in range(n_iter):
    wins,loses=do_quiz(wins, loses)
    print("current Losses : {} -  wins : {} | probability of wins : {}".format(loses, wins, wins/float(n_iter)))
