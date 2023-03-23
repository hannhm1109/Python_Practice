class Employee:
    def greet(self):
        print("Empolyee Great")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet()