"""
Programming for Data Science
Week 2 Tutorial
"""

# =============================================================================
# #Output
# print("Hello, World!")
# 
# #Input
# x = input("Enter a number: ")
# 
# print("You have entered " + x)
# 
# 
# x = 5 #x is of type int
# print(type(x)) #output type of x
# 
# 
# y = 7.9 #y is of type float
# print(type(y))
# 
# z = 1 + 3j #z is of type complex and j is imaginary
# print(type(z))
# 
# u = "Data Science" #u is of type str (string)
# print(type(u))
# v = 'Data Science' #v is of type str (string), too
# print(type(v))
# 
# t = True #t is of type bool
# print(type(t))
# 
# 
# a, b = 'data', 'science'
# print("a = " + a)
# print("b = " + b)
# 
# c = d = 'python'
# print('c = ' + c + ' and d = ' + d)
# 
# 
# a = 5 #a = 5
# print(a)
# b = float(a) #b = 5.0
# print(b)
# c = bool(b) #c = True
# print(c)
# d = str(c) #d = 'True'
# print(d)
# e = complex(a) #e = 5 + 0j
# print(e)
# 
# 
# name = 'Data Science'
# print("Unit name = " + name)
# myId = 123456
# print('My ID is ' + str(myId))
# print(f'My ID is {myId}')
# 
# 
# print('Programming for Data Science\nWeek 2 Tutorial')
# 
# print("""Programming for Data Science#Week 2 Tutorial
# """)
# 
# 
# s1 = 'abc'
# s2 = 'def'
# print(f's1 = {s1}')
# print(f's2 = {s2}')
# print(f's1 + s2 = {s1 + s2}')
# print(f's1 * 2 = {s1 * 2}')
# print('\n')
# x1 = 5
# x2 = 2
# print(f'x1 = {x1}, x2 = {x2}')
# x3 = x1 + x2
# print(f'x1 + x2 = {x3}')
# x3 = x1 - x2
# print(f'x1 - x2 = {x3}')
# x3 = x1 * x2
# print(f'x1 * x2 = {x3}')
# x3 = x1 ** x2 #power
# print(f'x1 ** x2 = {x3}')
# x3 = x1 / x2
# print(f'x1 / x2 = {x3}')
# x3 = x1 // x2 #divide and floor
# print(f'x1 // x2 = {x3}')
# x3 = x1 % x2 #modulo
# print(f'x1 % x2 = {x3}')
# 
# 
# w = 5
# print(f'w = {w}')
# w += 2
# print(f'w += 2 -> w = {w}')
# w -= 2
# print(f'w -= 2 -> w = {w}')
# w *= 2
# print(f'w *= 2 -> w = {w}')
# w /= 2
# print(f'w /= 2 -> w = {w}')
# w %= 2
# print(f'w %= 2 -> w = {w}')
# 
# 
# x1 = 5
# print(f'x1 = {x1}')
# x2 = 2
# print(f'x2 = {x2}')
# if x1 == x2:
#     print('x1 equals x2')
# elif x1 < x2:
#     print('x1 is less than x2')
# else:
#     print('x1 is greater than x2')
# 
# 
# x = 5
# while x <= 10:
#     x += 1
# else:
#     print(f'x = {x}')
#     
#     
# x = 0
# while x <= 3:
#     x += 2
#     print(f'x = {x}')
#     
#     
# assessments = ['tutorials', 'assignments', 'exams']
# for ass in assessments:
#   print(ass)
#   
#   
# for c in 'data': #string data is a sequence of characters
#   print(c)
# 
# 
# while True:
#     x = int(input('Enter a number : '))
#     if x == 0:
#         break
#     print('The number is', x)
# print('Done')
# 
# 
# while True:
#     x = int(input('Enter a positive number : '))
#     if x == 0:
#         break
#     elif x < 0:
#         print('The number must be positive')
#         continue
#     print('The number is', x)
# print('Done')
# =============================================================================


while True:
    x = int(input('Enter a number: '))
    y = x ** 2
    print(f'The square of {x} is {y}')
    i = input('Continue? (y/n) ')
    if i == 'n':
        break
    elif i == 'y':
        continue
print('Done')
        