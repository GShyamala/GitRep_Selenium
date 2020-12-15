# f=open("new_file.txt",'w')
# print(f.name)
# print(f.writable())
# print(f.readable())
# print(f.closed)
# print(f.close())
# print(f.closed)
# #WRITE
# #--------
# f=open("new_file.txt", 'w')
# f.write("New to Python\n")
# f.writelines("mbkldjbkdflbj\n")
# f.writelines("mbkldjbkdflbj\n")
# f.writelines("mbkldjbkdflbj\n")
# f.close()
# #Append
# #----------
# f=open("new_file.txt",'a')
# f.writelines("python")
# f.writelines("Java")
# f.close()
#Read
#---------
# f=open("new_file.txt",'r')
# p=f.read(20)
# print(p)
# c=f.tell()
# print(c)
# #Readline
# l=f.readline()
# print(l)
# lines=f.readlines()
# print(lines)
# #Position
# #----------
# f.seek(0)
# l=f.read()
# print(l)
# tel=f.tell()
# print(tel)
# f.close()
#with R+
#_______
with open("py_file.txt",'w+') as py:
    r=py.read()
    print(r)
    py.write("pythn\n")
    py.writelines("selenium")
    py.seek(0)
    r=py.read()
    print(r)
#with W+
#____________
with open("py_file.txt",'w+') as py1:
    py1.writelines("kjfhvjjfkvl")
    py1.writelines("kjhjkfhfjh")
    py1.seek(0)
    new=py1.readlines()
    print(new)


    #Binary
with open ("Typing_Keyboard_Wide.jpg",'rb' ) as f1:
    r=f1.read()
    print(r)

with open("new.jpg",'wb')as f:
    f.write(r)
with open("testDoc.doc", 'w+') as f:
    f.write("New to Python files")
    f.write("Learning Python")
with open("NewExcel.xls", 'w+',newline="")as f1:
    f1.write("Writting xl")
    f1.writelines(["1","johan","johan@gmail.com"])