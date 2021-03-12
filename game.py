# Python Text RPG
# Harrison Toppen-Ryan

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player setup #####
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
myPlayer = player()

##### Title screen #####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('        -- Play --          ')
    print('        -- Help --          ')
    print('        -- Quit --          ')
    print('--Copyright 2021 htoppen-ryan.me--')
    title_screen_selections()

def help_menu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('-- Use the keys "a", "b", and "c" to select options --')
    print('-- Type your commands to do them --')
    print('-- Use your best judgement when making choices--')
    print('-- Good luck and have fun!--')
    title_screen_selections()


"""
a1 a2...
---------
| | | | | a4
---------
| | | | | b4 ...
---------
| | | | | 
---------
"""

"""
NAME = ''
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False 
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
'b1': False, 'b2': False, 'b3': False, 'b4': False,
'c1': False, 'c2': False, 'c3': False, 'c4': False,
'c1': False, 'c2': False, 'c3': False, 'c4': False,
}

zonemap = {
    'a1': {
        ZONENAME: 'Town Market',
        DESCRIPTION: 'description',
        EXAMINATION:  'examime',
        SOLVED: False,
        UP:  '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2', 
    },
    'a2': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'description',
        EXAMINATION: 'examime',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3', 
    },
    'a3': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'description',
        EXAMINATION: 'examime',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',    
    },
    'a4': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: 'description',
        EXAMINATION: 'examime',
        SOLVED: False, 
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',  
    },
    'b1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examime',
        SOLVED: False, 
        UP: '',
        DOWN: 'a1',
        LEFT: 'c1',
        RIGHT: '',    
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'description',
        EXAMINATION: 'examime',
        SOLVED: False, 
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',    
    },

}
"""

###### Game Interactivity ######
"""
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))
"""

def printFast(i):
    for char in i:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def prompt():
    print("\n" + "===========================")
    statement1 = "You suddenly wake up in a on a labatory table.\n"
    printFast(statement1)
    statement2 = "You have no memories and no idea what is happening.\n"
    printFast(statement2)
    statement3 = "You notice a man wearing a white lab coat in the corner of the room shrieking at the site of you, horrified at what he has created.\n"
    printFast(statement3)
    statement4 = "As he flees in the next room and slams the door behind him, you notice that besides the door there is only that and a single window that leads to an unknown fate.\n"
    printFast(statement4)
    statement5 = ("What would you like to do?\n")
    printFast(statement5)
    print("a. try the enter the door\n")
    print("b. flee out the window\n")
    print("c. do nothing\n")
    action = input("> ")
    accepatble_actions = ['a', 'b', 'c']
    while action.lower() not in accepatble_actions:
        print("Unknown action, try again.\n")
        action = input("> ") 
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in accepatble_actions:
        player_move(action.lower())
        
    

def player_move(myAction):

    if myAction == 'a':
        statement1 = "You thump over to the door, trying to open it\n"
        printFast(statement1)
        statement2 = "After entering you see the scientist on his bed, trying to sleep away his terriors, only for him to wake up in horror as you loom over his bed with a grotesque smile.\n"
        printFast(statement2)
        statement3 = "The mad scientist panicks and flees his aprtment screaming in horror, leaving only you inside the empty room.\n"
        printFast(statement3)
        statement4 = ("What would you like to do?\n")
        printFast(statement4)
        print("a. flee out the window\n")
        print("b. do nothing\n")
        action = input("> ")
        accepatble_actions = ['a', 'b']
        while action.lower() not in accepatble_actions:
            print("Unknown action, try again.\n")
            action = input("> ") 
        if action.lower() == 'quit':
            sys.exit()
        elif action == 'a':
            player_move2()
        
        elif action == 'b': 
            statement1 = "Time passes and you begin to feel very hungary and alone. You flee the aprtment to find refuge."
            printFast(statement1)
            player_move2()
    
        
    elif myAction == 'b':
        player_move2()

    elif myAction == 'c':
        statement1 = "Time passes and you begin to feel very hungary and alone. You flee the aprtment to find refuge."
        printFast(statement1)
        player_move2()

        
        
    
def player_move2():
    statement1 = "You jump down the window into the cold stormy night.\n"
    printFast(statement1)
    statement2 = "After walking though the forest for a while you come across a small village.\n"
    printFast(statement2)
    statement3 = "All villagers that see you flee in horror on sight but you notice a small hut with a few elderly folk living in it.\n"
    printFast(statement3)
    statement4 = "What would you like to do?\n"
    printFast(statement4)
    print("a. flee the village too look for refuge.\n")
    print("b. steal some of the villagers food and learn more from them.\n")
    print("c. stay where you are and continue to observe the villagers.\n")
    action = input("> ")
    accepatble_actions = ['a', 'b', 'c']
    while action.lower() not in accepatble_actions:
        print("Unknown action, try again.\n")
        action = input("> ") 
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in accepatble_actions:
        player_move3(action.lower())

def player_move3(myAction):
    if myAction == 'a':
        statement1 = "You flee the village looking for shelter as you are now starving and cold from the weather.\n"
        printFast(statement1)
        statement2 = "You eventaully come across a cave, and deside to take refuge.\n"
        printFast(statement2)
        statement3 = "Falling asleep, you wake up the next morning hungary and looking for food.\n"
        printFast(statement3)
        statement4 = "What would you like to do?\n"
        printFast(statement4)
        print("a. flee the village too look for refuge.\n")
        print("b. steal some of the villagers food and learn more from them.\n")
        print("c. do nothing\n")
        action = input("> ")
        accepatble_actions = ['a', 'b', 'c']
        while action.lower() not in accepatble_actions:
            print("Unknown action, try again.\n")
            action = input("> ") 
        if action.lower() == 'quit':
            sys.exit()
        elif action.lower() in accepatble_actions:
            print("You've reached the end of the demo. Thanks for playing!")
    elif myAction == 'b':
        statement1 = "You wait for the villagers to leave before sneaking in thier house, looking for food and other useful items.\n"
        printFast(statement1)
        statement4 = "What would you like to do?\n"
        printFast(statement4)
        print("a. look in the kitchen.\n")
        print("b. look in one of the bedrooms.\n")
        print("c. look in the basement.\n")
        action = input("> ")
        accepatble_actions = ['a', 'b', 'c']
        while action.lower() not in accepatble_actions:
            print("Unknown action, try again.\n")
            action = input("> ") 
        if action.lower() == 'quit':
            sys.exit()
        elif action.lower() in accepatble_actions:
            print("You've reached the end of the demo. Thanks for playing!")
    elif myAction == 'c':
        statement1 = "As you continue to hide near a tree and easedrop on the villager's conversations, you begin to learn more about them.\n"
        printFast(statement1)
        statement2 = "You begin the learn language, how humans live, the concept of emotions and family.\n"
        printFast(statement2)
        statement3 = "You begin to question where you came from, and what you are.\n"
        printFast(statement3)
        statement4 = "You see the villagers begin to go to bed\n"
        printFast(statement4)
        statement5 = "What would you like to do?\n"
        printFast(statement5)
        print("a. flee the village to look for refuge.\n")
        print("b. enter in the house to look for food.\n")
        action = input("> ")
        accepatble_actions = ['a', 'b']
        while action.lower() not in accepatble_actions:
            print("Unknown action, try again.\n")
            action = input("> ") 
        if action.lower() == 'quit':
            sys.exit()
        elif action.lower() in accepatble_actions:
            player_move3(action)
        
         

    
    
    
def main_game_loop():
    prompt()
    # here if puzzles have been solved, boss defeated, explored everything, etc

def setup_game():
    os.system('clear')
    ### NAME COLLECTING
    question1 = "Hello there, what's your name?\n"
    printFast(question1)
    player_name = input("> ")
    myPlayer.name = player_name

    ## JOB HANDLE
    question2 = "My dear friend " + player_name + ", which character do you wish to play?\n"
    question2added = "(You can play as a Imogen, Iachimo, Elizabeth Bennet, Mr. Fitzwilliam Darcy, Victor Frankenstein, The Monster, Laura, or Carmilla)\n"
    printFast(question2)
    for char in question2added:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['imogen', 'iachimo', 'elizabeth bennet', 'mr. fitzwilliam darcy', 'victor frankenstein', 'the monster', 'laura', 'carmilla']

    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job 
        print("You are now " + player_job + "!\n")
    
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() not in valid_jobs:
            myPlayer.job = player_job
            print("You are now " + player_job + "!\n")

    ## Player stats
    if myPlayer.job is 'the monster':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is 'victor frankenstein':
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is 'imogen':
        self.hp = 60
        self.mp = 60

    ### Intro
    question3 = "Welcome, " + player_name + ". Enjoy playing as " + player_job + ".\n"
    printFast(question3)
    
    
    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "I hope it greets you well!\n"
    speech3 = "Just make sure you don't make to many wrong decisions...\n"
    speech4 = "Heheheheh....\n"

    for char in speech1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    for char in speech2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    for char in speech3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    for char in speech4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    
    os.system('clear')
    print("#######################")
    print("#     Let's start     #")
    print("#######################")
    main_game_loop()

title_screen()