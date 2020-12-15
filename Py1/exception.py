# print(1)
# print(2)
# try:
#     print(3)
#     try:
#         print(4+"a")
#     except ZeroDivisionError:
#         print("inside")
#     except TypeError:
#         print("Type")
#     finally:
#         print("Inside try")
# except Exception:
#     print("Exception")
# except BaseException:
#     print("BaseException")
# else:
#     print("i am in else part")
# finally:
#     print("I am in finally")

# empName = "Emp11"
# if empName == "Emp1":
#     print("Valid")
# else:
#     try:
#         raise NameError
#     except NameError:
#         print("Value is wrong")

class EmployeeNotFoundError(Exception):
      msg = ("Employee not present in DB")
id=12345
if id == 1234:
    print ("Valid entry")
else:
    try:
        raise EmployeeNotFoundError
    except EmployeeNotFoundError as ex:
        print(ex.msg)











