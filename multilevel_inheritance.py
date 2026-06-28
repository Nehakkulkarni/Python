class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self,name,age,emp_id,dept):
        super().__init__(name,age)
        self.emp_id = emp_id
        self.dept = dept
class Manager(Employee):
    def __init__(self,name,age,emp_id,dept,team):
        super().__init__(name,age,emp_id,dept)
        self.team = team

m = Manager("Priya",30,100,"IT",5)
print(m.name,m.team)