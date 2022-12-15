class Employee:
    #class variables
    increment = 1.5
    no_of_employees = 0

    #constructor
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.4
        Employee.no_of_employees += 1

    #class fucntion
    def increase(self):
        #self.salary = self.salary * self.increment
        self.salary = self.salary * Employee.increment
    
    #class method
    @classmethod    #decorator
    def change_increment(cls, amount):
        cls.increment = amount

    @property
    def email(self):
        if self.fname == None:
            return 'email not set'   
        else: 
            return self.fname + '.' + self.lname + '@email.com'

    #property decorator
    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

    #class method as alternative constructor
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split('-')
        return cls(fname, lname, salary)

    #static methods
    @staticmethod
    def isopen(day):
        if day == 'sunday':
            return False
        else:
            return True
    
    #dunder method
    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.fname, self.lname, self.salary)

    def __str__(self):
        return 'The name of employee is {}'.format(self.fname)

#inheritance
class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp
    
    def increase(self):
        self.salary = int(self.salary * (self.increment * 0.2))
'''
manish = Employee()
momo = Employee()
manish.fname = 'Manish'
manish.lname = 'Mawatwal'
manish.salary = 100000
'''
'''
print(Employee.__dict__)
manish = Employee('Manish', 'Mawatwal', 100000)
print(manish.__dict__)
print(Employee.no_of_employees)
Employee.change_increment(2)
manish.increase()
print(manish.salary)
'''
'''
momo = Employee.from_str('Momo-Jain-200000')
print(momo.lname)
print(Employee.isopen('sunday'))
'''
'''
vedant = Programmer('vedant', 'rade', 300000, 'Python', '3 yrs')
print(vedant.exp)
help(Programmer)
'''
'''
manish = Employee('manish', 'mawatwal', 900000)
momo = Employee('momo', 'jain', 9)
print(momo+manish)
print(repr(manish))
print(str(manish))
'''
if __name__ == '__main__':
    manish = Employee('manish', 'mawatwal', 900000)
    momo = Employee('momo', 'jain', 9)
    print(manish.email)
    manish.lname = 'abracadabra'
    print(manish.email)
    manish.email = 'manish.mawatwal@gmail.com'
    print(manish.email)
    del manish.email
    print(manish.email)
