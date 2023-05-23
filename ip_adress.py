import re 
#importing the re module to allow us to use regular expressions in our code

ip_adress = input("enter your ip adress:")
pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
match = re.search(pattern, ip_adress)
# we then get an input and a pattern, then match the input and regular expression

if match:
    print("this ip adress is valid")
else:
    print("this function is invalid")
#we then use an if statement to evaluate and decide what our program prints in every case