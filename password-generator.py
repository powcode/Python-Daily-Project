import string 
import random

# get password length from user input
length = int(input("Enter password length :"))
characters = ""



print(""" 
Choice password criteria 
1. iclude alphabeth
2. include number
3. inlcude speacial characters
4. exit
               """)
while(True):
    choice = int(input("Enter password criteria : "))
    if choice not in [1,2,3,4] :
        print("Please enter a valid number")
        continue
    elif choice == 1 :
        # adding alphabet to characters
        characters += string.ascii_letters
    elif choice == 2 :
        #adding number to characters
        characters += string.digits
    elif choice == 3 :
        # adding special char to characters
        characters += string.punctuation
    else :
        # break the while loop
        break


password = []
# looping for each character and add it to list
for i in range(length):
    # get the random char from characters
    random_char = random.choice(characters)
    # add the random char to password 
    password.append(random_char)

# convert the array to string
password = "".join(password)

    

