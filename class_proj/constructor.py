# class Employee:
#     def __init__(self):
#         print("Contructor")
#     def __init__(self,name):
#         print("Constructor --------------2")
#     def add(self):
#         print("Add")
# e=Employee("Johan")
# e.add()

class Employee:
    def __init__(self):
        self.phoneNo=859493696
        print("Contructor")

    def __init__(self,id1,name,email):
        self.id11=id1
        self.Name=name
        self.email = email
        print("Constructor --------------2")
    def add(self):
        print(self.Name)
        # print(self.phoneNo)
e=Employee(123,"Johan","johan@gmail.com")
e.add()