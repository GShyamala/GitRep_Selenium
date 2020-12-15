# name="shyamala gnanadass"
# print(name.title())
# print(name.upper())
# print(name.lower())
# first_name = "shyamala"
# last_name="gnanadass"
# full_name=f"{first_name} {last_name}"
# print(full_name.title())
# print(f"Hello,{full_name.title()}!")
#
# print("my\tnew\n\nproject")
# name ="   stripping       "
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())
# s="welcome to python"
# print(type(s))
# print(s)
# print("Length is", len(s))
# print(s[1])
# print(s[1:5])
# print(s[1:5:2])
# print(s[1:])
# print(s[:5])
# print(s[:])
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])

#INDEX
#----------
# s="welcome to python"
# s2="Selenium"
# # print(s.index("l"))
# print(s.index("python"))
# print(f"{s} {s2}" )
# print(s+s2)
# print(s,s2)
# print("".join([s,s2]))
# print("%s%s" % (s,s2))
# print("{} {}".format(s,s2))
# # print(s.rindex("e"))
# # print(s.rindex("to"))
# # print(s.index("b"))
#
# #FIND:
# #------
# # s="welcome to python"
# # print(s.find('l'))
# # print(s.find('e'))
# # print(s.rfind('e'))
# # print(s.find('a'))
#
# #starting
# #-------------
# s="welcome to python"
# print(s.startswith("w"))
# print(s.startswith("welcome"))
# print(s.startswith("wel"))
# print(s.startswith("to"))
# print(s.startswith("pyth"))
#
# #Ending
# #---------
# print(s.endswith("on"))
# print(s.endswith("python"))
# print(s.endswith("we"))
#
# #In
# #-----
#
# print("welcome" in s)
# print("jh" in s)
# print(" " in s)
#
# #Split
# #---------
# print(s.split(" "))
# print(s.split())
# print(s.split("e"))
#
# #memory
# #---------
#
# s1="string value"
# s2="string value"
# print(s1 is s2)
# print(s2)
# print(id(s1))
# print(id(s2))

#Length:
# #---------
# s1="greens technology"
# s2="selenium automation"
# s3="1231242354"
# print(len(s1))
# print(len(s2))
# print(len(s3))
# #Index position
# #________________
# print ("INDEX")
# print(s1.index("e"))
# print(s1.index("technology"))
# #Find:
# #---------
# print("FIND")
# print(s2.find("m"))
# print(s2.find("mation"))
# #sliceoperator
# #------------------
# print("SUBSTRING USING SLICE OPERATOR")
# print(s1[1:5])
# print(s2[9:19])
# print(s2[-6:-1])
# print(s2[-6:])
#
# s="c,c++,Java,Python"
# if(s.find("Java") != -1 ):
#     print ("Substring found")
# else:
#     print("Substring not found")
#
# #COUNT
# #_________
# s="python is awesome and it is dynamic language"
# print(s.count("is"))
# print(s.count("m"))

#ITERATION
#-----------
vowel=0
cons=0
s=input("please enter your string")
for i in range (0,len(s)):
    if s[i] == ('a' or 'A'):
       vowel=vowel+1
    elif s[i] == ('e' or 'E'):
        vowel=vowel+1
    elif s[i] == ('i' or 'I'):
        vowel = vowel + 1
    elif s[i] == ('o' or 'O'):
        vowel = vowel + 1
    elif s[i] == ('u' or 'U'):
        vowel=vowel+1
    else:
        cons=cons+1
print ("Vowels are : ", vowel)
print("Consonants are :", cons)