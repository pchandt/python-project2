#!/usr/bin/python3
import crayons
import random

"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""


def riddle():
    riddles = ['What has words, but never speaks?',
               'What month of the year has 28 days?',
               'What is always in front of you but can’t be seen?',
               'I have branches, but no fruit, trunk or leaves. What am I?',
               'What has many keys but can’t open a single lock?',
               'Where does today come before yesterday?',
               'What goes up and down but doesn’t move?',
               'What has a head and a tail but no body?',
               'What can you catch, but not throw?',
               'What has many teeth, but can’t bite?'
               ]
    ans = ['book',
           'all',
           'future',
           'bank',
           'piano',
           'dictionary',
           'staircase',
           'coin',
           'cold',
           'comb']
    print(
        'If you get 5 correct answers, you will get "treasure".\n'
        'If you get 10 correct answers you will win the game.\n'
        'If you get 10 incorrect answers you will lose the game.\n')
    user_input = ''
    while user_input == '':
        user_input = input("Enter 'go' to start the game and 'quit' to stop the game.\n>")

    if user_input == 'go':
        random_riddles = random.sample(range(len(riddles)), 10)

        correct_ans = 0
        incorrect_ans = 0
        for i in random_riddles:
            print((riddles[i]))
            answer = input('Please enter your answer in one word: ')

            if answer == ans[i]:
                print("You are right!")
                correct_ans += 1
                print(correct_ans)

                if correct_ans >= 5:
                    print("You got your treasure")
                    inventory.append("treasure")

                elif correct_ans == 10:
                    print("CONGRATULATIONS! YOU WON THE GAME.")
                    exit()

            else:
                print("Sorry! You're wrong!")
                incorrect_ans += 1
                print(incorrect_ans)

                if incorrect_ans == 10:
                    print("SORRY, YOU LOSE THE GAME.")
                    exit()

        else:
            print(crayons.yellow("Better luck next time."))

    if user_input == 'quit':
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
    if "mystery" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['mystery'])

        #

    print(crayons.red("---------------------------"))


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

        # count increment after each move
        count_move += 1
        print(count_move)
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

    if move[0] == 'solve':
        if 'mystery' in rooms[currentRoom] and move[1] in rooms[currentRoom]['mystery']:
            riddle()
            del rooms[currentRoom]['mystery']
            if 'treasure' in inventory:
                del rooms['Guest room']['item']
        else:
            print("There is no riddle in this room!")

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'treasure' in inventory:
        print('You escaped the house with the ultra rare key, magic potion, and valuable treasure... YOU WIN!')
        break
