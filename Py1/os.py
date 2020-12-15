import os
#Create Folder
# os.mkdir(r"E:\Python\dir_test")
# os.makedirs(r"E:\Python\F1\F2\F3")
f=os.path.isfile(r"E:\Python\F1\F2\hello.txt")
print(f)
f=os.path.isfile(r"E:\Python\F1\F2")
print(f)
f=os.path.isdir(r"E:\Python\F1\F2")
print(f)
f=os.path.isdir(r"E:\Python\F1\F2\hello.txt")
print(f)
#List Dir
lis_dir=os.listdir(r"E:\Python")
print(type(lis_dir))
print(lis_dir)
for i in lis_dir:
    print(i)
#Walk
wal=os.walk(r"E:\Python")
print(type(wal))
for i in wal:
    print(i)
# rm=os.rmdir(r"E:\Python\F1\F2\F3")
# print(rm)
rm1=os.removedirs(r"E:\Python\F1")
print(rm1)