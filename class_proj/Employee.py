# class Employee():
#     def emp_id(self):
#         print("emp id 123")
#         print(id(self))
#     def emp_Name(self):
#         print("emp Name Josh")
#         print(id(self))
# e=Employee()
# e.emp_id()
# e.emp_Name()
# print(id(e))
# print("Employee 2.......................")
# e1=Employee()
# print(id(e1))
# e1.emp_id()
# e1.emp_Name()

class Employee():
    def __init__(self):
        print("Contructor")
        print("Git test")
    def emp_id(self,emp_id):
        print("emp id",emp_id)
        print(id(self))
    def emp_Name(self,emp_name):
        print("emp Name Josh", emp_name)
        print(id(self))
e=Employee()
e.emp_id("johan")
e.emp_Name(123)
print(id(e))
print("Employee 2.......................")
# e1=Employee()
# print(id(e1))
# e1.emp_id()
# e1.emp_Name()