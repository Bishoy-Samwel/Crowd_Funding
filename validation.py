import re
from curses.ascii import isalpha

password = ''
msg_dict = {
    'input': 'You entered an empty input string.!',
    'name': 'Enter a valid name!',
    'email': 'Enter a valid email!',
    'password': 'Enter a stronger password!',
    'password_confirm': 'Password confirmation doesn\'t match!',
    'phone': 'Enter a valid egyptian phone number!'
}

def validate_input(input):
    return len(input.strip()) > 0

def validate_name(name):
    return name.isalpha()

def validate_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def validate_phone(phone):
    return bool(re.match(r'^01[0-2][0-9]{8}$', phone))
    pass

def validate_pswd(pswd):
    pattern = r'^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).{6,}$'
    valid =  bool(re.match(pattern, pswd))
    global password
    if (valid): password = pswd; return valid

def validate_pswd_conf(pswd):
    return pswd == password

