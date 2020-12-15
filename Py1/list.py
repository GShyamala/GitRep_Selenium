# print("LENGTH")
l=[10,234,65,43,57,10,78,31,10]
# print(len(l))
# print("INDEX")
# print(l.index(43))
# print(l.index(10,-1))
# #print(l.index(89)) ValueError
#
#
# print(" all 10's index")
# print(l)
# for i in range(0,len(l)):
#     if (l[i] == 10):
#         print (i)
# #APPEND:
# l.append(200)
l.insert(30,"600")

# l.append([300,400,500])
# print(l[10][1])
# # l.append(100,200,300) TypeError
# print(l)
# #Remove:
# print(l[2])
# l.remove(l[2])
# print(l)
l=[10,45,34,23,76,45,10,67,45,10,78]
print(l[2])
print(l[4])
print(l.remove(76))
print(l)
del(l[-2:-1])
print(l)
del(l[-3:-1])
print(l)
l[2]=500
print(l)
l.reverse()
print(l)
for i in range(0,len(l)):
    print(l[i])
s=sorted(l)
print(l)
#l.sort(reverse=True)
print(s)
for i,j in enumerate(l):
    if i%2 != 0:
        print (i,j)
