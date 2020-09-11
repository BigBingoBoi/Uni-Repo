# -*- coding: utf-8 -*-
"""
Pattern Recognition and Machine Learning
Week 4 Tutorial (Wine Quality)
@author u3141210 (Aleksandar Draskovic)
"""
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
diabetes_dataset = pd.read_csv("datasets_228_482_diabetes.csv", sep = ",")

sn.heatmap(diabetes_dataset.corr(), annot=True)
plt.show()

# Extract features and a target
feature_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                   'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

X = diabetes_dataset[feature_columns] # Features
y = diabetes_dataset.Outcome # Target

# split X and y into training and testing datasets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
lr = LogisticRegression(C = 10)

# fit the model with the training data
lr.fit(X_train,y_train)

# Make a prediction for the testing data
y_pred = lr.predict(X_test)

# import the metrics class
from sklearn import metrics
from sklearn.metrics import classification_report

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred, average= 'weighted'))
print("Recall:", metrics.recall_score(y_test, y_pred, average = 'weighted'))
print("F1-score:", metrics.f1_score(y_test, y_pred, average = 'weighted'))

fpr, tpr, _ = metrics.roc_curve(y_test, y_pred)
auc = metrics.roc_auc_score(y_test, y_pred)

plt.plot(fpr, tpr, label = "auc="+str(auc))
plt.title('ROC curve for Diabetes classifier')
plt.xlabel('False positive rate (1-Specificity)')
plt.ylabel('True positive rate (Sensitivity)')
plt.legend(loc=4)
plt.show()

index = 0
misclassifiedIndexes = []
for label, predict in zip(y_test, y_pred):
    if label != predict:
        misclassifiedIndexes.append(index)
    index +=1
    
np.array(misclassifiedIndexes).T

def linear_regression(c):
    lr = LogisticRegression(C = c)
    fit_lr = lr.fit(X_train, y_train)
    predicted_lr = fit_lr.predict(X_test)
    cm_lr = metrics.confusion_matrix(y_test, predicted_lr)
    
    f1_sc = metrics.f1_score(y_test, predicted_lr, average = 'weighted')
    return f1_sc

c = 0.0001
c_values = []
f1_values = []

while c < 1000:
    f1_sc = linear_regression(c)
    c_values.append(c)
    f1_values.append(f1_sc)
    c = c*10
    
f1_lr = pd.DataFrame({
        "c": c_values,
        "f1": f1_values
})