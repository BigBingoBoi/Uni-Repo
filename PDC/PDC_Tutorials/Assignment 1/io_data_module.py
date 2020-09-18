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

#Function to generate K cluster centres at random
def generate_K_cluster_centres(K, D):
    cluster_centre_list = []
    for k in range(K):
        cluster_centre = []
        for d in range(D):
            cluster_centre.append(k + d)
        cluster_centre_list.append(cluster_centre)
    return cluster_centre_list
#end of function

            
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
            

# Updated draw function to accomodate transformation
def display_data(data_list, xi=0, yi=1, colour='red', shape='circle', canvas=None, r=5, sx=150, sy=150, tx=300, ty=200):
    for sample in data_list:
        x = sample[xi]
        y = sample[yi]
        print
        x = x*sx + tx 
        y = y*sy + ty
        if canvas != None:
            if shape == 'circle':
                canvas.create_oval(x-r, y-r, x+r, y+r, outline = colour, fill=colour)
            elif shape == 'square':
                canvas.create_rectangle(x-r, y-r, x+r, y+r, outline=colour, fill=colour)
            elif shape == 'triangle':
                canvas.create_polygon(x, y-r, x-r, y+r, x+r, y+r, outline=colour, fill=colour)
            else: #if input shape is unknown, draw circle
                canvas.create_oval(x-r, y-r, x+r, y+r, outline = colour, fill=colour)
#end of function
            
            
# # Replaced with new one below
# def draw_lines_from_centre_to_samples(new_centre_list, samples_in_centre_list, xi=0, yi=1, colour='grey', 
#                                       canvas=None, r=5, s=150, tx=300, ty=200):
#     for centre in new_centre_list:
#         x = centre[xi]
#         y = centre[yi]
#         x = x*s + tx
#         y = y*s + ty
#         for sample in samples_in_centre_list:
#             a = sample[xi]
#             b = sample[yi]
#             a = a*s + tx
#             b = b*s + ty
#             if canvas != None:
#                 canvas.create_line(x, y, a ,b, fill = colour)
# #end of function
  
# add new line function here  
def draw_lines_from_centre_to_samples(drawList, ix=0, iy=1, colour='grey', 
                                      canvas=None, s=150, tx=300, ty=200):
    for a in drawList: # for each cluster
        print("\nDrawing lines to cluster #", drawList.index(a))
        for b in a: # for each (sample, centre) tuple
            sample = b[ix]
            cluster = b[iy]
            sX = sample[ix]
            sY = sample[iy]
            cX = cluster[ix]
            cY = cluster[iy]
            sX = sX*s + tx
            sY = sY*s + ty
            cX = cX*s + tx
            cY = cY*s + ty
            if canvas != None:
                # canvas.create_line(x, y, a ,b, fill = colour)
                canvas.create_line(sX, sY, cX, cY, fill = colour)
#end of function
                
            
#Function to transform data to display on canvas
def transform_data_for_canvas_display(data_list, idx=0, idy=1, canvas_width=800, canvas_height=600):
    #data_list is a list of nD samples, n > 2
    maxW = -1000000.0 #max width
    minW = 1000000.0 #min width
    maxH = -1000000.0 #max height
    minH = 1000000.0 #min height
    for sample in data_list: 
        if maxW < sample[idx]:
            maxW = sample[idx]
        if minW > sample[idx]:
            minW = sample[idx]
        if maxH < sample[idy]:
            maxH = sample[idy]
        if minH > sample[idy]:
            minH = sample[idy]
    sx = canvas_width / (maxW - minW) 
    tx = canvas_width * minW / (minW - maxW) 
    sy = canvas_height / (maxH - minH) 
    ty = canvas_height * minH  / (minH - maxH) 
    return (sx, sy, tx, ty)

  
          
# Function to calculate distance between tuples
def calculate_distance(a, b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i]-b[i]) * (a[i]-b[i])
    dist = dist**0.5
    return dist