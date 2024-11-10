ML_02_Classification

#import libraries

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Read file 
df=pd.read_csv('Admission.csv')

#Data Pre-Processing
df.head()
df.columns
df.shape
df.isnull().sum()

#Binarization
from sklearn.preprocessing import Binarizer
bi=Binarizer(threshold=0.75)
df['Chance of Admit ']=bi.fit_transformation['Chance of Admit ']

df.head()

#data input #drop
x=df.drop(['Chance of Admit '],axis=1)
y=df['Chance of Admit ']

#call
x
y=y.astype('int')
y

#Visulaization of ['Chance of Admit ']
sns.countplot(x=y);

#Cross-Validation
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=0.25)

x_train.count
x_test.count

#import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

#Create object
classifier=DecisionTreeClassifier()

#Train object
classifier.fit(x_train,y_train)

#Prediction
y_pred=classifier.predict(x_test)
y_pred

#Create DataFrame
result=pd.DataFrame({'Actual':y_test,'Predicted':y_pred})
result

#Confusion Matrix , Accuracy_score , Classification_report
from sklearn.metrics import ConfusionMatrixDisplay,accuracy_score,classification_report

ConfusionMatrixDisplay.from_predictions(y_test,y_pred)
accuracy_score(y_test,y_pred)
print(classification_report(y_test,y_pred))

#Tree Plot
from sklearn.tree import plot_tree
plt.figure(figsize=(12,12))
plot_tree(classifier,filled=True,round=True,fontsize=12,feature_names=x.column,class_names=['NA','AD'])

/******************************************************************************************
 Decision Tree Explained :- 

 A Decision Tree Classifier is a supervised machine learning algorithm that works by
 dividing the data into smaller subsets based on a series of sequential "yes" or "no" 
 questions about the features. It builds a tree-like structure where each internal 
 node represents a question, each branch corresponds to an answer, and each leaf 
 node represents the predicted class label. Decision Trees are known for their
 interpretability, which allows you to understand the decision-making process 
 of the model.
 
******************************************************************************************/
 
 