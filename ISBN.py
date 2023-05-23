import re
isbn = input("enter an isbn number")
pattern = r"ISBN \d{3}-\d-\d{3}-\d{5}-\d"
match = re.search(pattern, isbn)
if match:
    print("{} is a valid isbn number".format(isbn))
else:
    print("{} is an invalid isbn number".format(isbn))