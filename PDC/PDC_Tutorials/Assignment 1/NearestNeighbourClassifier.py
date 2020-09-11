# -*- coding: utf-8 -*-
"""
Programming for Data Science
Assignment 1 (Nearest Neighbor Classifier)
@author u3141210 (Aleksandar Draskovic)
"""
import io_data_module as iodata
import tkinter

# Read red, blue, and unknown datasets. Store in list. 
redList = iodata.read_data_file('datasets/red_2d.txt')
blueList = iodata.read_data_file('datasets/blue_2d.txt')
unknownList = iodata.read_data_file('datasets/unknown_2d.txt')

# Print lists to check all is well
print("Red list:\n", redList, "\n")
print("Blue list:\n", blueList, "\n")
print("Unknown list:\n", unknownList, "\n")

# Calculate distances from unknown to red/blue data
# Create lists for storing "labeled" unknown samples
redLabeled = []
blueLabeled = []

# Get distance from unknown list, find distance to each point in red list and 
# blue list. Add shortest distances and respective coordinates to min1 and 
# min2 respectively
for x in unknownList:
    rdList = []
    bdList = []
    for y in redList:
        rd = iodata.calculate_distance(x, y)
        rdList.append((x, rd))
    for z in blueList:
        bd = iodata.calculate_distance(x, z)
        bdList.append((x, bd))
    rdList.sort(key=lambda tuple: tuple[1])
    bdList.sort(key=lambda tuple: tuple[1])
    min1 = rdList[0]
    min2 = bdList[0]
    
    # Compare min1 and min2, assign red or blue label to unknown sample
    if min1[1] < min2[1]:
        redLabeled.append(min1[0])
    elif min2[1] < min1[1]:
        blueLabeled.append(min2[0])
        
# Print labeled unknowns to check all is well
print("Unknown samples labeled 'red':\n", redLabeled, "\n")
print("Unknown samples labeled 'blue':\n", blueLabeled)

# Write unknown, red labeled, and blue labeled samples to file
with open('unknown_and_labeled_red_blue_samples.txt', 'w') as f:
    f.write("Unknown samples:\n")
    for x in unknownList:
        f.write(str(x) + "\n")
    f.write("\nRed labeled samples:\n")
    for y in redList:
        f.write(str(y) + "\n")
    f.write("\nBlue labeled samples:\n")
    for z in blueList:
        f.write(str(z) + "\n")

# Create window and canvas
top = tkinter.Tk()
C = tkinter.Canvas(top, bg = "white", height = 720, width = 900)

# Draw red, blue and unknown (black) ovals using show_data function
s = 70 # Scale variable
r = 4 # Radius variable
tx = 250 # X translation
ty = 200 # Y translation

iodata.show_data(redList, 0, 1, 'red', 'red', C, r, s, tx, ty)
iodata.show_data(blueList, 0, 1, 'blue', 'blue', C, r, s, tx, ty)
iodata.show_data(unknownList, 0, 1, 'black', 'black', C, r, s, tx, ty) # On top of others

# Draw labeled unknowns over unknown with respective colours (altered for 
# visibility) and black outline
iodata.show_data(redLabeled, 0, 1, 'darkred', 'black', C, r, s, tx, ty)
iodata.show_data(blueLabeled, 0, 1, 'lightblue', 'black', C, r, s, tx, ty)    

C.pack() # Pack the canvas in the window
top.mainloop() # Display window