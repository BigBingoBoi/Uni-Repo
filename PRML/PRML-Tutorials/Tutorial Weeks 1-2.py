# -*- coding: utf-8 -*-
"""
Pattern Recognition and Machine Learning
Weeks 1-2 Tutorial
@author u3141210 (Aleksandar Draskovic)
"""

# Exercise 1: The First Running
print("Hello, World!")


# Exercise 2: Values and Operators
print(5 + 4) 
print(5.0 + 4.0)
print((5 + 4) * 8)
print((5.0 + 4) * 8)
print(-5 * -4 + 2)
print(4 ** 2 + 6 )
print(-4 ** 2 + 6)
print((9 + 1) * 5 / 2)
print((10 - 6) / ((3 * 2) - (15 / 5)))


# Exercise 3: Types of Values
print(type(5 + 4))
print(type(5.0 + 4.0))
print(type((5 + 4) * 3))
print(type((4.0 + 5) * 3))
print(type((9 + 1) * 5 / 2))
print(type("Hello World"))


# Exercise 4: Operators on Different Types
print("Hello" + "World")
print(type("Hello" + "World"))
print("Abc" * 3)
print("Abc" * 3.0)
print("123" * 3)
print("36" / 12)
print("36" / "3")
print([1, 2, 3] + [4, 5, 6] * 3)
print(["Hello", "World"] * 3)
print(type(["Hello", "World"] * 3))
print([1, 2, 3] * [3])


# Exercise 5
x = int(input("Enter a number: "))
y = x ** 2
print(f"The square of {x} is {y}")

a = int(input("Enter a number: "))
b = int(input("Enter a second number:" ))
c = a * b
print(f"{a} multiplied by {b} equals {c}")


# Exercise 6
print(3<5)
print(12 <= 6)
print(5 == 5.0)
print(2 * 3 == 3 * 2)
print(5-4 != 2)
print("Hello World" == "hello world")
print("Hello" + "World" == "Hello World")
print("ABC" < "ABCD")
print("123" < "97")


# Exercise 7
x = int(input("Enter a number: "))
if x < 0:
    print("x is negative")
elif x <= 10:
    print("x is between 0 and 10")
else: print("x is greater than 10")


x = int(input("Enter a number: "))
if x < 0:
    print(f"{x} is negative")
elif x == 0:
    print("This is 0")
elif x > 0:
     print(f"{x} is positive")
    

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
numList = [x, y, z]
numList.sort()
print("Largest number is: ", numList[-1])


x = int(input("Enter your score: "))
if x >= 85:
    print("HD")
elif x >= 75:
    print("D")
elif x >= 65:
    print("CR")
elif x >= 50:
    print("P")
else:
    print("F")


# Exercise 8
assessments = ['quizzes', 'assignments', 'exams'] 
for ass in assessments: 
    print(ass) 
    total_mark = 0 
    marks = [30, 25, 40] 
for point in marks: 
    total_mark += point 
    print(total_mark) 
    total_mark = 0 
    marks = [30, 25, 40] 
for i in range(len(marks)): 
    total_mark += marks[i] 
    print(total_mark) 
for c in 'data': #string data is a sequence of characters 
    print(c) 
 
 
x = int(input("Enter a positive integer: "))
y = x ** 2
def squareSum(x):
    z = 0
    for i in range(1, x+1):
        z = z + (i * i)
        if i < x - 1:    
            print(f"{z} + ", end = '')
        if i == x -1:
            print(f"{z} ", end = '')
    return z
print("=", squareSum(x))


# Exercise 9
while True:
    x = int(input("Enter a number: "))
    if x < 0:
        print(f"{x} is negative")
    elif x == 0:
        print("This is 0")
    elif x > 0:
        print(f"{x} is positive")
    

    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    z = int(input("Enter the third number: "))
    numList = [x, y, z]
    numList.sort()
    print("Largest number is: ", numList[-1])


    x = int(input("Enter your score: "))
    if x >= 85:
        print("HD")
    elif x >= 75:
        print("D")
    elif x >= 65:
        print("CR")
    elif x >= 50:
        print("P")
    else:
        print("F")



















