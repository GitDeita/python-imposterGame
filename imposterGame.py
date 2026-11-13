#IMPOSTER GAME

#Players assigned words form given category
#Players assigned imposter
#Players class gets hidden
#Imposters' result after typing name is class and category
#Players' result after typing name is class, word, and category

import json
import random
import pyfiglet

#opens and reads database
with open('imposterWords.json', 'r', encoding='utf-8') as file:
    wordDatabase = json.load(file)

#initialization of variables
categories = list(wordDatabase.keys())
randomCategory = random.choice(categories)
randomWord = (wordDatabase[randomCategory][random.randint(0, len(wordDatabase[randomCategory])-1)])
playerList = []
x = ""
y = ""
n = 0
rolecheck = ""

#Inputs player names into list and then displays list
print("Input player names, type 'exit' to exit")
while x != "exit":
    x = str(input("Input name: "))
    playerList.append(x)
playerList.remove("exit")
print(playerList)

#One imposter for now
imposter = playerList[random.randint(0,len(playerList)-1)]
#starting player
startingPlayer = playerList[random.randint(0,len(playerList)-1)]

#Tells user roles, category, and word
print("PASS DEVICE AROUND AND INPUT NAME TO SEE ROLE, THEN PRESS ENTER, TYPE 'exit' TO MOVE ON")
while rolecheck != "exit":
    rolecheck = input("Name: ")
    if rolecheck in playerList and rolecheck != imposter:
        print(pyfiglet.figlet_format("Player", font="slant"))
        print(f"Category is {randomCategory}, word is {randomWord}.")
        input("press enter when done reading")
        print("skipping\n"*50)
    if rolecheck in playerList and rolecheck == imposter:
        print(pyfiglet.figlet_format("Imposter", font="slant"))
        print(f"Category is {randomCategory}, blend in.")
        input("press enter when done reading")
        print("skipping\n"*50)

print("Starting player is:")
print(pyfiglet.figlet_format(startingPlayer, font="slant"))

vote = input("VOTE PROPOSED IMPOSTER OUT: ")
while n < 2:
    if vote == imposter:
        print(pyfiglet.figlet_format("Correct!!!", font="slant"))
        exit()
    elif vote != imposter and n == 0:
        print(pyfiglet.figlet_format("Wrong...", font="slant"))
        print("Try again!")
        vote = input("VOTE PROPOSED IMPOSTER OUT: ")
        n += 1
    elif vote != imposter and n == 1:
        print(pyfiglet.figlet_format("You Lose...", font="slant"))
        n += 1
