import codecademylib3

import pandas as pd

census = pd.read_csv('census_data.csv', index_col=0)

print(census.head())

print(census.dtypes)

print(census.birth_year.unique())

census['birth_year'] = census['birth_year'].replace('missing', 1967)
print(census['birth_year'].head())

census['birth_year'] = census['birth_year'].astype('int')

print(census['birth_year'].mean())

# converting type of columns to 'category'
census['higher_tax'] = census['higher_tax'].astype('category')

#  encoding
census['higher_tax'] = census['higher_tax'].cat.codes
print(census.higher_tax.unique)

# print out the median of the higher_tax variable
print(census['higher_tax'].median()) 

census = pd.get_dummies(census, columns = ['marital_status'] )

print(census.head())
