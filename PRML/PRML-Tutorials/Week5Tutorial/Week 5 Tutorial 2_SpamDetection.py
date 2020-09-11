# -*- coding: utf-8 -*-
"""
Pattern Recognition and Machine Learning
Week 5 Tutorial (Part 2: Spam Detection)
@author u3141210 (Aleksandar Draskovic)
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix

spam_dataset = pd.read_csv("spam.csv", sep = ",", encoding="latin-1")
spam_dataset.info()

cv = CountVectorizer()

cv.fit_transform([spam_dataset["v2"][82]])
cv.vocabulary_

features = cv.fit_transform(spam_dataset["v2"])

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    spam_dataset["v1"],
                                                    train_size = 0.8,
                                                    random_state = 0)

model = MultinomialNB()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

score = model.score(X_test, y_test)
print(score)
print(confusion_matrix(y_test, y_pred))

# Display Misclassified messages with Predicted Labels
index = 0
misclassifiedIndexes = []
for label, predict in zip(y_test, y_pred):
    if label != predict:
        misclassifiedIndexes.append(index)
    index += 1
    
misclassifiedEmailText = []

for badIndex in misclassifiedIndexes:
    misclassifiedEmailText.append([y_pred[badIndex],
                                   spam_dataset["v2"][badIndex]])
    
print(pd.DataFrame(misclassifiedEmailText, columns = ['Wrong Label', 'Email Test']))
