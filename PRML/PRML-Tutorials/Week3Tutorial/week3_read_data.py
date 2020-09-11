# -*- coding: utf-8 -*-
"""
Pattern Recognition and Machine Learning
Week 3 Tutorial (read_data)
@author u3141210 (Aleksandar Draskovic)
"""
import pandas as pd
import matplotlib.pyplot as plt

#read iris data
iris = pd.read_csv("iris.data", sep=',', names=["sepal_length", "sepal_width", "petal_length",
                                                 "petal_width", "species"])

