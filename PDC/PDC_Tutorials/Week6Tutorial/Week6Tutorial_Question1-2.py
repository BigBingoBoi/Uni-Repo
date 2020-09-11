# -*- coding: utf-8 -*-
"""
Programming for Data Science
Week 6 Tutorial
@author u3141210 (Aleksandar Draskovic)
"""
import io_data_module
import tkinter

# Question 1
def read_data_to_dict(filename):
    # declare list
    dataset = []
    # declare dictionary
    dataDict = {}
    # declare lists of tuples
    seto = []
    vers = []
    virg = []
    
    # read file
    file = None
    try:
        file = open(filename, 'r')
        while True:
            line = file.readline()
            if len(line) == 0:
                break
            # add all tuples (lines) to list
            dimLab = line.split(',')
            dataset.append((float(dimLab[0]), float(dimLab[1]), float(dimLab[2]),
                            float(dimLab[3]), str(dimLab[4])))          
    except Exception as ex:
        print(ex.args)
    finally:
        if file:
            file.close()    
    
    # loop through dataset and fill 3 lists of tuples
    for i in dataset:
        if i[4] == 'Iris-setosa\n':
            seto.append((float(i[0]), float(i[1]), float(i[2]), float(i[3]))) 
        elif i[4] == 'Iris-versicolor\n':
            vers.append((float(i[0]), float(i[1]), float(i[2]), float(i[3])))
        elif i[4] == 'Iris-virginica\n':
            virg.append((float(i[0]), float(i[1]), float(i[2]), float(i[3])))

    # add keys and values to dictionary
    dataDict["Iris-setosa"] = seto
    dataDict["Iris-versicolor"] = vers
    dataDict["Iris-virginica"] = virg

    return dataDict
            
# print(read_data_to_dict("iris.data"))


# Question 2
# read datalist
datalist = io_data_module.read_multi_dim_data('iris.data')

# create canvas
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="white", height=1080, width=1920)

s = 170 # scale

# draw ovals
for i in datalist:
    x = i[0] * s
    y = i[1] * s
    C.create_oval(x-3, y-3, x+3, y+3, outline = "red", fill = "red")
    
# centre ovals    
centre_1 = (5.1, 3.0, 1.1, 0.5)
centre_2 = (4.4, 3.2, 2.8, 0.2)
centre_3 = (5.7, 3.9, 3.9, 0.8)
a = centre_1[0] * s
b = centre_1[1] * s
c = centre_2[0] * s
d = centre_2[1] * s
e = centre_3[0] * s
f = centre_3[1] * s


C.create_oval(a-3, b-3, a+3, b+3, outline = "black", fill = "black")
C.create_oval(c-3, d-3, c+3, d+3, outline = "black", fill = "black")
C.create_oval(e-3, f-3, e+3, f+3, outline = "black", fill = "black") 


# determine distances and create lists 1-3
# Dat's modification, old one only works with 2 dimensions
####################
def calculate_distance(a, b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i]-b[i]) * (a[i]-b[i])
    dist = dist**0.5
    return dist
####################
list1 = []
list2 = []
list3 = []
for x in datalist:
    #d1 = ((centre_1[0]-x[0])*(centre_1[0]-x[0]) +
    #      (centre_1[1]-x[1]) * (centre_1[1]-x[1]))**0.5
    d1 = calculate_distance(centre_1, x)
    #d2 = ((centre_2[0]-x[0])*(centre_2[0]-x[0]) +
    #      (centre_2[1]-x[1]) * (centre_2[1]-x[1]))**0.5
    d2 = calculate_distance(centre_2, x)
    #d3 = ((centre_3[0]-x[0])*(centre_3[0]-x[0]) +
    #      (centre_3[1]-x[1]) * (centre_3[1]-x[1]))**0.5
    d3 = calculate_distance(centre_3, x)
    if d1 < d2 and d1 < d3:
        list1.append((x[0], x[1], x[2], x[3]))
    elif d2 < d1 and d2 < d3:
        list2.append((x[0], x[1], x[2], x[3]))
    elif d3 < d1 and d3 < d2: 
        list3.append((x[0], x[1], x[2], x[3]))
        

        
# =============================================================================
# # draw lines from data samples to nearest centre
# for a in list1:
#     C.create_line(float(a[0] * s), float(a[1] * s), float(centre_1[0] * s), float(centre_1[1] * s), fill = "black")
# for b in list2:
#     C.create_line(float(b[0] * s), float(b[1] * s), float(centre_2[0] * s), float(centre_2[1] * s), fill = "black")
# for c in list3:
#     C.create_line(float(c[0] * s), float(c[1] * s), float(centre_3[0] * s), float(centre_3[1] * s), fill = "black")
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
sum9 = 0
sum10 = 0 
sum11 = 0
sum12 = 0

for i in list1:
    sum1 += i[0]
    sum2 += i[1]
    sum3 += i[2]
    sum4 += i[3]
new_centre1 = (sum1 / len(list1), sum2 / len(list1), sum3 / len(list1), sum4 / len(list1)) 
print("New centre 1: ", new_centre1)

for i in list2:
    sum5 += i[0]
    sum6 += i[1]
    sum7 += i[2]
    sum8 += i[3]
new_centre2 = (sum5 / len(list2), sum6 / len(list2), sum7 / len(list2), sum8 / len(list2))
print("New centre 2: ", new_centre2)

for i in list3:
    sum9 += i[0]
    sum10 += i[1]
    sum11 += i[2]
    sum12 += i[3]
new_centre3 = (sum9 / len(list3), sum10 / len(list3), sum11 / len(list3), sum12 / len(list3))
print("New centre 3: ", new_centre3)

# new centre ovals    
g = new_centre1[0] * s
h = new_centre1[1] * s
i = new_centre2[0] * s
j = new_centre2[1] * s
k = new_centre3[0] * s
l = new_centre3[1] * s
C.create_oval(g-3, h-3, g+3, h+3, outline = "black", fill = "black")
C.create_oval(i-3, j-3, i+3, j+3, outline = "black", fill = "black")
C.create_oval(k-3, l-3, k+3, l+3, outline = "black", fill = "black") 

# draw lines from data samples to new nearest centre
for a in list1:
    C.create_line(float(a[0] * s), float(a[1] * s), float(new_centre1[0] * s), float(new_centre1[1] * s), fill = "black")
for b in list2:
    C.create_line(float(b[0] * s), float(b[1] * s), float(new_centre2[0] * s), float(new_centre2[1] * s), fill = "black")
for c in list3:
    C.create_line(float(c[0] * s), float(c[1] * s), float(new_centre3[0] * s), float(new_centre3[1] * s), fill = "black")

C.pack()
top.mainloop()

 