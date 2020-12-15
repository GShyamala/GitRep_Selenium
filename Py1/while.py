# a=10
# while a>5:
#     print (a)
#     a=a+1
#     if a>15:
#         break

# prompt=("Tell me something, i will repeat")
# prompt+=("\nEnter 'quit' to Exit !")
# message=""
# while message != "quit":
#     message=input (prompt)
#     print(message)
#

prompt=("Enter your fav city!")
prompt+=("Enter 'quit' to Exit")
message=""
while True:
    print (prompt)
    message=input()
    if message=="quit":
        break
    else:
        print("I love", message)

number =0
while number <10:
    number=number+1
    if number % 2 == 0:
        continue

    print (number)
