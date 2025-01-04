# import maskpass
from project import Project
from user import User

User.get_users()
Project.get_projects()


while True:
    logged_in = User.logged_in
    if logged_in :
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
    if x == '3' and logged_in:
        User.logout()
    if x == '4' and logged_in:
        User.create_project()




