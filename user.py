from logging import exception
import json

from input_handler import check_valid_input
from validation import validate_name, validate_email, validate_pswd, validate_pswd_conf, validate_phone, password, \
    validate_input


class User:
    logged_in = None
    all = {}
    def __init__(self, first_name, last_name, phone, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.activated = False

    @staticmethod
    def login():
        while True:
            email = check_valid_input('> What is your email? ', validate_email, 'email')
            password = check_valid_input('> What is your password? ', validate_input, 'input')
            user = User.all[email]
            if user and user['password'] == password:
                if not user['activated']:
                    user['activated'] = True
                    User.save_user(user)
                    print("Account activated")
                User.logged_in = user
                break

    def logout(self):
        User.logged_in = None

    @classmethod
    def save_user(self, user):
        print(user.__dict__)
        User.all = User.get_users()
        User.all[user.email]= user.__dict__
        try:
            user_file_obj = open('users.json', 'w')
        except exception as e:
            print(e)
            return False
        else:
            json.dump(User.all, user_file_obj, indent=4)
            user_file_obj.close()
            return True

    @classmethod
    def find_user(cls, email, password):
        pass

    @classmethod
    def get_users(self):
        try:
            user_file_obj = open('users.json', 'r').read()
            user_list = json.loads(user_file_obj)
        except Exception as e:
            return {}
        else:
            return user_list

    @classmethod
    def register(cls):
        f_name = check_valid_input('> What is your first name? ', validate_name, 'name')
        l_name = check_valid_input('> What is your last name? ', validate_name, 'name')
        email = check_valid_input('> What is your Email? ', validate_email, 'email')
        password = check_valid_input('> Enter a password! ', validate_pswd, 'password')
        password_confirm = check_valid_input('> Confirm the password! ', validate_pswd_conf,
                                             'password_confirm')
        phone = check_valid_input('> What is your (EG) phone number? ', validate_phone, 'phone')
        u = User(f_name, l_name, phone, email, password)
        User.save_user(u)