# -*- coding: utf-8 -*-
"""
Programming for Data Science
Assignment 1 (IO module)
@author u3141210 (Aleksandar Draskovic)
"""
# Function to read data of any dimention and save to list of tuples 
def read_data_file(filename):
    dataset = [] # List for data tuples
    file = None
    try:
        f = open(filename, 'r')
        while True: # Read line-by-line until end of file
            line = f.readline()
            if len(line) == 0:
                break
            line = line.replace('\n', '') # Remove \n
            xdString = line.split(' ') # Split multidimentional coordinates by space
            sample = [float(x) for x in xdString] # Convert to float
            dataset.append(tuple(sample)) # Add to list as tuple
            
    except Exception as ex:
        print(ex.args)
    finally:
        if file:
            file.close()
    return dataset
    # End of function

            
# Function to draw data
def show_data(drawing_list, xi = 0, yi = 1, fillColour = None,
              outlineColour = None, canvas = None, r = 5, s = 150, tx = 300, ty = 200):
    for sample in drawing_list:
        x = sample[xi]
        y = sample[yi]
        x = x * s + tx
        y = y * s + ty
        if canvas != None:
            canvas.create_oval(x-r, y-r, x+r, y+r, fill=fillColour,
                               outline=outlineColour, width=2)
    # End of function
  
          
# Function to calculate distance between tuples
def calculate_distance(a, b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i]-b[i]) * (a[i]-b[i])
    dist = dist**0.5
    return dist