# -*- coding: utf-8 -*-
"""
Programming for Data Science
Assignment 1 (K-Means Clustering)
@author u3141210 (Aleksandar Draskovic)
"""
import io_data_module as iodata
import tkinter
import random

# Read data file and store values in list of tuples
dataList = iodata.read_data_file('datasets/data_2c_2d.txt')
                                 
# Print list to check that all is well
print("Data list:\n", dataList, "\n")

# Get dimensions (D), number of data samples (N) set number of clusters (K)
# and set threshold (T) to 0 (or any small value)
D = len(dataList[0])
N = len(dataList)
K = 2 # 2c_2d and 2c_4d
#K = 4 # 4c_2d and 4c_4d
T = 0

# Print D and N to check that all is 
print("Number of dimensions:", D, "\n")
print("Number of data samples:", N, "\n")
print("Number of clusters:", K, "\n")

# Create K clusters number of clusters with dimensions D and fill with random 
# values
kcList = [] # List for cluster centre tuples
dRange = list(range(0, D)) # Range for multidimension accomodation
i = 0
while i < K:
    sample = [float(random.randrange(-2, 8)) for x in dRange]
    kcList.append(tuple(sample))
    i = i + 1

# Print clusters to check all is well
print("List of randomly generated cluster centres:", kcList, "\n")

# =============================================================================
# Loop through data list and find nearest cluster centre for each sample
# =============================================================================


checkDSum = 100 # initial variable for holding sum of distance between old and new cluster centres
while checkDSum > T: # While the sum is greater than the threshold
    # Create draw line list for final clusters
    # drawLineList = [[] for i in range(K)]
    
    # Create list of lists (clusters) for values to occupy
    clustList = [[] for i in range(K)]
    for x in dataList: # for each data sample
        distList = [] # list for holding tuples containing sample, cluster, and distance
        # sampTupList = [] # list for holding sample
        # clustTupList = [] # list for holding cluster
        # sampTupClustTup = [] # list for holding tuple of sample and cluster tuples
        for y in kcList: # for each cluster centre
            dist = iodata.calculate_distance(x, y) # calculate distance from each sample to each cluster
            distList.append((x, y, float(dist))) # add sample, cluster and distance to list
            # print(distList)
            distList.sort(key=lambda tuple: tuple[-1]) # sort the list by distance
            nearestSample = distList[0] # first list item is the nearest sample
            clustList[kcList.index(nearestSample[1])].append(nearestSample[0])
            # sampTupList.append(nearestSample[0])
            # clustTupList.append(nearestSample[1])
            # sampTupClustTup = [tuple(sampTupList), tuple(clustTupList)]
            # drawLineList[kcList.index(nearestSample[1])].append(tuple(sampTupClustTup))
            # append the sample to each cluster depending on the index value of the cluster centre
            
    newKcList = [] # list for holding new cluster centre      
    for j in clustList: # for each cluster
        clustSum = [] # Variable for holding sum of samples tuple
        clustLength = len(j) # Variable for holding length of cluster
        clustSum = [sum(y) for y in zip(*j)] # Get sum of cluster samples
        newKcList.append([z / clustLength for z in clustSum]) # Get average
        
    newKcList = [tuple(l) for l in newKcList] # Convert to tuple

    # Print new cluster centre to check all is well
    # print("New Cluster centre list:", newKcList, "\n")

    # Get distance from new to old cluster centre
    dSum = 0 # Variable for holding sum of distances
    e = 0 # Iterator
    while e < K:
        dSum = dSum + iodata.calculate_distance(kcList[e], newKcList[e])
        e += 1

    # Assign cluster centre distance sum value to check against threshold
    checkDSum = dSum
    print("checkDSum:", checkDSum, "\n")
    # Set cluster centres to new cluster centres
    kcList = newKcList 
    
    # Once threshold is reached, loop will break


# print("\ndrawLineList:", drawLineList)
# =============================================================================
# Displaying the data
# =============================================================================

# Create window and canvas
window = tkinter.Tk()
cvs_width = 800
cvs_height = 600
canvas = tkinter.Canvas(window, bg = "white", height = cvs_height,
                        width = cvs_width)
# Set variables for drawing
r = 4 # Radius variable
ix = 0 # X sample index
iy = 1 # Y sample index
s = 150 # Scale variable

# Set variables for transformation
(sx, sy, tx, ty) = iodata.transform_data_for_canvas_display(dataList, idx=ix,
idy=iy, canvas_height=cvs_height, canvas_width=cvs_width)

(nx, ny, mx, my) = iodata.transform_data_for_canvas_display(newKcList, idx=ix,
idy=iy, canvas_height=cvs_height, canvas_width=cvs_width)


# Draw lines from cluster samples to respecive cluster centres

# print("Cluster:", a, "\n")
# iodata.draw_lines_from_centre_to_samples(newKcList, , 0, 1, 'grey', 
#                                          canvas, r, s, tx, ty)
    
testList = [20, 80, 67, 43]

canvas.create_line(testList, fill='grey')
     
        
# Draw the data list
iodata.display_data(dataList, ix, iy, 'red', 'circle', canvas, r, sx, sy, tx, ty)

# Draw the new cluster centres
iodata.display_data(newKcList, ix, iy, 'blue', 'circle', canvas, r, nx, ny, mx, my)


canvas.pack() # Pack the canvas in the window
window.mainloop() # Display window