#------------------------------------------------------------------------------------------------------------------------------------------------------
#Code By :- Anmol Kumar Srivastava (dArKmOLeS)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Generates, sends and authenticates OTP.
#Using Twilio's API for sending messages.
#------------------------------------------------------------------------------------------------------------------------------------------------------
import random
import string

def otp_generator():
    otp = ''
    for i in range(6):
        random_character = random.choice(string.digits)
        otp += random_character
    return otp

def otp_authenticator(otp, try_number):
    print("Tries left : ",try_number)
    user_input = input("Enter OTP : ")
    if user_input == otp:
        print("OTP Authenticated")
    else:
        if try_number == 1:
            print("Authentication failed")
        else:
            otp_authenticator(otp, try_number - 1)

def set_up():
    from twilio.rest import Client
    account_sid = 'Your Account SID'
    auth_token = 'Twilio Authentication Token'
    client = Client(account_sid, auth_token)
    return client

def send_otp(number, otp, client):
    client.messages.create(
        body='Your One Time Password is : ' + otp,
        from_='Your Twilio Number',
        to='Country Code' + number
    )

while True:
    number = input("Enter your Mobile Number :")
    if len(number) == 10:
        client = set_up()
        otp = otp_generator()
        send_otp(number, otp, client)
        otp_authenticator(otp, 3)
        break
    else:
        print("Enter a Valid Mobile Number.")
