#Instance Method
# class Employee:
#     def __init__(self):
#         self.a = 10
#     def emp_id(self):
#         self.empid=897
#         print(self.a)
#         print("Emp id is",self.empid)
#     def emp_name(self):
#         self.emp_id()
#         self.name="Johan"
#         print("Emp name is",self.name)
# e=Employee()
# e.emp_id()
# e.emp_name()
# print(e.a)
# Class Method
# class Employee:
#     roll_no=1
#     def __init__(self):
#         self.a=10
#     @classmethod
#     def emp_id(cls):
#         print(Employee.roll_no)
#         cls.empid=897
#         print("Emp id is",cls.empid)
#     @classmethod
#     def emp_name(cls):
#         cls.emp_id()
#         cls.name="Johan"
#         print("Emp name is",cls.name)
#
# Employee.emp_id()
# Employee.emp_name()
# print(Employee.roll_no)

#Static method
class Employee:
    roll_no=1
    def __init__(self):
        self.a = 10
    @staticmethod
    def emp_id():
        empid=897
        # print(a)
        print("Emp id is",empid)
    @staticmethod
    def emp_name():
        Employee.emp_id()
        print(Employee.roll_no)
        name="Johan"
        print("Emp name is",name)

Employee.emp_id()
Employee.emp_name()
# print(Employee.a)
print(Employee.roll_no)



