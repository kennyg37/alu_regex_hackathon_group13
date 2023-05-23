import re
movi_n = input("Input any movie to validate:")
pattern = r"^.*?\s\(\d{4}\)$"
match = re.search(pattern, movi_n)
if match:
    print("{} is a real movie title".format(movi_n))
else:
    print(" {} is not a valid movie title".format(movi_n))

