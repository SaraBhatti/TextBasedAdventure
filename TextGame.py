room1 = "Living Room"
room2 = "Bedroom"
room3 = "Kitchen"

rooms = {
    'start': {
        'description': 'You are in a hunted house. There is a door to your north.',
        'north': 'room1'
    },
    'room1': {
        'description': 'You are in room 1. There is a door to your east and south.',
        'east': 'room2',
        'south': 'start'
    },
    'room2': {
        'description': 'You are in room 2. There is a door to your west and south.',
        'west': 'room1',
        'south': 'room3'
    },
    'room3': {
        'description': 'You are in room 3. You found the treasure! Congratulations!',
        'end': True
    }
}

def show_room(room):
    print(room['description'])

    if 'north' in room:
        print('There is a door to your north.')
    if 'east' in room:
        print('There is a door to your east.')
    if 'south' in room:
        print('There is a door to your south.')
    if 'west' in room:
        print('There is a door to your west.')

def get_action(room):
    while True:
        action = input('What do you want to do? ').lower().strip()

        if action == 'north' and 'north' in room:
            return room['north']
        elif action == 'east' and 'east' in room:
            return room['east']
        elif action == 'south' and 'south' in room:
            return room['south']
        elif action == 'west' and 'west' in room:
            return room['west']
        else:
            print('Invalid action. Try again.')

# Shah's Work

room1 = "Living Room"
room2 = "Bedroom"
room3 = "Kitchen"
# add 3 other rooms

#
distanceWalked = 0 # counts how many moves they have made or walked
movesAllowed = 10
currentRoom = ""
#Room and Description

rooms = {room1: "Description 1", room2: "Description 2", room3: "Description 3"}

print("you have entered a haunted house and walked through the front door you see a zombie and you need to head to the kitchen to get a knife")
print("you are in the hallway entrance, please move towards the living room to then access the kitchen")


move = input("What room would you like to go in:")



#switch statement 
if age > 90:
    print("You are too old to party, granny.")
elif age < 0:
    print("You're yet to be born")
elif age >= 18:
    print("You are allowed to party")
else: 
    "You're too young to party"

# Output: You are too old to party, granny.

def roomDesc(currentRoom):
    print (rooms[currentRoom])

def roomsEntered(distanceWalked):
    print("You have entered {rdistanceWalked} and have x amount of life remaininng")

def updateVariables(room):
    distanceWalked =+ 1
    currentRoom = room

