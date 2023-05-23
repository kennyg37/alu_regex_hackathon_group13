import re 
ip_adress = input("enter your ip adress:")
pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
match = re.search(pattern, ip_adress)
if match:
    print("this ip adress is valid")
else:
    print("this function is invalid")