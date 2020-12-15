#Method overloading
print ("Method overloading")
class Employee:
    def emp_id(self, a=None, b=None):
        print(a,b)
e=Employee()
e.emp_id()
e.emp_id(21)
e.emp_id(a=22)
e.emp_id(b=23)
e.emp_id(a=22, b=24)
#Overridding
print("Method Overridding")
class Car:
    def power(self):
        print("5000 CC")
    def gear(self):
        print("Automatic")
class maruti(Car):
    def power(self):
        print("8000 CC")
    def model(self):
        print("SUV")
m=maruti()
m.power()
m.gear()
m.model()