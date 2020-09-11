# -*- coding: utf-8 -*-
"""
Programming for Data Science
Week 4 Tutorial
@author u3141210 (Aleksandar Draskovic)
"""
import io_data_module as iodata
import tkinter

#Open file and read 
data_list = iodata.read_data_file('ellipse1.txt')
#print(data_list)

#Create canvas
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="white", height=720, width=720)

#Display data
s = 90 #scale factor
r = 4 #radius
for x, y in data_list:
    x = x*s + 150 #some values are negative so +150 to make them positive
    y = y*s + 150 
    C.create_oval(x-2, y-2, x+2, y+2, outline = "red", fill= "red")
    
#Question 1
unknown_sample = (2.236779, 2.896883)
a = unknown_sample[0] * s + 150
b = unknown_sample[1] * s + 150
C.create_oval(a-2, b-2, a+2, b+2, outline = "black", fill = "white")
    
#Question 3
nearest_neighbor = iodata.find_nearest_neighbor(unknown_sample, data_list)
j = nearest_neighbor[0]* s + 150
k = nearest_neighbor[1]* s + 150
C.create_oval(j-2, k-2, j+2, k+2, outline = "black", fill = "black")
C.create_line(a, b, j, k, fill = "black")

C.pack()
top.mainloop()
