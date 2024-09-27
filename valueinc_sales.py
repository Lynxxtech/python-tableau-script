# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:51:46 2024

@author: DE
"""

import pandas as pd

#file_name = pd.read_csv('dataset_name.csv', sep=';')


data = pd.read_csv('transaction.csv', sep=';')

# Summary of the data

data.info()

# Working with calculations

# Defining Variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchase = 6

# Mathematical Operations

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchase * ProfitPerItem

CostPerTransaction = CostPerItem * NumberofItemsPurchase

SellingPricePerTransaction = NumberofItemsPurchase * SellingPricePerItem

# CostPerTransaction Column Calculation
# CostPerTransaction  = CostPerItem * NumberofItemsPurchase
# Variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchase = data['NumberOfItemsPurchased']
CostPerTransaction = NumberofItemsPurchase * CostPerItem

# Adding a new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

# Sales Per Transaction Column

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Per Transanction column/ Calculation

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (Sales - Cost) / Cost

data['MarkUp'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

data['MarkUp'] = (data['ProfitPerTransaction']) / data['CostPerTransaction']

# Rounding MarkUp

roundmarkup = round(data['MarkUp'], 2)

# data['MarkUp'] = round(data['MarkUp'], 2)

data['MarkUp'] = roundmarkup

# Combining Data Fields (Date, month, year)

my_date = 'Day' + '-'+'Month'+'-'+'Year'

#my_date = data['Day'] + '-'

# Checking Column data type
print(data['Day'].dtype)

# Change Column Data type

day = data['Day'].astype(str)

print(day.dtype)

year = data['Year'].astype(str)
print(year.dtype)

my_date = day + '-' + data['Month']+'-' + year

data['Date'] = my_date


# Using split function to split the Clientkeyword field
# new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#Lets create 3 new columns for the split Clientkeyword field

data['ClientAge'] = split_col[0]

data['ClientType'] = split_col[1]

data['LengthofContract'] = split_col[2]


# Using The Replace Function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')

data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')


# Using the lower function to change Item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

# How to merge files

# Bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#Merging files: merge_df = pd.merge(df_old, df_new, on  ='key')


data = pd.merge(data, seasons, on  ='Month')

#Dropping Columns (Delete Columns)

# df = df.drop('column_name' , axis = 1)

data = data.drop('ClientKeywords' , axis = 1)

data = data.drop('Day' , axis = 1)

data = data.drop('Month' , axis = 1)

data = data.drop('Year' , axis = 1)

# Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)

































