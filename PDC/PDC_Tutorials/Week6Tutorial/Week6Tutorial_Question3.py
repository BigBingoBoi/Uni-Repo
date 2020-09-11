# -*- coding: utf-8 -*-
"""
Programming for Data Science
Week 6 Tutorial
@author u3141210 (Aleksandar Draskovic)
"""
import io_data_module
import tkinter
# Question 3
# read datalist
datalist = io_data_module.read_data_file('ellipse1.txt')
print(datalist)

# create canvas
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="white", height=600, width=850)

s = 90 # scale

# draw ovals
for x, y in datalist:
    x = x * s + 150
    y = y * s + 150
    C.create_oval(x-3, y-3, x+3, y+3, outline = "red", fill = "red")
    
# centre ovals    
centre_1 = (2.036779, 2.896883)
centre_2 = (2.836779, 3.896883)
a = centre_1[0] * s + 150
b = centre_1[1] * s + 150
c = centre_2[0] * s + 150
d = centre_2[1] * s + 150

# comment out old centre ovals

# =============================================================================
# C.create_oval(a-3, b-3, a+3, b+3, outline = "black", fill = "black")
# C.create_oval(c-3, d-3, c+3, d+3, outline = "black", fill = "black")
# =============================================================================


# determine distances and create lists 1-3
list1 = []
list2 = []
for x in datalist:
    d1 = ((centre_1[0]-x[0])*(centre_1[0]-x[0]) +
          (centre_1[1]-x[1]) * (centre_1[1]-x[1]))**0.5

    d2 = ((centre_2[0]-x[0])*(centre_2[0]-x[0]) +
          (centre_2[1]-x[1]) * (centre_2[1]-x[1]))**0.5
    
    if d1 < d2 and d1:
        list1.append((x[0], x[1]))
    elif d2 < d1 and d2:
        list2.append((x[0], x[1]))
      
# comment out old centre lines     
        
# draw lines from data samples to nearest centre
# =============================================================================
# for a in list1:
#     C.create_line(float(a[0] * s + 150), float(a[1] * s + 150), float(centre_1[0] * s + 150), float(centre_1[1] * s + 150), fill = "black")
# for b in list2:
#     C.create_line(float(b[0] * s + 150), float(b[1] * s + 150), float(centre_2[0] * s + 150), float(centre_2[1] * s + 150), fill = "black")
# =============================================================================
    

# calculate averages of lists and create new centres
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0


for i in list1:
    sum1 += i[0]
    sum2 += i[1]
new_centre1 = (sum1 / len(list1), sum2 / len(list1)) 
print("New centre 1: ", new_centre1)

for i in list2:
    sum5 += i[0]
    sum6 += i[1]
new_centre2 = (sum5 / len(list2), sum6 / len(list2), sum7 / len(list2), sum8 / len(list2))
print("New centre 2: ", new_centre2)


# new centre ovals    
g = new_centre1[0] * s + 150
h = new_centre1[1] * s + 150
i = new_centre2[0] * s + 150
j = new_centre2[1] * s + 150
C.create_oval(g-3, h-3, g+3, h+3, outline = "black", fill = "black")
C.create_oval(i-3, j-3, i+3, j+3, outline = "black", fill = "black")

# draw lines from data samples to new nearest centre
for a in list1:
    C.create_line(float(a[0] * s + 150 ), float(a[1] * s + 150), float(new_centre1[0] * s + 150), float(new_centre1[1] * s + 150), fill = "black")
for b in list2:
    C.create_line(float(b[0] * s + 150), float(b[1] * s + 150), float(new_centre2[0] * s + 150), float(new_centre2[1] * s + 150), fill = "black")

C.pack()
top.mainloop()

