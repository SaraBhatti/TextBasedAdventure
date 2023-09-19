'''
Project Brief

Remember Adventure? Well, we’re going to build a more basic version of that. A complete text
game, the program will let users move through rooms based on user input and get descriptions
of each room. To create this, you’ll need to 
- establish the direction in which the user can move, 
- a way to track how far the user has moved (and therefore which room he/she is in), 
- and to print out a description. 
- You’ll also need to set limits for how far the user can move. In other words,
- create “walls” around the rooms that tell the user, “You can’t move further in this direction.”

Concepts to keep in mind:
● Strings - Descripitions and using dictionary
● Variables - Rooms 
● Input/Output
● If/Else Statements
● Print
● List
● Integers - Moves made 

Deliverables
The tricky parts here will involve setting up the directions and keeping track of just how far the
user has “walked” in the game. I suggest sticking to just a few basic descriptions or rooms,
perhaps 6 at most. This project also continues to build on using user inputted data. It can be a
relatively basic game, but if you want to build this into a vast, complex word, the coding will get
substantially harder, especially if you want your user to start interacting with actual objects
within the game. That complexity could be great, if you’d like to make this into a long term
project. *Hint hint.



'''

import time

#MAP
room1 = "Living Room"
room2 = "Bedroom 1"
room3 = "Kitchen"
room4 = "Kitchen Pantry"
room5 = "Bedroom 2"
room6 = "Ensuite (Bedroom2)"
room7 = "Bedroom 3"
room8 = "Bathroom"
room9 = "Attic"
staircase1 = "Staircase"
staircase2 = "Staircase"

layout = {
    room1: {
        'description': "You are in the living room, this house hasn't been lived in for years",
        'items': ['Rucksack', 'Torchlight'],
        'direction':[room3, staircase1, room2]
    },  
    room2: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['Hallway']
    }, 
    room3: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['hallway', 'up the stairs']
    }, 
    room4: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['hallway', 'up the stairs']
    }, 
    room5: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['hallway', 'up the stairs']
    }, 
    room6: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['hallway', 'up the stairs']
    }, 
    room7: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['hallway', 'up the stairs']
    }, 
    room8: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['hallway', 'up the stairs']
    }, 
    room9: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['hallway', 'up the stairs']
    }, 
    staircase1: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['hallway', 'up the stairs']
    }, 
    staircase2: {
        'description': '.........',
        'items': ['object 1', 'object 2', 'object 3'],
        'direction':['hallway', 'up the stairs']
    }, 
}

# Variables
#distanceWalked = 0 # counts how many moves they have made or walked
movesAllowed = 10


# Functions
def roomDesc(room):
     print (layout[room]['description'])


def items(room):
    print("Here are the items you can see are useful")
    for item in layout[room]['items']:
        print(item)
    print("\n")

def direction(room):
    roomList = []
    print("There are only a few direction you can move now")
    for direction in layout[room]['direction']:
        roomList.append(direction)
        print(direction)
    print("\n")

    move = input("Type which direction you would like to go?: ")
    move = move.capitalize()
    #return move.capitalize()
    #Not working to valdiate response
   
    while move not in roomList:
        move = input(f"Please enter any of the following rooms:{roomList} OR enter quit: ")
        if move == 'quit':
            quit()
    
    return move.capitalize()
    
    
    
def tasks(room):
    roomDesc(room)
    #show items
    items (room)
    





# Timer
'''
start_time = time.time() # current time stamp
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
'''


#Start Game
print("The apocalypse has happened, a virus has spread throughout the world causing mutations in humans")
#time.sleep(2)
print ("The population is gradually dying and the deceased are starting to turn into zombies.")
#time.sleep(2)
print("It's been 5 years since the day of the first zombie and today is another day for you trying to survice and stay alive")
#time.sleep(2)
print("You need to collect supplies and find a first aid kit to heal a wound you picked up")
#time.sleep(2)
print("You see a haunted house that you MUST enter")
#time.sleep(2)
print ("Your goal is to search rooms for a first aid kit, collect supplies and most importantly get out within 10mins before any zombies start gathering outside the house")
#time.sleep(2)

'''
startGame = input("Are you ready to enter the haunted house?: Y / N: ")


#Option to play game
while startGame.lower() != 'y':
    if startGame.lower() == 'n':
        print("If you don't enter the house its only a matter of time before the zombies get you!")
        time.sleep(3)
        print("Game Ending")
        quit()
    elif startGame.lower() != 'y':
        print ("Please only enter the values 'Y' or 'N'")
        startGame = input("Are you ready to enter the haunted house?: Y / N: ")
        print("")

'''

#Enter Game and show rules


print("It take courage to enter the house!!")
print("Collect items, find the first aid kit and get the hell out!")
print("")

distanceWalked = -1 
# Start the game from the living Room
currentRoom = room1 


while distanceWalked < 2: 
    
    distanceWalked += 1

    if currentRoom == room1:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("")
    elif currentRoom == room2:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("")    
    elif currentRoom == room3:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("") 
    elif currentRoom == room4:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("") 
    elif currentRoom == room5:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("") 
    elif currentRoom == room6:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("") 
    elif currentRoom == room7:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("") 
    elif currentRoom == room8:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("") 
    elif currentRoom == room9:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("") 
    elif currentRoom == staircase1:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print("") 
    elif currentRoom == staircase2:
        tasks(currentRoom)
        currentRoom = direction(currentRoom)
        print() 
    else:
        print("Not a valid response")
        currentRoom = input("Type which direction you would like to go?: ")









