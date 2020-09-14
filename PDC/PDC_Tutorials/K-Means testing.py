# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:48:29 2020

@author: Aleks
"""
# Function to draw data
import tkinter
import io_data_module as iodata

K = 4
D = 4

dataList = [(1, 2, 7, 5),(5, 6, 2, 3),(9, 5, 5, 6),(2, 9, 3, 5),(3, 1, 6, 8),
            (7, 6, 1, 2),(6, 2, 1, 9),(2, 2, 2, 3),(8, 9, 1, 2),(4, 2, 2, 4),
            (8, 5, 4, 3),(9, 4, 2, 5)]

clusterList = [(1, 1, 2, 2), (1, 9, 7 ,9), (9, 1, 3 ,4), (9, 9, 7 ,3)]

drawLineList = [[((1, 2, 7, 5), (1, 1, 2, 2)), ((5, 6, 2, 3), (1, 1, 2, 2)), ((9, 5, 5, 6), (1, 1, 2, 2))], # first cluster
                [((2, 9, 3, 5), (1, 9, 7 ,9)), ((3, 1, 6, 8), (1, 9, 7 ,9)), ((7, 6, 1, 2), (1, 9, 7 ,9))], 
                [((6, 2, 1, 9), (9, 1, 3 ,4)), ((2, 2, 2, 3), (9, 1, 3 ,4)), ((8, 9, 1, 2), (9, 1, 3 ,4))], 
                [((4, 2, 2, 4), (9, 9, 7 ,3)), ((8, 5, 4, 3), (9, 9, 7 ,3)), ((9, 4, 2, 5), (9, 9, 7 ,3))]] # second cluster

print("Draw Line List:", drawLineList, "\n")
# print("Draw Line List[0:K]:", drawLineList[0:K], "\n")
# print("Draw Line List[0]:", drawLineList[0], "\n")
# print("Draw Line List:", drawLineList[0[0]], "\n")

for a in drawLineList: # for each cluster
    print("\nCluster:", a)
    for b in a:
        print("Outer tuple:", b) # for each sample, centre tuple
        for c in b:
            print("Inner tuple:", c) # for each individual tuple
            for d in c:
                print("Sample:", d) # for each individual value`
                


def draw_lines_from_centre_to_samples(drawList, ix=0, iy=1, colour='grey', 
                                      canvas=None, s=150, tx=300, ty=200):
    for a in drawList: # for each cluster
        print("\nDrawing lines to cluster #", drawList.index(a))
        for b in a: # for each (sample, centre) tuple
            sample = b[ix]
            cluster = b[iy]
            print("sample:", sample)
            print("cluster:", cluster)
            sX = sample[ix]
            sY = sample[iy]
            cX = cluster[ix]
            cY = cluster[iy]
            print("sX:", sX)
            print("sY:", sY)
            print("cX:", cX)
            print("cY:", cY)
            sX = sX*s + tx
            sY = sY*s + ty
            cX = cX*s + tx
            cY = cY*s + ty
            print("sX after scale:", sX)
            print("sY: after scale:", sY)
            print("cX: after scale:", cX)
            print("cY: after scale", cY)
            if canvas != None:
                # canvas.create_line(x, y, a ,b, fill = colour)
                canvas.create_line(sX, sY, cX, cY, fill = colour)
#end of function
            
# =============================================================================
# Drawing section            
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
sx = 60 # X scale variable
sy = 60 # Y scale variable
s = 60 # Universal scale variablwe
tx = 300 # X translate variable
ty = 200 # Y translate variable

# Draw the lines
draw_lines_from_centre_to_samples(drawLineList, 0, 1, 'grey', canvas, s, tx, ty)   
        
# Draw the data list
iodata.display_data(dataList, ix, iy, 'red', 'circle', canvas, r, sx, sy, tx, ty)

# Draw the new cluster centres
iodata.display_data(clusterList, ix, iy, 'blue', 'circle', canvas, r, sx, sy, tx, ty)


canvas.pack() # Pack the canvas in the window
window.mainloop() # Display window
            
