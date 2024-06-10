#Random Password Generator with Streamlit for frontend
#-----------------------------------------------------------------------------------------------------

import streamlit as stm
import random
import string

stm.title("Password-Generator")

def passwordGenerator(length, characters):
    passwords = ['','','','','']
    all_characters = ''
    for i in characters:
        all_characters += i
    for i in range(5):
        password = []
        for j in range(len(characters)):
            random_character = random.choice(characters[j])
            password.append(random_character)
        for j in range(length-len(characters)):
            random_character = random.choice(all_characters)
            password.append(random_character)
        random.shuffle(password)
        for j in range(length):
            passwords[i] += password[j]
    return passwords

length = stm.slider("Length of Password?",0,20,4)

if length < 4:
    stm.write("Minimum Password length should be 4.")
else:
    characters = []
    choices = []

    col1, col2 = stm.columns(2)

    with col1:
        lower = stm.checkbox("Include Lowercase characters")
        punctuation = stm.checkbox("Include Punctuations")

    with col2:
        upper = stm.checkbox("Include Uppercase characters")
        digit = stm.checkbox("Include Digits")

    if (not punctuation):
        symbol = stm.checkbox("Include @")
        if symbol:
            characters.append("@")

    if lower:
        characters.append(string.ascii_lowercase)
    if upper:
        characters.append(string.ascii_uppercase)
    if digit:
        characters.append(string.digits)
    if punctuation:
        characters.append(string.punctuation)

    if stm.button("Generate Passwords") and (lower or upper or digit or punctuation or symbol):
        passwords = passwordGenerator(length, characters)
        counter = 1
        for i in passwords:
            stm.write("password ", counter, " : ", i)
            counter += 1
    else:
        stm.write("Choose characters.")
stm.divider()
col3, col4 = stm.columns(2)
with col3:
    stm.caption("Creator : Anmol Kumar Srivastava")
with col4:
    stm.caption("Github : dArKmOLeS")
stm.divider()
