class Employee():
    name="Ben"
    department="Sales"
    starting_year=2020
    salary=5000
    def __init__(self, name, department, starting_year,salary):
      self.name = name
      self.department = department
      self.starting_year=starting_year
    
    
    
my_object=Employee()
employe1=Employee("Ben","test",2022,50000)

#constructor for is __init__ the creater 
def printer(a):
    print(a.name)
    print(a.department)
    print(a.starting_year)
    print(a.salary)
printer(employe1)
