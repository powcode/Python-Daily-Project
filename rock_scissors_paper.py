import random

data = ["rock", "scissors", "paper"]
isTrue = True

while isTrue:
    computer = random.choice(data)
    player = input("Choose rock scissors or paper : ").lower()
    if player not in data:
        print("Please input 'rock', 'scissors', or 'paper'")
    elif player == computer :
        print("Draw")
    elif player == "rock" and computer == "scissors" :
        print(f'You Win, computer choose {computer}')
    elif player == "rock" and computer == "paper" :
        print(f'You Lose, computer choose {computer}')
    elif player == "scissors" and computer == "rock" :
        print(f'You Lose, computer choose {computer}')
    elif player == "scissors" and computer == "paper" :
        print(f'You Win, computer choose {computer}')
    elif player == "paper" and computer == "rock" :
        print(f'You Win, computer choose {computer}')
    elif player == "paper" and computer == "scissors" :
        print(f'You Lose, computer choose {computer}')
    
    again = True
    while again:
        again = input("Wanna Play Again?(y/n) : ").lower()
        if again == "y" :
            again = False
        elif again == "n" :
            again = False
            isTrue = False
            print("Thanks for playing")
        else : 
            print("Please Input y or n")
    
