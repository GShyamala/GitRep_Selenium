def emp_Id():
    print ("Emp Id :",1)

def emp_Name():
    print("Name : ", "Emp1")
emp_Id()
emp_Name()

def bird_features(*color):
    print ("Birds color is", color)
bird_features("White", "Green","Yellow","Blue")

a=200
def calculator():
    a=10
    b=20
    print(globals()["a"])
    sum=globals()["a"]+b
    sub=a-b
    mul=globals().get("a")*b
    return sum,sub,mul
list=[]
l=calculator()
print(l)


# def my_name(fname,lname="emp1"):
#     print (fname ,lname)
# my_name("Emp1")
#
# def employee_details(*details):
#     print (details)
#     print ("Emp Name", details[0][0])
#     print("Emp id :", details[0][1])
#     print("company :", details[0][2])
# l=["Emp1", 1,"Company1"]
# employee_details(l)
#
# def computer(**names):
#     for i in names.items():
#         print("Name is :",i)
# computer(name1="Dell",name2="sony",name3="HP")
#
# count=0
# def welcome():
#     global count
#     print("Welcome", count)
#     count = count + 1
#     if count<=100:
#         welcome()
# welcome()

#Lambda
# from functools import reduce
#
# add=(lambda a,b:a+b)
# print(add(10,20))
# sub=(lambda a,b:a-b)
# print (sub(20,10))
# mul=(lambda a,b:a*b)
# print(mul(10,10))
#
# #Filter
# print("Filter")
# l=(12,23,33,77,65,44,90,88)
# print(list(filter(lambda a: a % 2 != 0,l)))
# print(tuple(filter(lambda a: a<=50,l)))
#
# #Map
# #-------
#
# l1=(2,4,3,1,5,6,7,8)
# print("Map")
# print(tuple(map(lambda a:a*a*a,l1)))
# print(tuple(map(lambda a:a*100,l1)))
#
# #Reduce
# #----------
#
# r=[12,45,32,22,65,43,13]
# print("Reduce")
# print(reduce((lambda a,b:a*b),r))

