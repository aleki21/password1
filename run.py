#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import random

def create_account(user_name,password):
    new_user = User(user_name,password)
    return new_user

def save_user(User):
    User.save_user()

def dlt_account(User):
    User.delete_user()

def create_credentials(application_name,username,password):
    new_credentials = Credentials(application_name,username,password)
    return new_credentials

def save_credentials(Credentials):
    Credentials.save_credentials()

def delete_credentials(Credentials):
    Credentials.delete_credentials()

def display_credentials():
    return Credentials.display_credentials

def main():
    print("Hello, welcome to your future Password Manager")
    print("Create a new user name")
    user_name = input()
    print("Input a login password of your choice")
    login_password = input()
    print(f"Welcome {user_name}.Your password is {login_password}")

    while True:
        print("Use the following short codes to operate: nc - create new credentials, dc - Display credentials, xc - delete credentials, cls - exit password Locker. ")
        short_code = input().lower()

        if short_code == 'nc':
            print("New Account Credentials")
            print("-"*10)

            print ("Application Name")
            application_name = input()

            print("Your user name on the above application? You can create a new user name if you don't have one already.")
            username = input()

            print("Would you like to generate Account password (y/n)")
            answer = input().lower()
            if answer =='y':
                chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
                number = 0
                length = input('password length?')
                plength = int(length)
                password = ''
                for password in range(number):
                    for chars in range(plength):
                        password =+ random.choice(chars)
                    break
            elif answer == 'n':
                print("Input Account password of your choice")
                password = input()

            save_credentials(create_credentials(application_name,username,password))
            print ('\n')
            print(f"New Credentials for {application_name}, user {username}, have been created")
            print ('\n')

        elif short_code == 'dc':
            print("These are the available credentials under your account")
            print('\n')

            for credentials in Credentials.display_credentials():
                print(f" Application name: {application_name}\n Username: {username} \n Password: {password}")
                print('\n')
                print('\n')
                break
            else:
                print("There are no saved credentials for this account")


        elif short_code == "xc":
            print("Which application details would you like to delete?")
            deleteCredentials = input()
            if deleteCredentials == application_name:
                delete_credentials(credentials)
                print("Credentials deleted")
            elif deleteCredentials != application_name:
                print("Sorry, no application credentials matches that name")

        elif short_code == "cls":
                print("Password locker, Security you can trust!")
                break

        else:
            print("Please use the short codes provided")    


if  __name__ == '__main__':

    main()
