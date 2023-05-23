import re
#we import the re module to hallow us to use the vast library of regular expressions

isbn = input("enter an isbn number")
pattern = r"ISBN \d{3}-\d-\d{3}-\d{5}-\d"
match = re.search(pattern, isbn)
#we then get an inpurt from the user and match it with our regular expression

if match:
    print("{} is a valid isbn number".format(isbn))
else:
    print("{} is an invalid isbn number".format(isbn))
#after we then use an if statement to give the program the last say to what gets printed in every case