# -*- coding: utf-8 -*-
"""
Pattern Recognition and Machine Learning
Week 3 Tutorial (Wine Quality)
@author u3141210 (Aleksandar Draskovic)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error, mean_absolute_error

#split the data into train/test dataset
from sklearn.model_selection import train_test_split

#import the linear regression
from sklearn.linear_model import LinearRegression

#read the wine quality data
wine_red_dataset = pd.read_csv("winequality-red.csv", sep=';')
wine_white_dataset = pd.read_csv("winequality-white.csv", sep=';')

wine_dataset = pd.concat([wine_red_dataset, wine_white_dataset])

# =============================================================================
# #define selected columns
# selected_columns = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
#                     "free sulfur dioxide", "total sulfur dioxide", "density", "pH",
#                     "sulphates", "alcohol", "quality"]
# =============================================================================

#remove quality from data
X = wine_dataset.drop(labels = 'quality', axis = 1)

#actual quality values
y = wine_dataset['quality']

#prepare data for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,
                                                    random_state = 1)

#training with linear regression model
lre = LinearRegression()

#train the train data
lre.fit(X_train, y_train)

#predict on the test data
pred = lre.predict(X_test)

#Evaluate the prediction
print('Mean Absolute Error: ', mean_absolute_error(y_test, pred))
print('Mean Squared Error: ', mean_squared_error(y_test, pred))
print('Mean Root Squared Error: ', np.sqrt(mean_squared_error(y_test, pred)))
abs(y_test-pred)

#print actual wine quality vs predicted quality
print(pd.DataFrame({'Actual': y_test, 'Predicted': pred}))

#print weight and coefficients
print(lre.intercept_)
print(lre.coef_)

#visualise the output for the feature "Citric Acid"
plt.scatter(X_test[['citric acid']], y_test, color = "red",
            label = "Actual Wine Quality")
plt.scatter(X_test[['citric acid']], pred, color = "green",
            label = "Predicted Wine Quality")
plt.legend()
plt.xlabel('Volatile Acidity')



