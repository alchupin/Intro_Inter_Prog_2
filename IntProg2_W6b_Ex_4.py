class Person:
    def __init__(self, name1, name2, year):
        self.first_name = name1
        self.last_name = name2
        self.birth_year = year
    def full_name(self):
        return(self.first_name + ' ' + self.last_name)
    def age(self, c_year):
        return c_year - self.birth_year
    def __str__(self):
        return('First name: ' + self.first_name +
               '. Last name: ' + self.last_name +
               '. Year of birh: ' + str(self.birth_year))

class Student:
    def __init__(self, person, pwd):
        self.person = person
        self.password = pwd
        self.projects = []
    def get_name(self):
        return person.full_name()
    def check_password(self, pss):
        return self.password == pss
    def get_projects(self):
        return self.projects
    def add_projects(self, project_name):
        self.projects.append(project_name)
    
def assign(students, name, pwd, project):
    for stud in students:
        if name == stud.get_name() and stud.check_password(pwd) and project not in stud.get_projects():
            stud.add_projects(project)
            
