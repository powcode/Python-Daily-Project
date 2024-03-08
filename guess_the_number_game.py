import random 
import string

# convert numbers to array list
number = [n for n in string.digits]
isTrue = True

# looping while playing
while isTrue :
    guess_number = input("Guess the number 0-9 : ")
    
    # if user input a number other than 0-9
    if guess_number not in number :
        print("Please enter the number from 0-9")
    
    # if the user number is same as the random selection number
    elif guess_number == random.choice(number) :
        print("Good, you guess the number")
    
    # if the user number is not same as the random selection number
    else :
        print("OOPPSS!! You're wrong")
    
    again = True
    # looping for play again
    while again :
        again = input("Wanna play again?(y/n) : ")
        # if the user wants to play again
        if again == 'y':
            again = False
        
        # if the user doesn't want to play again
        elif again == 'n':
            again = False
            isTrue = False
            print("Thanks for playing")
        
        # if the user input something other than y or n
        else :
            print("Please input 'y' or 'n")
        
    
    
    
    
    