import random

''''
$Takes @lengthOfTheName, @letterOfTheName and @mixedLetterList as parameter
$Adds the letter of the name in the @mixedLetterList
'''


def mixupName(lenName, letters, mixedLetters):
    indexes = []
    for i in range(0, lenName):
        # Get updated length
        # Reduce by 1 to get index within the range
        lengthOfLetters = len(letters) - 1

        # Add a random letter from the name at i (0-n) index
        index = random.randint(0, lengthOfLetters)
        mixedLetters.append(letters[index])

        # Remove the added letter
        letters.pop(index)


'''
$Takes the @firstIndex, @secondIndex and a @list
$Swaps the values between the indexes from the @list
'''


def swap(index1, index2, mixedLetters):
    # Save the value in variable
    indexOneValue = mixedLetters[index1]
    indexTwoValue = mixedLetters[index2]

    # Change the values
    mixedLetters[index1] = indexTwoValue
    mixedLetters[index2] = indexOneValue


'''
$Takes @listOfLetters
$Turns them in string
'''


def joinLetters(letters):
    return ("".join(letters))


'''
$Takes the @listOfLetter 
$Displays them with indexes in a table format
'''


def displayStatus(mixedLetters):
    print("\n\n")
    # Letters row
    for index, letter in enumerate(mixedLetters):
        if index == 0:
            # Row one header
            print(f"\033[01mLetters ->\t\033[0m", end=" ")

        print(f"\033[34m{letter}\t\033[0m", end=" ")

    # Go to a new row
    print("\n")

    # Index row
    for index, letter in enumerate(mixedLetters):
        if index == 0:
            # Row two header
            print(f"\033[01mIndexes ->\t\033[0m", end=" ")
        print(f"\033[37m{index}\t\033[0m", end=" ")
