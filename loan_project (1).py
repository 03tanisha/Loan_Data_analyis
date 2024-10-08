# -*- coding: utf-8 -*-
"""Loan_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IYy0JDizlxzPdXh8zjkl-U2ZFuth6BS9

# The main objective of this data analsis is to find the factors which play important role in loan approval
"""

# importing necc. libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')



# reading the dataset
df = pd.read_csv('/content/loan_train.csv')

# checking top 5 rows
df.head()

# checking columns
df.columns

# checking statistical measures
df.describe()

# checking null values
df.isnull().sum()

# dropping all the null values
df.dropna(inplace = True)

# checking null values again
df.isnull().sum()

# check data type
df.info()

# check no. of rows and columns
df.shape

# renaming the column
df.rename(columns = {'Married' : 'Marital_Status'},inplace = True)

df.rename(columns = {'Married_Status' : 'Marital_Status'},inplace = True)

"""#  Gender




"""

# plot the countplot
plt.figure(figsize = (8,5))
ax = sns.countplot(data = df, x = 'Gender')
ax.bar_label(ax.containers[0])
plt.title('Gender Distribution', size = 30, weight = 'bold',color= 'salmon')
plt.show()

"""*From this plot we can conclude that number of Males in the data are more than Females*

# Marital Status
"""

# plot the countplot
plt.figure(figsize = (5,5))
ax = sns.countplot(data = df, x = 'Marital_Status')
ax.bar_label(ax.containers[0])
plt.xlabel('Marital_Status', size= 20, color = 'Black')
plt.ylabel('Count', size = 20, color = 'Black')
plt.title('Marital Status',size = 30,color ='red')
plt.show()

"""*From the above we can conclude that count of Married People are more than the Unmarried People*

#  Dependents
"""

# plot the histogram
plt.figure(figsize=(5,6))
ax = sns.histplot(x=df['Dependents'],kde=True)
ax.bar_label(ax.containers[0])
plt.title('Dependents Distribution',size=25,color='purple')
plt.xlabel('Dependents',size=20,color='yellow')
plt.ylabel('Count',size=20,color='yellow')
plt.show()

df['Dependents']

#plot the countplot
df.groupby(['Dependents','Education']).count().head(15)

plt.figure(figsize = (10,6))
ax = sns.countplot(data = df, x = 'Dependents', hue = 'Education')
ax.bar_label(ax.containers[0])
plt.title('Dependents Distribution',size=25,color='brown')
plt.xlabel('Dependents',size=20,color='green')
plt.ylabel('Count',size=20,color='green')
plt.show()

"""From the above graph we can conclude:

1.   Most of the applicants who are Graduate have no dependents.

2.  The number of dependents decreases as the education level increases.

# Applicant Income
"""

df['ApplicantIncome'].head(15).mean()

df['ApplicantIncome'].head(15).median()

df['ApplicantIncome'].head(15).mode().iloc[0]

plt.figure(figsize=(9,5))
sns.histplot(x=df['ApplicantIncome'], kde=True)
plt.title('Applicant Income Distribution')
plt.xlabel('Applicant Income')
plt.ylabel('Count')
plt.show()

"""
This indicates that, it is a right-skewed graph,as majority of the applicants category falling towards left.

From the above plot we can conclude that most of the applicant's income is less than 3000."""

#group by Applicant income and co-applicant income
df[['ApplicantIncome','CoapplicantIncome']].groupby(by='ApplicantIncome').sum().head(15)

"""We can conclude that most of the Coapplicant's Income is more than the Applicant's Income"""

# plot the boxplot

plt.figure(figsize=(4,3))
sns.boxplot(data = df[['ApplicantIncome', 'CoapplicantIncome']])
plt.title('ApplicantIncome vs CoapplicantIncome')
plt.ylabel('Income')
plt.show()

"""*Insights*



* We can conclude that both applicant income's and co-applicant income's have Outliers.But most of the Outliers are present in the applicant's income


*  These Outliers represent the Unusual Income of the applicants.


* The boxplot indicates that both ApplicantIncome and CoapplicantIncome
 are positively skewed (right-skewed), with a longer right whisker and the median closer to the bottom of the box.

# Handling Outliers
"""

# removing outliers from the Applicant income

df = pd.DataFrame(df,columns=['ApplicantIncome'])

Q1 = df['ApplicantIncome'].quantile(0.25)
Q3 = df['ApplicantIncome'].quantile(0.75)
IQR = Q3 - Q1

#calculating the upper and the lower bound
upper_bound = Q3 + 0.5 * IQR
lower_bound = Q1 - 0.5 * IQR

df_filtered = df[(df['ApplicantIncome'] >= lower_bound) & (df['ApplicantIncome'] <= upper_bound)]

print('original dataset')
print(df)
print('\nFiltered dataset')
print(df_filtered)

# removing outliers from the Co-applicant income

df = pd.DataFrame(df,columns=['CoapplicantIncome'])

Q1 = df['CoapplicantIncome'].quantile(0.25)
Q3 = df['CoapplicantIncome'].quantile(0.75)
IQR = Q3 - Q1

#calculating the upper and the lower bound
upper_bound = Q3 + 0.5 * IQR
lower_bound = Q1 - 0.5 * IQR

df_filtered = df[(df['CoapplicantIncome'] >= lower_bound) & (df['CoapplicantIncome'] <= upper_bound)]

print('original dataset')
print(df)
print('\nFiltered dataset')
print(df_filtered)

"""Hence, Removed the Outliers from both the Income .

# Loan Amount
"""

# cheking the unique values
df['Loan_Amount_Term'].unique()

#plot countplot

plt.figure(figsize=(10,7))
ax = sns.countplot(data = df, x = 'Loan_Amount_Term')
ax.bar_label(ax.containers[0])
plt.title('Loan Amount Term', size = 30, color = 'red')
plt.xlabel('Term', size = 20, color = 'green')
plt.ylabel('Count', size = 20, color = 'green')
plt.show()

"""# From this we can conclude that majority of the applicants took Loan for the period of 360 months"""

df['LoanAmount'].unique()

"""## Density plot of the Loan Amount"""

plt.figure(figsize =(10,7))
ax = sns.histplot(df['LoanAmount'],kde=True)
plt.title('Density plot of Loan Amount', size = 30, color = 'salmon')
plt.xlabel('Loan Amount', size = 20 , color = 'red')
plt.ylabel('Density', size = 20, color = 'red')
plt.show()

"""### From this plot we can conclude that:


1. It is a right-skewed plot, which means that the most people take out smaller loans.


2. There is a peak around 100, which indicating that 100 is a common loan amount.


3. Few people take loan of large amounts.

### Relation B/W Edcuation and Loan Status
"""

df_grouped = df.groupby(['Education', 'Loan_Status'])['Loan_Status'].count().unstack()

# plotting barchart

df_grouped.plot(kind = 'bar',stacked = True)
plt.title('Loan Status by Education')
plt.xlabel('Education')
plt.ylabel('Proportion')
plt.show()

"""From the graph we can conclude that Graduates have higher chance of getting laon approval as compare to the non-graduates.

This suggests that education level is significant facotr in loan approval decisions.

### Relation between Loan Status and Property Area
"""

# group by the Property Area and Loan Status

df_grouped = df.groupby(['Property_Area', 'Loan_Status'])['Loan_Status'].count().unstack()

# plot the  barchart


df_grouped.plot(kind = 'bar',stacked = True)
plt.title('Loan Status by Property Area',size = 30, color = 'salmon')
plt.xlabel('Property Area',size = 20,color = 'purple')
plt.ylabel('Proportion',size = 20, color = 'purple')
plt.show()

"""### From this plot we can conclude that majority of the loan is approved in the semiurban area.

### The loan approval rates are lowest in the Rural areas.

# Credit History
"""

df['Credit_History'].unique()

df['Credit_History'].value_counts()

# plot the barchart

ax = df['Credit_History'].value_counts().plot(kind = 'bar')
ax.bar_label(ax.containers[0])
plt.title('Credit History',size = 30,color = 'red')
plt.xlabel('Credit History',size = 20, color = 'black')
plt.ylabel('Counts',size = 20, color = 'black')
plt.show()

pd.crosstab(df['Credit_History'], df['Loan_Status'])

"""### Relation Between Loan status and Credit History"""

grouped_data = df.groupby(['Credit_History', 'Loan_Status'])['Loan_Status'].count().unstack()

# plotting barchart

ax = grouped_data.plot(kind = 'bar', stacked = True)
ax.bar_label(ax.containers[0])
plt.title('Loan Status by Credit History',size = 30, color = 'red')
plt.xlabel('Credit History',size = 20, color = 'black')
plt.ylabel('Proportion',size = 20, color = 'black')
plt.show()

"""### From this we can conclude that the applicants who have Credit card, only they are getting loan approvals.

### Only very few of them get the loan approval who doesn't have credit card.

# Conclusion

### This data analysis delved into a loan dataset, which aims to uncover the factors that play a crucial role in the loan approval. Through Visualizations and Statistical meausures, several key insights emerged.



1. DEMOGRAPHICS



* Gender : Through the Visualizations,I have found the gender imbalance,with  
a larger proportion of the Male applicants as compared to the Females applicants.

* Marital Status : Most of the people who applied for the loans were married.
This might mean that married people are more likely to apply for the loan.

* Dependents : People with higher education levels tended to have the fewer
children. This could be because education influences family planning decisions and financial stabiclity.

* Education : Graduates had the higher chance of getting loan approvals as compare to the non-graduates.



2. FINANCIALS



* Credit History : Applicants with a credit history (meaning they've used credit cards or loans before) were much more likely to get approved. This suggests lenders see a credit history as an important indicator of responsibility.


(ii) Only Few of them get loan approvals who doesn't have credit cards.



* Income : Dataset represents Applicant and Co-applicant's income. Most applicants had an income less than 3000.


(i) Co-applicants often had a higher income than the main applicant.




* Loan Amount : Most people applied for the smaller loans, with around 100.There's a high demand for the smaller loans, possibly for the personal expenses or small business needs as compare to the higher loan amounts.


3. Location


 (i) Property Area : People living in semi-urban areas had the highest loan approval rates, while those in rural areas had the lowest. This might reflect differences in economic opportunities or property values in different locations.

* Loan Term : The most common loan term was 360 months(30years). This is a typical term for the larger loans like the homeloans.


* The analysis also highlighted the importance of visualizing data.By creating charts and graphs, it was easier to understand patterns and relationships in the data, such as the connection between education and loan approvals or the distribution of loan amounts.



# Key Takeaway

### The analysis showed that factors like education,credit history,and location play a significant role in approval decisions. Lenders likely use this information to assess the risk of lending money to different applicants.
"""