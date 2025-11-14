# print("Hello World")
# if 5>2:
#     print("five is greater than two")
# x = 5
# y = 3
# print(x-y)
# print(x+y)
# print(x*y)
# print(x/y)
# x = ""
# print(bool(x))
# x = "e"
# print(bool(x))

# x = "30","40","50"
# print(x)

# fruits = ["banana", "apple","cherry"]
# x,y,z = fruits
# print(y)
# print(type(y))
# print(type(fruits))


# x = "this is python"
# print(x)

# x= "python"
# y ="is"
# z = "good"
# print(x,y,z)
# print(x+y+z)


# x = "good"
# def my_function():
#     print("python is "+x)

# my_function()


# x = 1j

# print(type(x))



# print("Hello world")
# my_list = [1,2,9,4]
# my_list.insert(0,"svchm")
# my_list.append("sfa")
# print(my_list)




# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.extend(list2)
# print(list1)



# list3 = [1,2,3,4,5,6]
# list3.insert(5,"banana")
# print(list3)
# list3.remove("banana")
# print(list3)

# list3.append("apple")
# print(list3)
# list3.pop()
# print(list3)

# list3.clear()
# print(list3)

#looslists
# list1 = [1,2,3,4,5,4,4,6]
# for x in list1:
#     print(x)





# sort
# list1 = [2,5,1,4,8]
# list1.sort()
# print(list1)

# list = [2,5,1,4,8]
# list.sort(reverse=True)
# print(list)




# text = "hello"

# print(text.upper())
# print(text.lower())
# print(text.strip())
# print(text.replace("hello","world"))
# print(text.split())
 

# x = "bob"
# y = 20
# print(f"my name is {x} and my age is {y}")


# x = 5
# x+=5
# print(x)


# #x = 5
# #y = "hello"
# #print(x+y)

# x = "bob"
# y = 20
# print(f"my name is {x} and my age is {y}")


# x = 20
# x *= 4
# print(x)
# x /= 6
# print(x)
# x -= 8
# print(x)
# x += 19
# print(x)

# y = 2
# y **= 4
# print(y)
# y %= 5
# print(y)



# y = 12
# y //= 6
# print(y)

# a = 5
# b = 10
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b)
# print(a<b)
# print(a>b)

# x = 5
# y =x
# print(x is y)
# z = 10
# print(z is x)
# print(z is not x)

# students = {"name":"chander","age":30,"grades": "A"}
# print(students)


# if else 
# age = 20
# if age>=18:
#     print("you are an adult")
# else:
#     print("you are not adult")



# marks = 85
# if marks >= 90:
#     print("Grade A+")
# elif marks >= 75:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# else : 
#     print("Grade D")






# x = 45
# if x>10:
#     print("x is grrater than 10")
#     if x>20:
#         print("x is greater than 20")
#     else:
#         print("x is not greater than 20")
# else:
#     print("x is smaller than 10")

# 




# x = int(input("enter the person age: "))

# if x >= 18:
#     print("you are eligible for driving")

# else:
#     print("you are not eligibblle for driving")

# loops

# fruits = ["apple", "banana","cherry"]
# for i in fruits:
#     print(i)

# for i in range(5):
#     print(i)
# 

# for i in range(1,5):
#     for j in range(1,4):
#         print(f"i = {i}, j = {j}")

# colours = ["black","blue","red","maroon","brown"]
# for i in colours:
#     print(i)

# matrix = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         value=int(input(f"enter the [{i+1}] [{j+1}] element"))
#         row.append(value)
#     matrix.append(row)
# for row in matrix:
#     for j in row:
#         print(j, end = "\t")
#     print()



# def a():
#     print("hhello python")


# a()


# def greet(name):
#     print(f"hello {name}")


# greet("bob")
# greet("alice")


# def mul(a,b):
#     return a*b
# a = mul(7,5)
# print(a)

# def sub(a,b):
#     return a-b
# a = sub(45,5)
# print(a)
# def div(a,b):
#     return a/b
# a = div(455,5)
# print(a)

# def add(a,b):
#     return a+b
# a = add(7,5)
# print(a)

# def greet(name = "student"):
#     print(f"hello {name}")


# greet()
# greet("alice")


# x = 10
# def fun():
#     global y
#     y = 5

#     print("inside" , x ,y)
# fun()
# print("outside" , x)
# print(y)

# 



# class car:
#     def __init__(self,brand,colour):
#         self.brand = brand
#         self.colour = colour
#     def drive(self):
#         print(f"{self.colour} {self.brand} is driving")


# car1 = car("bmw","black")
# car1.drive()


# car2 = car("mercedes" , "white")
# car2.drive()


# import array

# number = array.array('i',[45,45,11,89,4])
# print(number)


# from numpy import random

# x = random.randint(0,100)
# print(x)


# x = random.rand()
# print(x)
# print(type(x))

# [85]
# [[45,45,66,5],
#  [4,24,52,1,5,4]]
# [[[4,4,1],[52,41,65]]
#  ,[[5,6,2],[41,41]]]

# from numpy import random
# x = random.randint(100,size = 3)
# print(x)


# x = random.randint(100,size =(3,2))
# print(x)


# x = random.randint(100,size =(3,2,2))
# print(x)
# x = random.randint(100,size =(2,2,3,5))
# print(x)



#pandas

#import pandas as a 
# data = [45,45,24,63]

# x = a.Series(data)
# print(x)


# import pandas as pd

# data = {
#     "name":["Alice", "bob","Charlie","David"],
#     "Age":[24,27,22,23],
#     "city":["Delhi","mumbai","Chennai","kolkata"]
# }
# df = pd.DataFrame(data)
# print(df)


# import numpy as np

# arr = np.array([1,2,3,4])

# s = pd.Series(arr)
# print(s)


import pandas as pd

df = pd.read_csv("D:\crocodile_dataset.csv")
print(df.head())
print(df.tail())