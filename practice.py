# print(5)
# print(3.14)
# print("ha"*9)
# print(5<10)

# age = 5
# name = "yo"

# print(name + " is " + str(age) + "years old")
# print(name, "is", age, "years old")

# print(2**3)
# print(29//4)
# print(29%4)

# print((3 < 4) and (5 < 2))
# print((3 < 4) & (5 < 2))

# print((3 < 4) or (5 < 2))
# print((3 < 4) | (5 < 2))

# print(pow(3, 2))

# from math import *

# print(floor(4.89))
# print(ceil(3.19))
# print(sqrt(16))

# from random import *

# print(random()) # 0.0 ~ 1.0 미만
# print(int(random() * 10)) # 0 ~ 10 미만
# print(int(random() * 10 + 1)) # 1 ~ 10 이하
# print(randrange(1, 46)) # 1 ~ 46 미만
# print(randint(1, 45)) # 1 ~ 45 이하

# sentence = '''
# I am a boy.
# I like python.'''
# print(sentence)

# jumin_number = "940912-1234567"
# print("gender: " + jumin_number[7])
# print("year: " + jumin_number[0:2])
# print("birth year, month, day: " + jumin_number[:6])
# print("back seven numbers: " + jumin_number[-7:])

# python = "Python is good"
# print(python.lower())
# print(python[0].isupper())
# print(python.replace("Python", "Java"))

# index = python.index("o")
# print(index)
# index = python.index("o", index + 1)
# print(index)
# print(python.count("o"))

# print("I am %s. I am %dyears old." %("Sujong", 27))
# print("I am {}years old." .format(27))
# print("I am {1}. I am {0}years old." .format(27, "Sujong"))
# print("I am {name}. I am {age}years old." .format(age = 27, name = "Sujong"))

# print("I am Sujong.\nI am 27 years old.")
# print("I like \"Python\".")

# print("C:\\Users\\Sujong\\Desktop") # \\ is \ in printing

# print("Red apple\rPine") # \r moves cursor to the beginning
# print("Pinee\bapple") # \b is backspace
# print("Pine\tapple") # \t is tab

# arr = [10, 20, 30]
# print(arr.index(20))
# arr.insert(1, 15)
# print(arr)
# arr.append(10)
# print(arr.count(10))

# numbers = {1: "100", 2: "200", 3: "300"}
# print(numbers[2])
# # print(numbers[5])
# print(numbers.get(5, "no value"))
# del numbers[2]
# print(numbers)
# print(numbers.keys())

# (tup, arr, dic) = ("tuple", "array", "dictionary")
# print(tup, arr, dic)

# set_1 = {1,2,3,4,5,5,5}
# set_2 = {2,3,4}
# print(set_1)
# print(set_1 & set_2)
# print(set_1 | set_2)


# weather = input("weather?")
# if weather == "rainy":
#     print("umbrella")
# else:
#     print("nothing")

# customer = "Iron man"
# index = 5
# while index >=1:
#     print("{0}, your coffee is ready. {1} times left." .format(customer, index))
#     index -= 1
#     if index == 0:
#         print("Your coffee is gone.")

# def profile(name, age, main_lang):
#     print("name: {0}\tage: {1}\tmain language: {2}" \
#         .format(name, age, main_lang)) #change line

# profile("Sujong", 27, "Python")
# profile(main_lang = "Java", age = 27, name = "Sujong")

##### * usage #####
# def profile(name, age, *language):
#     print("name: {0}\tage: {1}\t".format(name, age), end = " ") #no line change
#     for lang in language:
#         print(lang, end = " ")
#     print()

# profile("Sujong", 27, "Python", "C", "C++")

2:59:00