class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def display(self):
        print("Employee ID:",self.emp_id)
        print("Name:",self.name)
        print("Salary:",self.salary)
    def __del__(self):
        print("Employee object deleted:",self.emp_id)

e1 = Employee(101,"Riddhi",50000)
e2 = Employee(102,"Priya",60000)
e1.display()
e2.display()
del e1
del e2