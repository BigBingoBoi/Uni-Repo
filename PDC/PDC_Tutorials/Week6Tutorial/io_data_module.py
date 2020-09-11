# -*- coding: utf-8 -*-
"""
Programming for Data Science
Week 6 Tutorial (IO module)
@author u3141210 (Aleksandar Draskovic)
"""
# for question 1 and 2
# MAKE SURE IN THE ASSIGNMENTS TO HAVE A FUNCTION THAT CAN READ ANY NUMBER OF COLUMNS
# e.g. sample = [float(x) for x in xystring]
# above wont work if all aren't float, if you know the last is label then 'label = xystring[-1]'
# check week 4 answers and follow the assignments sheet "algorithm" (psuedocode)
# have a function for scaling the canvas and dots (check canvas for post)


def read_multi_dim_data(filename):
    dataset = []
    file = None
    try:
        file = open(filename, 'r')
        while True:
            line = file.readline()
            if len(line) == 0: 
                break
            dim = line.split(',')
            dataset.append((float(dim[0]), float(dim[1]),
                            float(dim[2]), float(dim[3])))
    except Exception as ex:
        print(ex.args)
    finally:
        if file:
            file.close()
    return dataset

# for question 3
#Function to read 2D data from file and save data to a list of tuples
def read_data_file(filename):
    dataset = [] #dataset is a python list 
    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0: #end of file
                break
            line = line.replace('\n', '') #remove end of line \n character
            xystring = line.split(' ') #x y coordinates in string format 
            #use split function to separate x & y strings then 
            #use float function to convert x & y strings to x & y numbers and 
            #add them as a tuple (x, y) to dataset that is a list
            dataset.append((float(xystring[0]), float(xystring[1])))
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
    return dataset
#end of function
