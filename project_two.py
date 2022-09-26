#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# import random
import random


def riddle():
    """A function to solve riddle """

    # list of riddles
    riddles = ["What has words, but never speaks?",
               "What month of the year has 28 days?",
               "What is always in front of you but can’t be seen?",
               "I have branches, but no fruit, trunk or leaves. What am I?",
               "What has many keys but can’t open a single lock?",
               "Where does today come before yesterday?",
               "What goes up and down but doesn’t move?",
               "What has a head and a tail but no body?",
               "What can you catch, but not throw?",
               "What has many teeth, but can’t bite?"
               ]
    # list of answers to riddles
    riddle_answer = ["book",
                     "all",
                     "future",
                     "bank",
                     "piano",
                     "dictionary",
                     "staircase",
                     "coin",
                     "cold",
                     "comb"]

    # display statement when player start to solve riddle.
    print(
        "If you get 5 correct answers, you will get 'treasure'.\n"
        "If you get 10 correct answers you will win the game.\n"
        "If you get 10 incorrect answers you will lose the game.\n")

    # the player MUST type something in
    # otherwise input will keep asking
    user_input = ""
    while user_input == "":
        # ask user to choose one of two options
        user_input = input("Enter 'go' to start the game and 'quit' to stop the game.\n>")

        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        user_input = user_input.lower().split(" ", 1)

        # if user type go
        if user_input[0] == "go":
            # random index of riddle and ans lists
            random_riddles = random.sample(range(len(riddles)), 10)

            # initial count of correct answers
            correct_ans = 0
            # initial count of incorrect answers
            incorrect_ans = 0
            # print riddle at index i
            for i in random_riddles:
                print((riddles[i]))
                # collect answer in one word from user
                answer = ""
                while answer == "":
                    answer = input("Please enter your answer in one word: ")
                    # normalizing input:
                    answer = answer.lower().split(" ", 1)

                # if user answer matches the answer in the list named riddle_answer
                # display they are correct and increase the count of correct answer
                if answer[0] == riddle_answer[i]:
                    print("You are right!")
                    correct_ans += 1
                    print(f"Correct answer count = {correct_ans}\n")

                    # if count of correct answers is equal to 5 add treasure to their inventory
                    if correct_ans == 5:
                        print("You got your treasure")
                        inventory.append("treasure")

                    # if count of correct answers is equal to 10 user wins the game and game ends
                    elif correct_ans == 10:
                        print("CONGRATULATIONS! YOU WON THE GAME.")
                        exit()

                # if user answer doesn't match to the answer list display sorry message
                # increase the count of incorrect answers
                else:
                    print("Sorry! You're wrong!")
                    incorrect_ans += 1
                    print(f"Incorrect answer count = {incorrect_ans}\n")

                    # if count of incorrect answers is equal to 10 user loses the game and game ends.
                    if incorrect_ans == 10:
                        print("SORRY, YOU LOSE THE GAME.")
                        exit()

        # if user type "quit"
        if user_input == "quit":
            print("Bye bye.")


def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      solve [mystery]
    ''')


def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    # check if there's a mystery in the room, if so print it
    if "mystery" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['mystery'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'down': 'Store room',
        'up': 'Bed room',
        'north': 'Pantry',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'north': 'Garage',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room',
    },
    'Store room': {
        'up': 'Hall',
        'east': 'Laundry room',

    },
    'Laundry room': {
        'west': 'Store room',
        'mystery': 'riddle'
    },
    'Pantry': {
        'south': 'Hall',
        'west': 'Garage'
    },
    'Garage': {
        'east': 'Pantry',
        'south': 'Dining'
    },
    'Bed room': {
        'down': 'Hall',
        'east': 'Guest room',
    },
    'Guest room': {
        'west': 'Bed room',
        'item': 'treasure'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()
# initial count of move
count_move = 0
# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')
        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]
        move = move.lower().split(" ", 1)

        # increase the number of count after each move
        count_move += 1
        print(f"Move count = {count_move}")
        # alternate condition to lose the game.
        if count_move == 25:
            print("YOU LOSE THE GAME.")
            exit()

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    # 1. if the current room contains a riddle.
    # 2. if the player wishes to solve riddle.
    if move[0] == 'solve':
        # check if the room contains riddle
        if 'mystery' in rooms[currentRoom] and move[1] in rooms[currentRoom]['mystery']:
            # call the function to play riddle
            riddle()
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['mystery']
            # if player gets treasure in their inventory by solving riddle then delete treasure from its room
            if 'treasure' in inventory:
                del rooms['Guest room']['item']
        else:
            print("There is no riddle in this room!")

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'treasure' in inventory:
        print('You escaped the house with the ultra rare key, magic potion, and valuable treasure... YOU WIN!')
        break
