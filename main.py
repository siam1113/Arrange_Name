'''
  Project Name : ArrangeName
  Author : Siam Hasan

'''
from game_functions import mixupName, displayStatus, swap, joinLetters

'''
--------------------------
Game operation starts here
--------------------------
'''
# Game status
gameOn = False

# Storages
name = ''
letters = []
mixedLetters = []

# Welcome message
print(
    f"\n\n\033[46mWelcome to ArrangeName. Let's see how well you know your name...\033[0m")
print(f"\033[46mWe have mixed up your name letters, Now it's your job is to arrange them again.\033[0m\n\n")

# Running the game
while True:
    # Booting the game
    if gameOn == False:
        # Ask for name
        name = input("\n\n\033[94mYour name ? \033[0m").upper()

        # Ask for start or end the game
        choice = int(
            input("Would you like to start(1) or end(0) the game {name} ? "))

        # Start or End the game
        if choice == 0:
            # Goodbye message
            print(
                f"\n\n\033[33mBye {name}👋! \nCome back again when you feel you are forgetting your name 😁\033[0m\n")
            break
        elif choice == 1:
            # Storing the info
            letters = list(name)

            # Mixing the letters
            # Mixes the letters and stores them in list [mixedLetters]
            lengthOfName = len(name)
            mixupName(lengthOfName, letters, mixedLetters)
        else:
            # Validation message
            print("\n⚠️  Choice the right option  ⚠️\n\n")
            continue

    # Updating game status to On
    gameOn = True

    # Display user progress
    displayStatus(mixedLetters)

    # User action
    print(
        f"\n\n\033[95m\n\nPut two index number you want to swap between \033[0m")
    index1 = int(input("Index 1 : "))
    index2 = int(input("Index 2 : "))

    # Swap the values
    swap(index1, index2, mixedLetters)

    # Validate progress
    userProgress = joinLetters(mixedLetters).upper()
    if name == userProgress:
        # Display success message
        print("\033\n\n[32mSuccess 🙌 You have done it \033[0m ")

        # Updating game status
        gameOn = False
        name = ''
        letters = []
        mixedLetters = []
    else:
        print("\033\n[31mKeep going ...\n\033[0m")
