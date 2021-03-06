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

def average_age(person_list, c_year):
    sum_age = 0
    for p in person_list:
        sum_age += p.age(c_year)
    return sum_age/float(len(person_list))
