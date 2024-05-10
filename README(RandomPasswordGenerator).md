#Random Password Generator in python (terminal based)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#In this program, i have created a random password generator, that allows the user to select which characters he/she wants to include and then 
#generate a list of 5 passwords from which he chooses a final password
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random #to make random choices
import string #to access character strings directly

#function to generate password (length of password and choosen charancters list as arguments)
def passwordGenerator(length,characters):
    passwords = [] #to store all generated passwords in a string
    all_characters = '' #to store allchoosen characters that are to be used
    #add all choosen character strings to the final string
    for i in characters:
        all_characters += i
    #generate 5 random passwords
    for i in range(5):
        password = '' #individual generated password
        #pick random elements from the all characters string
        for j in range(length):
            random_character = random.choice(all_characters)
            password = password + random_character
        passwords.append(password) #add individual generated password to passwords list
    return passwords #return all generated passwords

length = int(input("Enter the length of Password : "))
characters = []
choices = []
#all valid yes/no choices: to process wordplay
valid_choices = ['YES','yes','Yes','yEs','yeS','YEs','yES','YeS','NO','no','No','nO']
#all questons to be asked for character selection
questions = ["Include Lowercase characters (Yes/No): ","Include Uppercase characters (Yes/No): ","Include Digits (Yes/No): ","Include Punctuations (Yes/No): "]

#loop for character inclusion quesstions
for i in range(4):
    while True:
        answer = input(questions[i])
        if answer in valid_choices:
            choices.append(answer)
            break
        else:
            print("Invalid choice!")

#including selected character strings 
if choices[0] in valid_choices[:8]:
    characters.append(string.ascii_lowercase)
if choices[1] in valid_choices[:8]:
    characters.append((string.ascii_uppercase))
if choices[2] in valid_choices[:8]:
    characters.append(string.digits)
if choices[3] in valid_choices[:8]:
    characters.append(string.punctuation)
else: #if no punctuations used, consider '@'? 
    while True:
        choice2 = input("Include @ (Yes/No): ")
        if choice2 in valid_choices[:8]:
            characters.append('@')
            break
        elif choice2 not in valid_choices:
            print("Invalid choice!")

passwords = passwordGenerator(length,characters) #calling method

counter = 1

for i in passwords: #display all generated passwords
    print("password ",counter," : ",i)
    counter += 1

#choose final password
while True:
    choice = int(input("Choose final password (1-5): "))
    if choice in range(1,6):
        final_password = passwords[choice - 1]
        print("the final password is : ",final_password)
        break
    else:
        print("Invalid choice!")
