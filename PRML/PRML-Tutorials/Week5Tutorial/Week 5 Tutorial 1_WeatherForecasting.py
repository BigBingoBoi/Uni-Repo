# -*- coding: utf-8 -*-
"""
Pattern Recognition and Machine Learning
Week 5 Tutorial (Part 1: Weather Forecasting)
@author u3141210 (Aleksandar Draskovic)
"""
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.metrics import classification_report

# Assigning features and label variables
weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast',
           'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']

temp = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 
        'Mild', 'Mild', 'Mild', 'Hot', 'Mild']

humid = ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 
         'normal', 'normal', 'normal', 'high', 'normal', 'high']

windy = [False, True, False, False, False, True, True, False, False, False, 
         True, True, False, True]

play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 
        'Yes', 'Yes', 'No']

# Import LabelEncoder
from sklearn import preprocessing
# creating LabelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels
weather_encoded = le.fit_transform(weather)
temp_encoded = le.fit_transform(temp)
humid_encoded = le.fit_transform(humid)
windy_encoded = le.fit_transform(windy)

play_encoded = le.fit_transform(play)

features = pd.DataFrame(np.array([weather_encoded, temp_encoded, humid_encoded,
                                  windy_encoded]).T, columns = ['Weather', 
                                  'Temperature', 'Humidity', 'Windy'])

X = list(zip(weather_encoded, temp_encoded, humid_encoded, windy_encoded))

#print(X)

#get labels
y = play_encoded

#Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,
                                                    random_state=1)
# 70% training, 30% test

#print(X_test)

# Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

# Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(X_train, y_train)

# Predict output
y_pred = model.predict(X_test)
print(f'"Predicted Value:" {y_pred}')

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred, average = 'weighted'))
print("Recall:",metrics.recall_score(y_test, y_pred, average = 'weighted'))
print("F1-score:",metrics.f1_score(y_test, y_pred, average = 'weighted'))

metrics.confusion_matrix(y_test, y_pred)





