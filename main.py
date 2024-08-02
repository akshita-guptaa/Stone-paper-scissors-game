''' 
1 = stone 
0 = paper
-1 = scissors
'''

import random


print(''' 
    Hello! Welcome to the game STONE PAPER SCISSORS.
     Here are the instructions:
            s for Stone 
            p for Paper
            sc for Scissors ''')

comp = random.choice([1, 0, -1])

user_input = input("    Enter your choice: ")
dic={"s": 1,"p":0,"sc":-1}
revdic={1:"Stone",0:"Paper",-1:"Scissors"}

user = dic[user_input]

print(f"    You chose {revdic[user]}\n    Computer chose {revdic[comp]}")


if (comp == user ):
    print("    It's a draw")
else:
    if(comp == -1 and user == 1):
        print("    You Win!")
    elif(comp == -1 and user == 0):
        print("    You Lose!")

    elif(comp == 1 and user == 0):
        print("    You Win!")
    elif(comp == 1 and user == -1):
        print("    You Lose!")

    elif(comp == 0 and user == -1):
        print("    You Win!")
    elif(comp == 0 and user == 1):
        print("    You Lose!")
    else:
        print("    Something went wrong!")
