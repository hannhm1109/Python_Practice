class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,first,last,pay, employees = None):
        super().__init(first, last, pay)
        if employees is None:
            self.employees = []    
        else :
            self.employees == employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Han', 50000,'Python')
dev_2 = Developer('Hanane', 60000, 'Java')

print(Employee.num_of_emps)

emp_1 = Employee('Han', 'Nah', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)


mgr_1 = Manager('Han','Smith', 90000,[dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()


