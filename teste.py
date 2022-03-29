from re import search


def email_is_true(email):
    regex = r'^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not search(regex, email):
        raise ValueError("Invalid email")
    return email

a = email_is_true('vih-reis@hotmail.com')
print(a)
