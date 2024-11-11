ML_LAB_04_Email

#import libraries 

import pandas as pd 
import numpy as np

#Read file 
df=pd.read_csv('Spam.csv',encoding='latin-1')

#Data Pre-processing
df.head()
df.shape
df.info()
df.describe()
df.count

#Spam & Ham in Binary 

df['Spam']=df['v1'].apply(lambda x:1 if x=='Spam' else 0)
df

#Assign x & y Values 

x=df['v2']
y=df['Spam']

#Cross-Validation 

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test  = train_test_split(x,y,random_forest=0,test_size=0.25)

#Text Data to Numerical Data

from sklearn.feature_extraction.text import CountVectorizer 
v = CountVectorizer()
x_train = v.fit_transform(x_train.values)
x_train.toarray()[ :2]

x_test = v.transform(x_test)

#Implement naive_bayes Algorithm 

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(x_train,y_train)

#Prediction 
y_pred = model.predict(x_test)

from sklearn.metrics import ConfusionMatrixDisplay,accuracy_score,classification_report 
ConfusionMatrixDisplay.from_prediction(y_test,y_pred)
y_test.value_counts()
print(classification_report(y_test,y_pred))
accuracy_score(y_test,y_pred)

#Import RandomForestClassifier

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(x_train,y_train)

#Prediction 
y_pred = rf.predict(x_test)

ConfusionMatrixDisplay.from_prediction(y_test,y_pred)
y_test.value_counts()
print(classification_report(y_test,y_pred))
accuracy_score(y_test,y_pred)

#Hyper Parameter Tuning 

from sklearn.model_selection import GridSearchCV

param_grid = {'criterion':['gini','entropy'],'max_features':['sqrt','log2'],
              'random_state':[0,1,2,3,4],
              'class_weight':['balanced','balanced_subsample']}
              
grid = GridSearchCV(rf,param_grid=param_grid,cv=5,scoring='accuracy')              
             
grid.fit(x_train,y_train)             
              
