# -*- coding: utf-8 -*-
"""
Programming for Data Science
Assignment 1 (K-Means Clustering)
@author u3141210 (Aleksandar Draskovic)
"""
import io_data_module as iodata
import tkinter

# Read data file and store values in list of tuples
dataList = iodata.read_data_file('datasets/data_2c_2d.txt')
                                 
# Print data list to check that all is well
print("Data list:\n", dataList, "\n")

# Get dimensions (D), number of data samples (N) set number of clusters (K)
# and set threshold (T) to 0 (or any small value)
D = len(dataList[0])
N = len(dataList)
K = 2 # 2c_2d and 2c_4d
#K = 4 # 4c_2d and 4c_4d
T = 0.1

# Print D and N to check that all is 
print("Number of dimensions:", D, "\n")
print("Number of data samples:", N, "\n")
print("Number of clusters:", K, "\n")

# Create K number of clusters with dimensions D and fill with random values
kcList = [] # List for cluster centre tuples
kcList = iodata.generate_K_cluster_centres(K, D)

# Print clusters to check all is well
print("List of randomly generated cluster centres:", kcList, "\n")

# =============================================================================
# Loop through data list and find nearest cluster centre for each sample
# =============================================================================

while True: # Loop until correct cluster centres are found
    
    # Create list of lists (clusters) for samples to occupy
    clustList = [[] for i in range(K)]
    i = 0 # iterator for appending cluster centre to the beginning their
          # respective clusters
    for j in clustList:
        j.append(kcList[i])
        i += 1
    
    for x in dataList: # for each data sample
        sampClustDistList = [(x), (c for c in kcList), []] # get sample,
                    # clusters, and empty list for distances. Convert distance list to tuple 
                    # when calculating distance
        # list for holding distances from sample to each cluster
        distList = []
        # for each cluster centre
        for y in kcList:
            dist = iodata.calculate_distance(x, y)
            distList.append(float(dist))
        sampClustDistList[2].extend((distList))
        sampClustDistList[2] = tuple(sampClustDistList[2])
        sampClustDistList[1] = tuple(sampClustDistList[1])
        smallestDist = min(sampClustDistList[2])
        centresList = sampClustDistList[1]
        clustIndex = sampClustDistList[2].index(smallestDist)
        correctClust = centresList[clustIndex]
        sampClust = [(sampClustDistList[0]), (correctClust)]
        for z in clustList:
            if sampClust[1] == z[0]:
                z.append(sampClust[0])
                
    for a in clustList: 
        del a[0]
    
    # # Create list of lists (clusters) for values to occupy
    # clustList = [[] for i in range(K)]
    # for x in dataList: # for each data sample
    #     distList = [] # list for holding tuples containing sample, cluster, and distance
    #     for y in kcList: # for each cluster centre
    #         dist = iodata.calculate_distance(x, y) # calculate distance from each sample to each cluster
    #         distList.append((x, y, float(dist))) # add sample, cluster and distance to list
    #         distList.sort(key=lambda tuple: tuple[-1]) # sort the list by distance
    #         nearestSample = distList[0] # first list item is the nearest sample
    #         clustList[kcList.index(nearestSample[1])].append(nearestSample[0])
    #         # append the sample to each cluster depending on the index value of the cluster centre
            
            
    # Calculate new cluster centre for each cluster
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

    # check if sum is equal to threshold, if so, break loop and draw
    if dSum < T:
        break
    else:
        # Set cluster centres to new cluster centres
        kcList = newKcList  
        print("Sum of cluster centre distances: ", dSum,"\n")
       
    # Set cluster centres to new cluster centres
    kcList = newKcList 
    
# ===========================================================6==================
# Format new cluster list to include each sample's respective
# cluster centre in order to draw lines from sample to cluster
# =============================================================================
    
print("New cluster centre list:", newKcList, "\n")    

# print("Cluster List:\n", clustList)

drawLineList = []
clustIndex = - 1
for a in clustList: # for each cluster
    drawClustList = []
    clustIndex = clustIndex + 1
    for b in a: # for each sample
        sampList = []
        centreList = []
        sampCentreList = []
        sampList = b
        centreList = newKcList[clustIndex]
        sampCentreList = [sampList, centreList]
        drawClustList.append(tuple(sampCentreList))
    drawLineList.append(drawClustList)   
    
# print("\nNew cluster centre list:\n", newKcList)    
# print("\nList for drawing samples to centres:\n", drawLineList)    
    
# =============================================================================
# Displaying the data
# =============================================================================

# Create window and canvas
window = tkinter.Tk()
cvs_width = 1920
cvs_height = 1080
canvas = tkinter.Canvas(window, bg = "white", height = cvs_height,
                        width = cvs_width)
# Set variables for drawing
r = 4 # Radius variable
ix = 0 # X sample index
iy = 1 # Y sample index
sx = 120 # X scale variable
sy = 120 # Y scale variable
s = 120 # Universal scale variable
tx = 550 # X translate variable
ty = 250 # Y translate variable


# # Set variables for transformation
# (sx, sy, tx, ty) = iodata.transform_data_for_canvas_display(dataList, idx=ix,
# idy=iy, canvas_height=cvs_height, canvas_width=cvs_width)

# (nx, ny, mx, my) = iodata.transform_data_for_canvas_display(newKcList, idx=ix,
# idy=iy, canvas_height=cvs_height, canvas_width=cvs_width)


# Draw lines from cluster samples to respecive cluster centres
iodata.draw_lines_from_centre_to_samples(drawLineList, 0, 1, 'grey', canvas, s, tx, ty)       

# Draw the data list
iodata.display_data(dataList, ix, iy, 'red', 'circle', canvas, r, sx, sy, tx, ty)

# Draw the new cluster centres
iodata.display_data(newKcList, ix, iy, 'blue', 'circle', canvas, r, sx, sy, tx, ty)


canvas.pack() # Pack the canvas in the window
window.mainloop() # Display window