# Guess a number from 1 to 6 Game 

from random import randint                              #import randint function from random module to generate random numbers.

randomNumber = randint(1,6)                             #generate a random number from 1 to 6

for x in range(3,0,-1):                                 #use for loop to give user 3 chances
    
    print(f"***You have {x} chances remaining***")
    num = int(input("Enter a number from 1 to 6 : "))   #getting value from user
    
    if num == randomNumber:                             #checking if the user value is equal to the generated number
        print ("You win!!")
        break                                           #if the numbers match the loop will break
    else:
        print ("You lose!!")
    
    
print("The number was : ", randomNumber)                #at the end the random number will be shown
