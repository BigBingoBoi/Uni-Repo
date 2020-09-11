# -*- coding: utf-8 -*-
"""
Programming for Data Science
Week 4 Tutorial (IO Data Module)
@author u3141210 (Aleksandar Draskovic)
"""
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

#Question 2
#define function
def find_nearest_neighbor(unknown_sample, data_list):
    distances = []
    for x, y in data_list:
        d = ((unknown_sample[0]-x)*(unknown_sample[0]-x) +
             (unknown_sample[1]-y) * (unknown_sample[1]-y))**0.5
        distances.append((x, y, d))
    distances.sort(key=lambda tuple: tuple[2])   
    nearest_d = distances[0]
    nearest_sample = nearest_d[0:2]
    return nearest_sample
#end function