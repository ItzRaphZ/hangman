import random

#Count the number of words exist
file = open("words.txt", "r")
wordsCounter = 0

for x in file:
    wordsCounter += 1

file.close()

#Choose a random word
r = random.randint(0, wordsCounter)

file = open("words.txt", "r")

for x in range(r):
    file.readline()

word = file.readline()

file.close()


