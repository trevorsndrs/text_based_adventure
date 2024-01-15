import os

# INVENTORY
inventory = []
# here lies the empty inventory list

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("#####  #   #  #####   ###   #####")
    print("#   #  #   #  #      #   #    #  ")
    print("#   #  #   #  #      #        #  ")
    print("#   #  #   #  #####   ###     #  ")
    print("#   #  #   #  #          #    #  ")
    print("#  #   #   #  #      #   #    #  ")
    print("### #  #####  #####   ###     #  ")
    print("")
    print("Start Game?")
    print("y/n")

    while True:
        user_input = input("Start Game?").lower()
        if user_input == "y":
            welcome_screen()
            break
        elif user_input == "n":
            print("You have chosen to forego your adventure. Coward.")
            break
        else:
            print("I do not recognize that command.")

def welcome_screen():
    clear_screen()
    
    # Initialize player_name outside the loop
    player_name = ""
    
    print("Greetings traveler... What is your name?")
    print("|")

    while True:
        user_input = input("Enter your name: ").strip()
        if user_input != "":
            player_name = user_input  # Assign the entered name to player_name
            print("Welcome, " + player_name + "! I wish you the best of luck on the journey you are about to")
            print("embark on. Good luck, you will need it...")
            level_one(player_name)
            break
        else:
            print("Please enter a name.")
    
    # Now player_name is accessible outside the loop
    return player_name

def level_one(player_name):
    clear_screen()
    print(f"{player_name}, you find yourself in a dark damp room, what would you like to do?")

    while True:
        print("")
        print("1. Look around.")
        print("2. Check my inventory.")
        print("3. Sleep for a while.")
        print("4. Move on to the next area.")
        user_input = input("Enter the number of your choice: ")

        if user_input == "1":
            print("")
            print("You check around the dim room and find a rusted key!")
            print("A Rusted Key was added to your inventory!")
            inventory.append("Rusted Key")
        elif user_input == "2": 
            if inventory:
                inventory.extend(["Rusted Iron Dagger", "Sealed Letter"])
                print("")
                print("Your inventory contains: {}".format(', '.join(inventory)))
            else:
                print("")
                print("Your inventory is empty.")
        elif user_input == "3": 
            print("")
            print("You decide to get some rest... You wake up feeling refreshed.")
        elif user_input == "4":
            level_two(player_name)
            break
        else:
            print("")
            print("I do not recognize that command or you have already chosen this option.")

def level_two(player_name):
    clear_screen()
    print(f"{player_name}, you find yourself face to face with a rusted iron door.")
    
    while True:
        print("")
        print("1. Attempt to open the door")
        print("2. Check my inventory.")
        print("3. Go back to the previous area.")
        user_input = input("Enter the number of your choice: ")

        if user_input == "1":
            clear_screen()
            print("")
            print("The door won't budge, it's locked")
            if "Rusted Key" in inventory:
                use_key_input = input("Would you like to use the Rusted Key to unlock the door? (y/n): ")
                
                if use_key_input == "y":
                    print("")
                    print("You use the Rusted Key and unlock the door, however it snapped inside the lock and is no longer usable")
                    inventory.remove("Rusted Key")
                    level_three(player_name)
                    break
                elif use_key_input == "n":
                    print("")
                    print("You decide not to use the Rusted Key.")
                else:
                    print("")
                    print("I do not recognize that command.")
            else:
                print("")
                print("The door is locked. You may need to find a key to unlock it.")
        elif user_input == "2":
            if inventory:
                print("")
                print("Your inventory contains: {}".format(', '.join(inventory)))
            else:
                print("")
                print("Your inventory is empty.")
        elif user_input == "3":
            print("")
            print("You decide to go back to the previous area")
            level_one(player_name)
            break
        else:
            print("")
            print("I do not recognize that command or you have already chosen this option.")

def level_three(player_name):
    clear_screen()
    print(f"Congratulations, {player_name}! You have reached the third level.")





# Call the main_menu function to start the game
main_menu()