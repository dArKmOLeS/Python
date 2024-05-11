OTP Generator and Authenticator using Twilio's API

This Python script generates, sends, and authenticates one-time passwords (OTPs) using Twilio's API for sending messages. OTPs are commonly used for two-factor authentication (2FA) to verify user identities securely.

Features:
Generates a random 6-digit OTP using numeric characters.
Sends the OTP via SMS to the provided mobile number using Twilio's messaging service.
Allows the user to authenticate by entering the received OTP within three attempts.
Utilizes recursive function for OTP authentication with limited attempts.
Ensures input validation for the mobile number format.

Prerequisites:
Twilio Account SID and Authentication Token:
You need to sign up for a Twilio account and obtain your Account SID and Authentication Token from the Twilio Console.
Twilio Phone Number:
Use a Twilio phone number with SMS capabilities to send OTP messages.

Installation:
Install the required Python packages:
pip install twilio
Replace 'Your Account SID' and 'Twilio Authentication Token' with your Twilio credentials.
Replace from_='Your Twilio Number' with your Twilio phone number.
Replace 'Country code with the specific country code where the message is to be sent

Usage:
Run the script and enter a valid 10-digit mobile number when prompted.
Check your mobile device for the OTP sent via SMS.
Enter the received OTP for authentication within three attempts.

Example:
python otp_generator.py

Note:
Ensure that your Twilio account has sufficient balance to send SMS messages.
Customize the message body or OTP length as per your requirements.
Feel free to fork the repository, contribute improvements, or report issues.

Author: [Anmol Kumar Srivastava]
GitHub Repository: [https://github.com/dArKmOLeS/Python]
