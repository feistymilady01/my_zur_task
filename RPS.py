# Please istructor the correct link to my Assignment is in the anchor tag using the CLI.
#<!DOCTYPE html>
#<html lang="en">
<head>
    #<title>RSP</title>
#</head>
#<body>
    #<main>
        <a href="https://github.com/feistymilady01/Games">Correct link to the assignment!</a>
    #</main>
#</body>
#</html>

#Incase you dont use the link.... Here is the assignment below:
import random

input("You are welcome to Rock Paper Scissors game! Press enter to countinue \n")
choiceList = ['R','P', 'S']

while True:
    cpuChoice = random.choice(choiceList)
    print("Computer:", cpuChoice)
    userChoice = input("Select R for Rock, P for Papper, S for Scisssors or (end game) \n").lower()
    print("Player:", userChoice)
    if userChoice == "end game":
        print("The game has ended")
        break
    elif userChoice == cpuChoice:
       print("it's a tie! Try again. \n")
    elif userChoice == 'R':
        if cpuChoice == 'p': 
            print('player loose!', cpuChoice, 'beats', userChoice)
        else:
            print("Player Win!", userChoice, "beats", cpuChoice)
    elif userChoice == 'S':
        if cpuChoice == "P":
            print("player loose!", cpuChoice, "beats", userChoice)
        else:
            print("Player Win!", userChoice, "beats", cpuChoice) 
    elif userChoice == 'S':
        if cpuChoice == "R":
            print("player loose!", cpuChoice, "beats", userChoice)
        else:
            print("Player Win!", userChoice, "beats", cpuChoice)
    else:
        print("Choice not in choiceList. TryAgain!")
