# parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def print_name(self):
        print(self.firstname, self.lastname)
        
x = Person("John", "Doe")
x.print_name()

# child class
class Student(Person):
    pass

y = Student("Mike", "Olsen")
y.print_name()