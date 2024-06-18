#--------------------------------------------------------------------------------------------------------------------------
#Anmol Kumar Srivastava (dArKmOLeS)
#--------------------------------------------------------------------------------------------------------------------------
import os
import re
from datetime import datetime
import random
import string
import pandas as pd
import bcrypt

DASH = "-" * 100
RED = "1;31"
GREEN = "1;32"
YELLOW = "1;33"
BLUE = "1;34"
MAGENTA = "1;35"

file_path = "Text file path"


def import_saved_data():
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(color_text("File not found. Please ensure the file exists.", RED))
    except Exception as e:
        print(color_text(f"An error occurred: {e}", RED))
    user_data = []
    for i in lines:
        user = list(i.split(','))
        user_data.append(user)
    df = pd.DataFrame(user_data, columns=['E-mail', 'Username', 'Password', 'Name', 'DOB', 'Security Code'])
    print(df)
    return df


def hash_passwd(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()


def security_word():
    print(color_text("For security purpose, let's add a security word."
                     "\nRemember/Note this security word for future Password Reset.", BLUE))
    print(color_text(DASH, BLUE))
    word = ""
    for i in range(8):
        word += random.choice(string.ascii_uppercase)
    return word


def clean_up_code():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        if os.getenv('TERM'):
            _ = os.system('clear')


def is_integer(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False


def valid_passwd(passwd):
    pattern = (
        r'^(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'(?=.*\d)'
        r'(?=.*[@$!%*?&])'
        r'[A-Za-z\d@$!%*?&]{8,20}$'
    )
    if re.match(pattern, passwd):
        return True
    else:
        return False


def valid_dob(dob):
    format_ = "%d-%m-%Y"
    try:
        datetime.strptime(dob, format_)
        return True
    except ValueError:
        return False


def get_email():
    email = input(color_text("Enter E-Mail Address : ", MAGENTA))
    email = email.lower()
    if valid_email(email):
        return email
    else:
        print(color_text("Please enter a valid E-mail address.", RED))
        get_email()


def get_username(df, key):
    username = input(color_text("Enter Username : ", MAGENTA))
    if username in df:
        print(color_text("Username already taken, please use different username.", RED))
        get_username(df, key)
    else:
        return username


def confirm_password(password):
    confirm_password_var = input(color_text("Enter Password Again : ", MAGENTA))
    if confirm_password_var != password:
        print(color_text("Password Mismatch...\nTry Again.", RED))
        confirm_password(password)


def get_password():
    print(
        color_text(
            "Rules for Strong Password : \n*8-20 letters\n*Must have Uppercase and Lowercase."
            "\n*Must have Digits.\n*Must have symbols.[@_-+.,:;/]", BLUE
        )
    )
    password = input(color_text("Enter Password : ", MAGENTA))
    if valid_passwd(password):
        confirm_password(password)
        return hash_passwd(password)
    else:
        print(color_text("Password conditions not met.\nTry new password.", RED))
        get_password()


def get_dob():
    dob = input(color_text("Enter DOB [DD-MM-YYYY] : ", MAGENTA))
    if valid_dob(dob):
        date, month, year = dob.split('-')
        dob = date + month + year
        return dob
    else:
        print(color_text("Enter a Valid Date.[DD-MM-YYYY]", RED))
        get_dob()


def generate_db_string(df):
    email = get_email()
    username = get_username(df.values, 1)
    password = get_password()
    name = input(color_text("Enter your name : ", MAGENTA))
    dob = get_dob()
    db_string = email + "," + username + "," + password + "," + name + "," + dob
    return db_string


def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def welcome():
    print(color_text("Welcome to SIGN-UP/LOG-IN", GREEN))
    print(color_text(DASH, GREEN))
    main()


def update_password(index, password):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(color_text("File not found. Please ensure the file exists.", RED))
    except Exception as e:
        print(color_text(f"An error occurred: {e}", RED))
    email, username, password_old, name, dob, security = lines[index].split(',')
    database_string = email + "," + username + "," + password + "," + name + "," + dob + "," + security[:8] + "\n"
    lines[index] = database_string
    try:
        with open(file_path, 'w') as file:
            file.writelines(lines)
    except FileNotFoundError:
        print(color_text("File not found. Please ensure the file exists.", RED))
    except Exception as e:
        print(color_text(f"An error occurred: {e}", RED))
    print(color_text("Password Updated Successfully.\n" + DASH, GREEN))
    main()


def forgot_password(df0, df1):
    print(color_text("Password Recovery...\n" + DASH, BLUE))
    username = input(color_text("Enter your Username : ", MAGENTA))
    if username not in df0.values:
        print(color_text("Invalid username.", RED))
        print(color_text(DASH, RED))
        forgot_password(df0, df1)
    else:
        code = input(color_text("Enter your security code to change password : ", MAGENTA))
        code = code.upper()
        index = 0
        for i in df0.values:
            if i == username:
                break
            else:
                index += 1
        stored_code = df1.at[index]
        stored_code = stored_code[:8]
        if stored_code == code:
            password = get_password()
            update_password(index, password)
        else:
            print(color_text("Wrong Security code.\nReturning to Main menu.\n" + DASH, RED))
            main()


def authenticate(usernames, passwords):
    username = input(color_text("Enter your Username : ", MAGENTA))
    if username not in usernames.values:
        print(color_text("Invalid username.", RED))
        print(color_text(DASH, RED))
        authenticate(usernames, passwords)
    else:
        index = 0
        for i in usernames.values:
            if i == username:
                break
            else:
                index += 1
        attempt = 0
        while attempt < 3:
            password = input(color_text("Enter your Password : ", MAGENTA))
            if valid_passwd(password):
                stored_password = passwords.at[index]
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    print(color_text("Log-in Successful.", GREEN))
                    break
                else:
                    print(color_text("Wrong Password.\nAttempt left : " + str(2 - attempt), RED))
                    attempt += 1
            else:
                print(color_text("Invalid Password.", RED))
                attempt += 1
        else:
            print(color_text("Maximum Tries Utilised.\nReturning back to Main Menu.", RED))
            main()


def sign_up(df):
    print(color_text("Welcome to new user registration page.\nLet's start with your Account Setup." + DASH, GREEN))
    database_string = generate_db_string(df)
    key = input(color_text(DASH + "Enter YES to save sign-in data, NO to exit : ", MAGENTA))
    print(color_text(DASH, MAGENTA))
    yes = ["YES", "yes", "Yes", "yEs", "yeS", "YEs", "YeS", "yES"]
    no = ["NO", "no", "No", "nO"]
    if key in yes or key in no:
        if key in yes:
            security = security_word()
            database_string = database_string + "," + security
            print(color_text(DASH, GREEN))
            print(color_text("Your security word is : " + security + DASH, GREEN))
            try:
                with open(file_path, 'a') as file:
                    file.write(database_string + "\n")
            except FileNotFoundError:
                print(color_text("File not found. Please ensure the file exists.", RED))
            except Exception as e:
                print(color_text(f"An error occurred: {e}", RED))
        else:
            print(color_text("Sign-UP Aborted.\nBack to Main Menu." + DASH, RED))
        main()
    else:
        print(color_text("Enter a Valid Choice.", RED))


def log_in(username_df, password_df, security_df):
    print(color_text("Welcome to user log-in page.\n" + DASH, GREEN))
    print(color_text("Press 1 for Log-In form.\n"
                     "Press 2 for Forget Password.\n"
                     "Press 3 to return back to Main Menu.\n"
                     + DASH, BLUE))
    while True:
        choice = input(color_text("Enter your choice : ", MAGENTA))
        print(color_text(DASH, MAGENTA))
        if is_integer(choice) and choice in ["1", "2", "3"]:
            if choice == "1":
                authenticate(username_df, password_df)
            elif choice == "2":
                forgot_password(username_df, security_df)
            else:
                main()
            break
        else:
            print("Enter a valid integer choice...")


def main():
    df = import_saved_data()
    print(color_text("Press 1 for Sign-Up.\nPress 2 for Log-In.\nPress 3 to exit.\n" + DASH, BLUE))
    while True:
        choice = input(color_text("Enter your choice : ", MAGENTA))
        print(color_text(DASH, MAGENTA))
        if is_integer(choice) and choice in ["1", "2", "3"]:
            if choice == "1":
                sign_up(df['Username'])
            elif choice == "2":
                log_in(df['Username'], df['Password'], df['Security Code'])
            else:
                clean_up_code()
                print(color_text("Program Exited Successfully.\nHave a Great Day Ahead.", RED))
                break
            break
        else:
            print(color_text("Enter a valid integer choice...", RED))


welcome()
