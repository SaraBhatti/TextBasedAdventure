# import library
import random

# Function to handle input and choices
def get_player_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter a valid option.")

# Function to handle encounters
def handle_encounter(encounter_name, success_text, failure_text, success_chance):
    print(encounter_name)
    choice = get_player_choice("Do you want to proceed? (Yes/No): ", ["yes", "no"])
    if choice == "yes":
        if random.random() < success_chance:
            print(success_text)
            return True
        else:
            print(failure_text)
            return False
    else:
        return False

def main():
    name = input("Enter your name: ")
    print(f"Welcome to the Haunted House, {name}!")
    print("The house has a legend, the legend of the lost treasure.")
    print("You have always wanted to go to the house, but something always held you back. Today was different.")
    print("There was a face in the attic window, a face of a young woman.")
    print("Something drew you in; you had to find out who she was...")
    print("The door blew open with a gust of wind, you enter the house...")

    # Initialize step count
    step_count = 0

    print("You find yourself in the hallway.")
    step_count += 1

    while True:
        print("Options: explore, quit")
        choice = get_player_choice("What would you like to do? ", ["explore", "quit"])

        if choice == "quit":
            print("You decide to leave the haunted house. Thanks for playing!")
            break

        if choice == "explore":
            step_count += 1
            print(f"Step count: {step_count}")

            if step_count == 5:
                if handle_encounter("You hear a strange noise coming from the kitchen.", "You found a valuable artifact!", "A ghostly presence scares you away.", 0.6):
                    print("You've successfully collected the valuable artifact!")

            if step_count == 10:
                if handle_encounter("As you enter the bedroom, you see a shadowy figure.", "You've made a new friend!", "The figure disappears into thin air.", 0.4):
                    print("The shadowy figure offers to help you.")
                    print("You now have a companion to assist you on your journey!")

            if step_count == 15:
                if handle_encounter("You notice a trapdoor in the hallway. It's locked.", "You unlocked the trapdoor and found a secret passage!", "The lock is too complex, and you can't open it.", 0.7):
                    print("You've discovered a hidden passage to the basement!")

            if step_count == 20:
                if handle_encounter("In the basement, you find a chest. Do you want to open it?", "You've found the lost treasure!", "The chest is empty.", 0.5):
                    print("Congratulations, you've found the legendary treasure!")
                    print("As you leave the house, you notice the young woman's spirit is at peace.")
                    print("You've successfully completed your adventure!")
                else:
                    print("The chest was empty, and you leave the basement disappointed.")

if __name__ == "__main__":
    main()
