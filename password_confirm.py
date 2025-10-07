password = input("Enter a password of at least 7 characters long with one uppercase: ")
valid = 0
is_upper = False
is_alpha = False
is_alphanum = False
is_symbol = False

if len(password) < 7:
    print("password invalid")
else:
    for char in password:
        if char.isupper():
            is_upper = True
        if char.isalnum():
            is_alphanum = True
        if char.isalpha():
            is_alpha = True
        if not char.isalpha():
            is_symbol = True

    if is_upper and is_alpha and is_alphanum and is_symbol:
        print("Password valid")
    else:
        print("Password invalid")