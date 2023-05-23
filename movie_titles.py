import re
# we import the re module to allow us to use regular expressions

movi_n = input("Input any movie to validate:")
pattern = r"^.*?\s\(\d{4}\)$"
match = re.search(pattern, movi_n)
#then match the input by the user with the regular expression
if match:
    print("{} is a real movie title".format(movi_n))
else:
    print(" {} is not a valid movie title".format(movi_n))

""" use the if statement to print out an affirmative text in case the regular expression matched and
the otherwise if it did not"""
