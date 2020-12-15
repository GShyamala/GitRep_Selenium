import csv
with open ("csv_test.csv",'w+',newline="")as f:
    c=csv.writer(f)
    c.writerow(["100","johan",12349478349])
    c.writerow(["200", "john", 12349478349])
    c.writerow(["300", "sam", 12349478349])
    c.writerow(["400", "jons", 12349478349])
    print(type(c))

with open("csv_test.csv",'r+')as f1:
    r=csv.reader(f1)
    print(type(r))
    li = list(r)
    print(li)
    for i in li:
        print(i)
    wr=csv.writer(f1)
    wr.writerow(["500","josh", 6547676767])

with open ("csv_test.csv",'a+',newline="")as f:
    c=csv.writer(f)
    c.writerow(["600","`    jo",456776775])
    c.writerow(["700", "jade", 12])