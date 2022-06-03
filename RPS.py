#using import function
import  random

input("You are welcome to Rock Paper Scissors game! Press enter to countinue \n")

choiceList = ["R", "P", "S"]
userChoice = input("Select R for Rock, P for Papper, S for Scisssors: \n").upper()
game = input("cpu: (cpuChoice), player: (uerChoice) \n")
cpuChoice = random.choiceList()
 
    
if userChoice == choiceList:
    print("you won the game!!!")
#Paper versus Rock
    if userChoice == 'P':
        if cpuChoice == 'R':
            print("you won! Papper cover Rock")
        else:
            print("you lost! Scissor cut Paper")
        
        #Rock versus Scissors
        if userChoice == 'R':
            if cpuChoice == 's':
                print("You won! Rock smashes Scissors")
            else:
                print("You losy! Paper covers Rock")

        #Scissors versus Paper
        if userChoice == 's':
            if cpuChoice == 'p':
                print("You won! Scisors cuts Paper")
            else:
                print("You lot! Rock smashes Scissors")  

    while userChoice not in choiceList:
        userChoice = input("choice not valid. Try again: \n").upper()
        

        while userChoice == cpuChoice:
            print("it's a tie! Try again. \n")
            userChoice = input("Please Try again: \n").upper()
            while userChoice not in choiceList:
                userChoice = input("Invalid choice! Please Try again: \n").upper()

            print("cpu: (cpuChoice), player: (uerChoice) \n")
            
    while True:
        userChoice()
        game = input("Do you want to countine? Y/N")
        game = game.lower().strip()
        if game == 'n':
            break