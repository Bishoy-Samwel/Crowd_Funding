import json

from input_handler import check_valid_input
from validation import validate_input, validate_number, validate_date


class Project:
    all = {}
    def __init__(self, title, details, target, start_date, end_date, email):
        self.title = title
        self.details = details
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
        self.email = email

    @staticmethod
    def create_project(email):
        title = check_valid_input('> What is the title? ', validate_input, 'input')
        details = check_valid_input('> What are the details? ', validate_input, 'input')
        target = check_valid_input('> What is the total target? ', validate_number, 'number')
        start_date = check_valid_input('> What is the start date? ', validate_date, 'date')
        end_date = check_valid_input('> What is the end date? ', validate_date, 'date')
        p = Project(title, details, target, start_date, end_date, target, email)
        Project.all[p.title] = p.__dict__
        Project.update_projects_data()
        pass

    @staticmethod
    def get_projects():
        try:
            project_file_obj = open('projects.json', 'r').read()
            Project.all = json.loads(project_file_obj)
        except Exception as e:
            return {}
        else:
            return Project.all


    @staticmethod
    def update_projects_data():
        try:
            project_file_obj = open('projects.json', 'w')
        except Exception as e:
            print(e)
            return False
        else:
            json.dump(Project.all, project_file_obj, indent=4)
            project_file_obj.close()
            return True

    @staticmethod
    def view_projects():
        print (Project.all)

    @staticmethod
    def delete_project(user_email):
        title = input('> What is the title? ')
        if Project.all[title]['email'] == user_email:
            if Project.all[title]:
                Project.all.pop(title, None)
                Project.update_projects_data()
            print('Project is deleted')
        else:
            print('You are not allowed to delete this project')
        pass

    @staticmethod
    def update_project(user_email):
        title = input('> What is the title? ')
        if Project.all[title]['email'] == user_email:
            if Project.all[title]:
                keys = ['title', 'details', 'target', 'start_date', 'end_date']
                for i, key in enumerate(keys):
                    print(f'{i} to edit {key}')
                x  = int(input('> '))
                val = input(f'> Enter the new {keys[x]}! ')
                Project.all[title][keys[x]] = val
                Project.update_projects_data()
                print('Project is updated')
        else:
            print('You are not allowed to update this project')
        pass

    @staticmethod
    def search_project(self):
        pass