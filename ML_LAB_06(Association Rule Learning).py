ML_LAB_06_Association_Rule_Mining

#install mlxtend

!pip install mlxtend

#import 

import pandas as pd 
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules

#Read file 

df=pd.read_csv('Market_Basket_Optimization',header=None)

#Data Preprocessing

df.head()
df.shape
len(df)

#Apply TransactionEncoder

df = df.apply(lambda row: list(row.dropna()), axis=1).tolist()
te = TransactionEncoder()
x = te.fit_transform(df)

x 

#Create DataFrame 

df=pd.DataFrame(x,columns=te.coumns_)

df.head()

#apriori rules 
#1. frequent items 

freq_itemset = apriori(df,min_support=0.01,colnames=True)
freq_itemset

#2.Find the rules 

supports=freq_itemset['support'].values

rules=association_rules(freq_itemset,metric='confidence',min_threshold=0.1,support_only=False,num_itemsets=supports)
rules

#Generate Rules 

rules = rules[['antecedents','consequents','support','confidence']]
rules.head()

#Recommendation 

rules[rules['antecedents']=={'burgers'}]['consequents']

/******************************************************************************************/

* Association Rule Mining is a data mining technique used to discover 
relationships between items in a dataset. 
It identifies frequent patterns or co-occurrences of items, 
often represented as "If-Then" rules.

* Support: The frequency of occurrence of an itemset in the dataset.
Confidence: The probability of the consequent given the antecedent.
Lift: The ratio of the observed support of the rule to the expected 
support if the items were independent. It measures the strength of 
the association between the antecedent and the consequent.

*  The Apriori algorithm is a popular algorithm for mining frequent itemsets. 
It uses a bottom-up approach, starting with frequent itemsets of size 1 and 
iteratively generating larger frequent itemsets.
It prunes candidate itemsets that cannot be frequent based on the anti-monotone property of support.

* The TransactionEncoder class is used to convert the transaction data into a binary matrix, 
where each row represents a transaction and each column represents an item. 
It assigns a binary value of 1 if the item is present in the transaction and 0 otherwise

/******************************************************************************************/

