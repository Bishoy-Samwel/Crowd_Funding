# import maskpass
from user import User

User.all = User.get_users()
looged_in = User.logged_in

while True:
    if looged_in :
        print("""
                > 3 to sign out
                > 4 to create project
                """)
    else:
        print("""
                > 1 to sign up
                > 2 to sign in
                """)

    x = input('> ').lower()
    if x == 'quit':
        print('Bye!')
        break
    if x == '1':
        User.register()
    if x == '2':
        User.login()
    if x == '3' and looged_in:
        User.logout()
    if x == '4' and looged_in:
        looged_in.create_project()




