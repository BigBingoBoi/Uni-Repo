# -*- coding: utf-8 -*-
"""
Pattern Recognition and Machine Learning
Week 3 Tutorial (Linear Regression Example)
@author u3141210 (Aleksandar Draskovic)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#metrics to evaluate the linear regression
from sklearn.metrics import mean_squared_error, mean_absolute_error

#split the data to train/trest dataset
from sklearn.model_selection import train_test_split

#import the linear regression
from sklearn.linear_model import LinearRegression


#read iris data
iris_dataset = pd.read_csv("iris.data", sep=',', names=["sepal_length", "sepal_width", "petal_length",
                                                "petal_width", "species"])

#define selected_columns
selected_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

#remove petal width from data
X = iris_dataset[selected_columns].drop(labels = 'petal_width', axis = 1)

#correct petal width values
y = iris_dataset['petal_width']

#split data into train/test dataseet with ratio 3/1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)


lre = LinearRegression()

#train the train data
lre.fit(X_train, y_train)

#predict on the test data
pred = lre.predict(X_test)


#Evaluate the prediction
print('Mean Absolute Error:', mean_absolute_error(y_test, pred))
print('Mean Squared Error:', mean_squared_error(y_test, pred))
print('Mean Root Squared Error:', np.sqrt(mean_squared_error(y_test, pred)))
abs(y_test-pred)


#Visualise the prediction
plt.scatter(X_test[["sepal_length"]], y_test, color = "red",
            label = "Actual petal_width")
plt.scatter(X_test[["sepal_length"]], pred, color = "green",
            label = "Predicted petal_width")
plt.legend()
plt.xlabel('Sepal Length')