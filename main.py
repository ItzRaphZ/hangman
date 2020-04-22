import random

gameIsRunning = True

#Count the number of words exist
file = open("words.txt", "r")
wordsCounter = 0

for x in file:
    wordsCounter += 1

file.close()

#Choose a random word
r = random.randint(0, wordsCounter-1)

file = open("words.txt", "r")

for x in range(r):
    file.readline()

word = file.readline()

file.close()

#Game
characters = list(word)
characters.pop()

line = []

lives = 5

for x in range(len(characters)):
    line.append("*")

print("WELCOME TO HANGMAN")
print("Let's start\n")

while gameIsRunning == True:
    for x in line:
        print(x, end =" ")
    print(f"\n\nLives: {lives}")
    guess = input("Guess a letter: ")

    if len(guess) > 1:
        print("You can only guess one letter")
    elif len(guess) < 1:
        print("You can only guess one letter")
    else:
        if guess in characters:
            print("\n\n\nCORRECT!\n")

            for x in range(len(characters)):
                if guess == characters[x]:
                    line[x] = guess
        else:
            print("WRONG! REMOVING ONE LIFE\n")
            lives-=1

    completed = True
    for x in line:
        if x == "*":
            completed = False
            break

    if completed == True:
        gameIsRunning = False
        print("\n\nCONGRATULATION!!! YOU WON.... nothing, well played anyway!")
        print("word: ", end="")
        for x in line:
            print(x, end ="")
        input("\nPress any key to leave...")

    if lives == 0:
        gameIsRunning = False
        print("\n\nGame Over!")
        input("Press any key to leave...")
