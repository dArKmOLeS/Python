#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                     A random number guesser game
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random
import time
import sys
import pandas
import os

DASH = "-----------------------------------------------------------------------------------------------"


def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def clean_up_code():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        if os.getenv('TERM'):
            _ = os.system('clear')


def typing(message):
    for char in message:
        sys.stdout.write(char)
        time.sleep(0.1)
    print()


def is_integer(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def welcome():
    message = color_text("WELCOME TO THE NUMBER GUESSER GAME", "1;31")
    typing(message)
    print()
    print(color_text(DASH, "1;35"))


def print_instructions():
    instructions = (
        "Welcome to the Number Guesser Game!\n"
        "1. You will choose a difficulty level, or set a custom range.\n"
        "2. The computer will select a random number within this range.\n"
        "3. Your task is to guess this number in the fewest tries possible.\n"
        "4. Follow the hints to guess higher or lower.\n"
        "Good luck!"
    )
    print(color_text(instructions, "1;36"))
    print(DASH, "1;35")


def users_data(user_count):
    users = []
    print("User Registration...")
    print(color_text(DASH, "1;35"))
    i = 1
    while i <= user_count and user_count > 1:
        print("User ", i, " : ")
        user = input("Enter InGame name : ")
        if user not in users:
            users.append(user)
        else:
            print("Name already taken...")
            i -= 1
        i += 1
    if user_count == 1:
        user = input("Enter InGame name : ")
        users.append(user)
    print(color_text(DASH, "1;35"))
    clean_up_code()
    difficulty_setter(users)


def difficulty_setter(users):
    difficulty_list = ["Easy", "Medium", "Hard", "Custom"]
    print("Difficulty Level :-")
    while True:
        print("Press 1 for Easy (0 - 10).")
        print("Press 2 for Medium (0 - 50).")
        print("Press 3 for Hard (0 - 100).")
        print("Press 4 for Custom.")
        user_difficulty_choice = input("Enter your choice : ")
        bool_ = is_integer(user_difficulty_choice)
        if bool_:
            user_difficulty_choice = int(user_difficulty_choice)
            if user_difficulty_choice in [1, 2, 3, 4]:
                difficulty_level = difficulty_list[user_difficulty_choice - 1]
                print(color_text(DASH, "1;35"))
                print("Difficulty level set to - ", difficulty_list[user_difficulty_choice - 1])
                print(color_text(DASH, "1;35"))
                break
            else:
                print("Invalid choice! Please enter valid choice.")
        else:
            print("Only Numeric Inputs Allowed...")
            print(color_text(DASH, "1;35"))
    numbers_generator(users, difficulty_level)


def numbers_generator(users, difficulty_level):
    numbers = []
    lower = 0
    if difficulty_level == "Easy":
        possible_list = list(range(11))
        upper = 10
    elif difficulty_level == "Medium":
        possible_list = list(range(51))
        upper = 50
    elif difficulty_level == "Hard":
        possible_list = list(range(101))
        upper = 100
    else:
        while True:
            lower = input("Enter the Lower Limit of numbers : ")
            bool_1 = is_integer(lower)
            if bool_1:
                while True:
                    upper = input("Enter the Upper Limit of numbers : ")
                    bool_2 = is_integer(upper)
                    if bool_2:
                        lower = int(lower)
                        upper = int(upper)
                        possible_list = list(range(lower, upper + 1))
                        break
                    else:
                        print("Only Numeric Inputs Allowed...")
                break
            else:
                print("Only Numeric Inputs Allowed...")
    for _ in range(len(users)):
        numbers.append(random.choice(possible_list))
    input("Press Enter to continue...")
    clean_up_code()
    game(users, numbers, lower, upper)


def game(users, numbers, lower, upper):
    message = color_text("The Game is Starting...", "1;32")
    print(color_text(DASH, "1;35"))
    typing(message)
    print(color_text(DASH, "1;35"))
    print()
    points = []
    for i in range(len(users)):
        lower_copy = lower
        upper_copy = upper
        if len(users) > 1:
            well = users[i] + "'s turn :- "
            print(color_text(well, "1;34"))
        random_number = numbers[i]
        point = 1
        while True:
            print("Enter your choice (", lower_copy, "-", upper_copy, ") : ")
            users_choice = input()
            bool_ = is_integer(users_choice)
            if bool_:
                users_choice = int(users_choice)
                if users_choice in range(lower_copy, upper_copy + 1):
                    if users_choice > random_number:
                        upper_copy = users_choice - 1
                        print("Enter a lower number...")
                    elif users_choice < random_number:
                        lower_copy = users_choice + 1
                        print("Enter a higher number...")
                    else:
                        print("That's a hit...")
                        print("You took ", point, " turn to hit the number...")
                        points.append(point)
                        input("Press Enter to continue...")
                        clean_up_code()
                        break
                    point += 1
                else:
                    print("Invalid choice...")
            else:
                print("Only Numeric Inputs Allowed...")
                print(color_text(DASH, "1;35"))
        print(color_text(DASH, "1;35"))
    result(users, numbers, points)


def exit_code():
    print(color_text(DASH, "1;35"))
    message = color_text("Exiting Game...", "1;31")
    typing(message)
    print()
    clean_up_code()
    print("Good Bye, Come Back Soon.")
    sys.exit()


def more_round(users):
    print("One more round???")
    while True:
        print("Press 1 for Another round (same players).")
        print("Press 2 for Another round (new players).")
        print("Press 3 to Exit.")
        choice = input("Enter your choice : ")
        bool_ = is_integer(choice)
        if bool_:
            choice = int(choice)
            if choice in [1, 2, 3]:
                if choice == 1:
                    difficulty_setter(users)
                elif choice == 2:
                    main()
                else:
                    exit_code()
            else:
                print("Invalid Choice!!!")
        else:
            print("Only Numeric Inputs Allowed...")
            print(color_text(DASH, "1;35"))


def result(users, numbers, points):
    result_list = {"Player_Name": users, "Numbers": numbers, "Tries_Taken": points}
    dataframe = pandas.DataFrame(result_list)
    message = color_text("Preparing results...", "1;32")
    typing(message)
    print()
    print(color_text(DASH, "1;35"))
    print("___Points Table___")
    print(color_text(DASH, "1;35"))
    print(dataframe)
    print(color_text(DASH, "1;35"))
    if len(users) > 1:
        winner_dec(users, points)
    else:
        more_round(users)


def winner_dec(users, points):
    if len(users) > 1:
        min_number = min(points)
        winners = points.count(min_number)
        if winners == 1:
            min_index = points.index(min_number)
            print("The Winner of this round is : ", users[min_index], " with only ", points[min_index], " tries.")
            print(color_text(DASH, "1;35"))
        else:
            min_indexes = []
            for i in range(len(points)):
                if min_number == points[i]:
                    min_indexes.append(i)
            print("The match is a tie between ", winners, "players.")
            print(color_text(DASH, "1;35"))
            print("The Winners of this round are : ")
            for i in min_indexes:
                print(users[i])
            print(color_text(DASH, "1;35"))
            print("They all took ", min_number, " tries.")
            print(color_text(DASH, "1;35"))
    more_round(users)


def main():
    user_count = input("Enter the total number of players : ")
    bool_ = is_integer(user_count)
    if not bool_:
        print("Only Numeric Inputs allowed...")
        print(color_text(DASH, "1;35"))
        main()
    else:
        user_count = int(user_count)
        if user_count < 0:
            print("Invalid choice!!!")
            print(color_text(DASH, "1;35"))
            main()
        elif user_count == 0:
            print("At least 1 Player needed to start!!!")
            print(color_text(DASH, "1;35"))
            main()
        elif user_count == 1:
            print("Starting in solo mode...")
            print(color_text(DASH, "1;35"))
            users_data(user_count)
        else:
            users_data(user_count)


if __name__ == "__main__":
    welcome()
    print_instructions()
    main()
