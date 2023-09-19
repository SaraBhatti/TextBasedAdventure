#Welcome to the game
name = input("Enter your name: ")
print(f"Welcome to the Haunted House, {name}!")
print("The house has a legend, the legend of the lost treasure.")
print("You have always wanted to go to the house, but something always held you back. Today was different.")

# Aim of the game is to reach the attic
print("There was a face in the attic window, a face of a young woman... Did she need our help?")
print("Something drew you in; you had to find out who she was...")
print("With a gust of wing, the door blew open, you enter the house...")

#Step count
step_count = 0

choice = input("On the floor, you see there is a sword and some keys. Do you want to pick them up? (please enter 'Yes' or 'No') ")

if choice == 'Yes':
    print(f"Excellent choice, {name}, these will be useful!")
    step_count += 1
    print(f"Step count: {step_count}")
    print(f"You now enter the hallway. Watch out, {name}, a zombie has followed you into the house!")
    choice2 = input("Where would you like to go? Select: Pantry, Kitchen, Stairs, or the Bedroom: ")
elif choice == 'No':
    print(f"Bad move, {name}, you needed those items.")
    print("GAME OVER")
    quit()
else:
    print("Invalid choice. Please enter Yes or No")

if choice2 == "Pantry":
    print("There is nowhere to go; the Zombie has eaten your brains.")
    print("You are now dead.")
    print("GAME OVER")
    quit()
elif choice2 == "Kitchen":
    print("You find some food and a knife.")
    knife = input("Would you like to pick them up? Yes or No? ")
    step_count += 1

    if knife == "Yes":
        print(f"Smart move, {name}, these will be useful!")
        step_count += 1
        print(f"Step count: {step_count}")
    elif knife == "No":
        print("That may have been a mistake!")
    else:
        print("Invalid choice. Please enter Yes or No")
elif choice2 == "Stairs":
    print("Let's see what's up here.")
    step_count += 1
    print(f"Step count: {step_count}")
elif choice2 == "Bedroom":
    print("You found a First Aid kit.")
    firstaid = input("Do you want to take it with you? ")
    step_count += 1

    if firstaid == "Yes":
        print(f"Smart move, {name}, it will be useful!")
        step_count += 1
        print(f"Step count: {step_count}")
    elif firstaid == "No":
        print("That may have been a mistake!")
    else:
        print("Invalid choice. Please enter Yes or No")
else:
    print("Invalid choice. Please enter Pantry, Kitchen, Stairs, or Bedroom.")

attic_key = False
attic_sword = False
attic_zombie_alive = True

while attic_zombie_alive:
    choice3 = input("You are in the attic. There is a young woman trapped by a zombie. Do you want to use the items you collected to save her? (please enter 'Yes' or 'No') ")

    if choice3 == 'Yes':
        if attic_key and attic_sword:
            print(f"You bravely use the sword to defeat the zombie and rescue the young woman, {name}! Congratulations, you win!")
            print(f"Step count: {step_count}")
            break
        else:
            print("You need both the sword and the keys to save the young woman. Keep looking!")
    elif choice3 == 'No':
        print("You hesitate and decide not to take action. The zombie attacks you and eats your brains.")
        print("GAME OVER")
        quit()
    else:
        print("Invalid choice. Please enter Yes or No")

    if not attic_key:
        attic_key_choice = input("You notice a set of keys in the attic. Would you like to pick them up? (please enter 'Yes' or 'No') ")
        if attic_key_choice == 'Yes':
            attic_key = True
            step_count += 1
            print(f"You picked up the keys. Step count: {step_count}")
        elif attic_key_choice == 'No':
            print("You leave the keys behind.")
        else:
            print("Invalid choice. Please enter Yes or No")

    if not attic_sword:
        attic_sword_choice = input("You also see a sword in the attic. Would you like to pick it up? (please enter 'Yes' or 'No') ")
        if attic_sword_choice == 'Yes':
            attic_sword = True
            step_count += 1
            print(f"You picked up the sword. Step count: {step_count}")
        elif attic_sword_choice == 'No':
            print("You leave the sword behind.")
        else:
            print("Invalid choice. Please enter Yes or No")


