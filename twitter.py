import re
#importing the regular expressions library to allow us to use regular expressions

twitter = input("Enter your Twitter username: ")
pattern = r"@(\w+)"
match = re.search(pattern, twitter)
#prompt the user to input their username and match our regular expression with their input

if match:
    print("Your username {} is a valid username.".format(twitter))
else:
    new = input("invalid username, Would you like to change your username to a suitable one? (y/n): ")
    if new == 'y':
        creation = input("Create a new username that matches the @username format: ")
        pattern = r"@(\w+)"
        new_match = re.search(pattern, creation)
        if new_match:
            print("Your username has been changed to {} and it is valid".format(creation))
        else:
            print("the new username is invalid too")
    elif new == 'n':
        print("Your username will not change.")
    else: 
        print("Invalid selection.")
#if statement that checks if it matches and if it does not it prompts the user to change their username