# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression

def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1

def binarySearch(anArray, item):
    lower, upper = 0, len(anArray) - 1
    while(upper >= lower):
        middle = (upper + lower) // 2
        if item == anArray[middle]:
            return middle
        elif item < anArray[middle]:
            upper = middle - 1
        else:
            lower = middle + 1

    return -1

def printMainMenu():
    print("Main Menu")
    print("1: Spell check a word (Linear Search)")
    print("2: Spell Check a Word (Binary Search)")
    print("3: Spell Check Alice in Wonderland (Linear Search)")
    print("4: Spell Check Alice in Wonderland (Binary Search)")
    print("5: Exit")
    return int(input("Enter menu selection (1-5):"))

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    inp = printMainMenu()
    while inp != 5:
        
        match inp:
            case 1:
                inputWord = input("Please enter a word: ")
                print("Linear Search Starting...")
                res = linearSearch(dictionary, inputWord)
                if res == -1:
                    print(f"{inputWord} is NOT IN the dictionary.")
                else:
                    print(f"{inputWord} is IN the dictionary at position {res}")
            case 2:
                inputWord = input("Please enter a word: ")
                print("Linear Search Starting...")
                res = binarySearch(dictionary, inputWord)
                if res == -1:
                    print(f"{inputWord} is NOT IN the dictionary.")
                else:
                    print(f"{inputWord} is IN the dictionary at position {res}")
            case 3:
                print("AAAAA")
        inp = printMainMenu()

# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()
