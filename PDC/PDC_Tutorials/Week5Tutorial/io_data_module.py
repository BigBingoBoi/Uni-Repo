# -*- coding: utf-8 -*-
"""
Programming for Data Science
Week 5 Tutorial (IO module)
@author u3141210 (Aleksandar Draskovic)
"""
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


