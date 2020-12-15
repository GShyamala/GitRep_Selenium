t=(34,10,56,12,10,"python","rs",78,10,90)
lis=list(t)
print(type(lis))
print(t.index(12))
print(t.index("python"))
print(t[3:7])
print(t[-2])

count=0
for i in range(0,len(t)):
    if t[i] == 10:
        print (i, "--------",t[i])
        count=count+1
print("10 present in", count, "Times")

t=(45,23,10,76,23,10,90,89,10,67)
print(t.count(10))
print(min(t))
print(max(t))

s=sorted(t)
print(t)
print(s)
print(type(s))
tup1=tuple(s)
print(type(tup1))
t1=(10,70,60,50,30)
t2=(10,70,60,50,30)
print(t1==t2)
tco=("python")
print(tco)
print(type(tco))
