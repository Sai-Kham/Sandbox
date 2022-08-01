MINIMUM_LENGTH=4
password = input("Enter password of at least 4 characters :")
while len(password) < MINIMUM_LENGTH:
    print("Password does not meet requirements")
    password = input("Enter password of at least 4 characters :")
print ("*" * len(password))
