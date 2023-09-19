# Function to handle input and validate choices
def get_player_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter a valid option.")

# Function to handle encounters
def handle_encounter(encounter_name, success_text, failure_text):
    print(encounter_name)
    choice = get_player_choice("Do you want to proceed? (Yes/No): ", ["yes", "no"])
    if choice == "yes":
        print(success_text)
        return True
    else:
        print(failure_text)
        return False

def main():
    name = input("Enter your name: ")
    print(f"Welcome to the Haunted House, {name}!")
    print("The house has a legend, the legend of the lost treasure.")
    print("You have always wanted to go to the house, but something always held you back. Today was different.")
    print("There was a face in the attic window, a face of a young woman.")
    print("Something drew you in; you had to find out who she was...")
    print("The door blew open with a gust of wind, you enter the house...")

    current_room = "hallway"
    progress = 0
    has_companion = False
    has_valuable_artifact = False

    while True:
        print(f"You are currently in the {current_room}.")
        print("Options: explore, quit")
        choice = get_player_choice("What would you like to do? ", ["explore", "quit"])

        if choice == "quit":
            print("You decide to leave the haunted house. Thanks for playing!")
            break

        if choice == "explore":
            progress += 1
            print(f"You've explored {progress} rooms.")

            if current_room == "hallway":
                if handle_encounter("You hear a strange noise coming from the kitchen.", "You found a valuable artifact!", "A ghostly presence scares you away."):
                    print("You've successfully collected the valuable artifact!")
                    has_valuable_artifact = True
                current_room = "kitchen"

            elif current_room == "kitchen":
                if not has_companion:
                    if handle_encounter("As you enter the bedroom, you see a shadowy figure.", "You've made a new friend!", "The figure disappears into thin air."):
                        print("The shadowy figure offers to help you.")
                        print("You now have a companion to assist you on your journey!")
                        has_companion = True
                current_room = "bedroom"

            elif current_room == "bedroom":
                if handle_encounter("You notice a trapdoor in the hallway. It's locked.", "You unlocked the trapdoor and found a secret passage!", "The lock is too complex, and you can't open it."):
                    print("You've discovered a hidden passage to the basement!")
                current_room = "basement"

            elif current_room == "basement":
                if has_valuable_artifact and has_companion:
                    if handle_encounter("In the attic, you confront a zombie threatening the young woman. Do you want to use the valuable artifact to defeat the zombie?", "You defeat the zombie and save the young woman!", "The zombie overpowers you."):
                        print("Congratulations, you've defeated the zombie and saved the young woman!")
                        print("As you leave the house, you notice the young woman's spirit is at peace.")
                        print("You've successfully completed your adventure!")
                        break  # End the game
                else:
                    print("You enter the attic, but you are not prepared to confront the zombie. You should explore further and collect necessary items.")
            else:
                if progress >= 5:
                    print("You've explored thoroughly and found all there is to find in the house.")
                else:
                    print("You explore the house but find nothing else of significance.")

if __name__ == "__main__":
    main()
