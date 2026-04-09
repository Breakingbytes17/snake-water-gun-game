
'''
1 for snake
-1 for water
0 for gun'''
import random
computer=random.choice([-1,0,1])
youstr=input("Enter your choice (r/p/s): ")
youDict={"r":1,"p":-1,"s":0}
reverseDict={1:"rock",-1:"paper",0:"scissors"}

you=youDict[youstr]
#by now we have 2 numbers computer and you
print(f"computer choice is {reverseDict[computer]}")
print(f"your choice is {reverseDict[you]}")
if computer==you:
    print("tie")
else:
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("Computer wins!")
    elif(computer==1 and you==-1):
        print("Computer wins!")
    elif(computer==1 and you==0):
        print("You win!")
    elif(computer==0 and you==-1):
        print("You win!")
    elif(computer==0 and you==1):
        print("Computer wins!")
    else:
     print("Something went wrong")
 
           