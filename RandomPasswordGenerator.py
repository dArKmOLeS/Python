#Random Password Generator in python (terminal based)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#In this program, i have created a random password generator, 
#that allows the user to select which characters he/she wants to include and then 
#generate a list of 5 passwords from which he chooses a final password
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random
import string

def passwordGenerator(length,characters):
    passwords = []
    all_characters = ''
    for i in characters:
        all_characters += i
    for i in range(5):
        password = ''
        for j in range(length):
            random_character = random.choice(all_characters)
            password = password + random_character
        passwords.append(password)
    return passwords

length = int(input("Enter the length of Password : "))
characters = []
choices = []
valid_choices = ['YES','yes','Yes','yEs','yeS','YEs','yES','YeS','NO','no','No','nO']
questions = ["Include Lowercase characters (Yes/No): ","Include Uppercase characters (Yes/No): ","Include Digits (Yes/No): ","Include Punctuations (Yes/No): "]

for i in range(4):
    while True:
        answer = input(questions[i])
        if answer in valid_choices:
            choices.append(answer)
            break
        else:
            print("Invalid choice!")

if choices[0] in valid_choices[:8]:
    characters.append(string.ascii_lowercase)
if choices[1] in valid_choices[:8]:
    characters.append((string.ascii_uppercase))
if choices[2] in valid_choices[:8]:
    characters.append(string.digits)
if choices[3] in valid_choices[:8]:
    characters.append(string.punctuation)
else:
    while True:
        choice2 = input("Include @ (Yes/No): ")
        if choice2 in valid_choices[:8]:
            characters.append('@')
            break
        elif choice2 not in valid_choices:
            print("Invalid choice!")

passwords = passwordGenerator(length,characters)
counter = 1

for i in passwords:
    print("password ",counter," : ",i)
    counter += 1

while True:
    choice = int(input("Choose final password (1-5): "))
    if choice in range(1,6):
        final_password = passwords[choice - 1]
        print("the final password is : ",final_password)
        break
    else:
        print("Invalid choice!")
