name="johan"
Age=123
print("Name is ",name,"Age is ",Age)
print("Name is "+name+"     Age is "+str(Age))
print("Name is {} and Age is {}".format(name,Age))
print("Name is {} and Age is {}".format(Age,name))
print("Name is %s and Age is %d" %(name,Age))
# print("Name is %d and Age is %s" %(name,Age))  ---- TypeError
print(f"Name is {name} and Age is {Age}")