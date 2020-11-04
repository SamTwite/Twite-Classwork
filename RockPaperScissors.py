### SRC - This is a good effort and works well
### you do need to add some #endif lines.
from random import randint

#list of choices for computer to choose from
t = ["Rock", "Paper", "Scissors"]

#computer randomly chooses number assigned to t
computer = t[randint(0,2)]

#Create a loop so game can be repeatedly played

loop = False

while loop == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("You choose the same, draw.")
    elif player == "Rock":
        if computer == "Paper":
            print("You lost, Paper beats rock")
        else:
            print("You win, rock beats scissors")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost, Scissors beats paper")
        else:
            print("You won, paper beats rocks")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lost, rock beats scissors")
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    
        
    computer = t[randint(0,2)]
    YorN = input("Do you want to keep playing? (N for No or program continues..): ")
    if YorN == "N":
        loop = True
#end while
        #message printed when game is ended
print("Game ended, thanks for playing!")
