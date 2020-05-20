# try:
#     print("Only for division")
#     num1 = int(input("First number: "))
#     num2 = int(input("Second number: "))
#     print("{0} / {1} = {2}".format(num1, num2, num1/num2))

# except ValueError:
#     print("Error! Wrong value")

# except ZeroDivisionError as err:
#     print(err)

# except:
#     print("Unknown error")

#################################

# try:
#     print("Only for one digit numbers")
#     num1 = int(input("First number: "))
#     num2 = int(input("Second number: "))
#     if num1 >=10 or num2 > 9:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, num1/num2))
# except ValueError:
#     print("Wrong number inserted")

############################

class BigValueError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("Only for one digit numbers")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    if num1 >=10 or num2 > 9:
        raise BigValueError("Error, inputs: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, num1/num2))

except ValueError:
    print("Wrong number inserted")

except BigValueError as err:
    print("Big value!")
    print(err)

finally:
    print("Thank you for using!")