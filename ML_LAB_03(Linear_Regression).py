ML_03_Linear_Regression 

#Import Libraries
import pandas as pd #Data manipulation and analysis.
import numpy as np # Numerical computations and array operations.
import matplotlib.pyplot as plt #Creating visualizations.
import seaborn as sns #Creating  Statistical visualizations.

# Read File
df=pd.read_csv('Temperature.csv')

#Data Pre-Processing
df.head()           #to view the first few rows.
df.shape            #to check the data dimensions (number of rows and columns).
df.info()           #to get information about data types and potential missing values.
df.isnull().sum() 
df.count()          #to check for missing values and column counts.
df.dtypes           #to check the data types of each column.

#input data
x=df['YEAR']
#output data
y=df['ANNUAL']

#Create Plot
plt.title('ANNUAL AVERAGE TEMPERATURE')
plt.xlabel('Year')
plt.ylabel('Annual Average Temperature')
plt.scatter(x,y)

#Re-shape to fit in model for training the algorithm  
x.shape
x=x.reshape(117,1)
x.shape

#LineraRegression Model import
from sklearn.linear_model import LinearRegression

#Create obbject of LinearRegression
regressor=LinearRegression()

#Fit Model to train algorithm 
regressor.fit(x,y)

#Model Parameter 
regressor.coef_ #slope
regressor.intercept_ #the point where the regression line crosses the y-axis.

#Predict Future Temperature
regressor.predict([[2030]])
predicted=regressor.predict(x)
predicted

#MAE
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y,predicted)

#MSE
from sklearn.metrics import mean_squared_error
mean_squared_error(y,predicted)

#R-Squre Error
from sklearn.metrics import r2_score
r2_score(y,predicted)

#Visulaization of LinearRegression with Actual & Predicted Data
plt.title('Annual Average Temperature')
plt.xlabel('Year')
plt.ylabel('Annual')
plt.scatter(x,y, label='Actual Data', color='r',marker='.')
plt.plot(y,predicted,label='Predicted Data',color='g')
plt.legend()

#Using Seaborn library Directly 
sns.regplot(x='YEAR',y='ANNUAL',data=df)

#THEORY 

/******************************************************************************************

Regression

Statistical method to model the relationship between variables.
Used to predict a continuous outcome variable.
Linear Regression

A type of regression where the relationship is modeled as a straight line.
Used to predict numerical values.
Logistic Regression

Used to model the probability of a binary outcome (e.g., yes/no, win/loss).
Outputs a value between 0 and 1, interpreted as probability.
MSE (Mean Squared Error)

Measures the average squared difference between predicted and actual values.
Lower MSE indicates better model fit.
MAE (Mean Absolute Error)

Measures the average absolute difference between predicted and actual values.
Less sensitive to outliers than MSE.
R-squared Error

Represents the proportion of variance in the dependent variable explained by the independent variables.
Higher R-squared indicates a better fit.  
Represents the proportion of variance in the annual temperature explained by the year variable.

******************************************************************************************/
