#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:25:23 2022

@author: yuerujin
"""

import pandas as pd

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep = ';')

#summary of the data
data.info()

#CostPerTransaction Column Calculation
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding a new column to a dataframe

data['CostPerTransaction'] = CostPerTransaction

#Sales per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * NumberofItemsPurchased

#Profit Calculation = Sales - Cost

data['ProfitPertransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPertransaction'] / data['CostPerTransaction']

#Rounding Marking

roundmarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'], 2)

#combining data fields

#checking columns data type
print(data['Day'].dtype)

#change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data['date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] # views the row with index = 0
data.iloc[:3] # first 3 rows
data.iloc[-5:] # last 5 rows

data.head(5) # first 5 rows
data.iloc[:,2] # all rows on the 2nd col
data.iloc[4,2] # 4th row and 2nd col

#using split to split the client keywords field
#new_var = column.str.split('sep', expand = True)

split_col =data['ClientKeywords'].str.split(',', expand = True)

#creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

# df = df.drop('columnname', axis = 1)
data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'], axis = 1)

#Export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)





















