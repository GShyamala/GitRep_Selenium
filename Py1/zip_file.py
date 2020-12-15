from zipfile import *

with ZipFile("new_zip.zip",'w', ZIP_DEFLATED) as f:
    f.write("new_file.txt")
    f.write("py_file.txt")
with ZipFile("new_zip.zip",'r', ZIP_STORED) as f:
    print(type(f))
    rd=f.namelist()
    new_zip=list(rd)
    for i in new_zip:
        print("File is",i,"-------------")
        with open(i, 'r')as f1:
            da=f1.read()
            print(da)