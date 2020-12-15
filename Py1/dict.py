l=[(10,'emp1','emp1@gmail.com'),(20,'emp2','emp2@gmail.com'),(30,'emp3','emp3@gmail.com')]
print(l[1])
print(l[1][1])
for i in range (0,len(l)):
        for j in range (0,len(l)):
            print(l[i][j])

dic=({id:10,'Name':'emp1','Mail':'emp1@gmail.com'},{id:20,'Name':'emp2','Mail':'emp2@gmail.com'},{id:30,'Name':'emp3','Mail':'emp3@gmail.com'})
print(dic[2])
for i in range (0,len(dic)):
        print(dic[i][id])
        print (dic[i]["Name"])


dn={'key1':(1,"emp1","emp1@gmail.com"),'key2':(2,"emp2","emp2@gmail.com"),'key3':(3,"emp3","emp3@gmail.com")}
print(dn['key1'])

for i in dn.items():
    for j in i:0
        print(j)

