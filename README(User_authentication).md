User Sign-Up and Log-In System
-This Python project provides a console-based system for user sign-up, log-in, and password management. 
-It includes features like password hashing, security code generation, and input validation to ensure secure and user-friendly interaction.

Table of Contents
-Features
-Requirements
-Installation
-Usage
-Code Explanation
-Contributing
-License
-Contact

Features
-User Registration: Allows new users to sign up by providing their email, username, password, name, and date of birth.
-Password Hashing: Uses bcrypt for secure password hashing.
-Log-In: Users can log in using their username and password.
-Password Recovery: Users can recover their password using a security code.
-Input Validation: Validates email, password, and date of birth formats.
-Console Interface: Interactive and user-friendly console interface.
-Data Persistence: User data is saved to and read from a text file.

Requirements
-Python 3.x
-pandas
-bcrypt

You can install the required Python packages using:
-pip install pandas bcrypt

Installation
-Clone the repository
-Navigate to the project directory
-Install dependencies

Usage
-Edit the file path: Replace the file_path variable in the code with the path to your text file for saving user data.
-python: file_path = "your_text_file_path.txt"
-Run the script: python user_signup_login.py
-Follow the console instructions to sign up, log in, or recover your password.

Code Explanation
The script user_signup_login.py contains the following functions:
-import_saved_data: Reads user data from the specified text file and loads it into a DataFrame.
-hash_passwd: Hashes the password using bcrypt.
-security_word: Generates an 8-character security word for password recovery.
-clean_up_code: Clears the console screen.
-is_integer: Checks if a user input is an integer.
-valid_email: Validates the email format.
-valid_passwd: Validates the password format based on defined rules.
-valid_dob: Validates the date of birth format.
-get_email: Prompts the user to enter an email.
-get_username: Prompts the user to enter a unique username.
-confirm_password: Confirms the password entered by the user.
-get_password: Prompts the user to enter a valid password.
-get_dob: Prompts the user to enter a date of birth.
-generate_db_string: Collects user information and generates a string to save in the text file.
-color_text: Adds color to the text for console output.
-welcome: Displays the welcome message and starts the main menu.
-update_password: Updates the user's password in the text file.
-forgot_password: Handles the password recovery process.
-authenticate: Authenticates the user's log-in credentials.
-sign_up: Handles the user registration process.
-log_in: Provides options for log-in or password recovery.
-main: Displays the main menu for sign-up, log-in, or exit.

Contributing
-Contributions are welcome! If you have any ideas, feel free to open an issue or submit a pull request.

License
-This project is licensed under the MIT License. See the LICENSE file for details.

Contact
-GitHub: dArKmOLeS
-Email: anmolsrivas2803@gmail.com
