# Preprocessing Bullshit
import pandas as pd
import numpy as np
import os
import glob
os.chdir("../_propcsv")

###############################
# DATA PREPROCESSING
###############################


# extension = 'csv'
# all_filenames = glob.glob('*.{}'.format(extension))
# all_filenames.sort(key=os.path.getmtime)
df = pd.read_csv('PropertySearchResults(19).csv')

# changing data types of numbers (str to numbers)
df['Property ID'] = df['Property ID'].values.astype(int)
df['Doing Business As'] = df['Doing Business As'].values.astype(str)

a = []
for num in df['Appraised Value']:
    # removing commas from numbers like 100,000
    a.append(int(num.replace(",", "")))
df['Appraised Value'] = a

# make zipcode new field


# zipcode = 78207
# df['Indexes'] = df['Property Address'].str.find(str(zipcode))
# df["Indexes"] = data[]
# print(df.head())

# previewing dataframe
# print(df.head())
# print(df.columns)
# for col in df.columns:
#     print(col)
#     print(type(df[col][0])) # read first entry of row
















###############################
# DATA ANALYSIS AND VISUALIZATION
###############################
import matplotlib.pyplot as plt
# df [col] [grab index of my NaN vals]
# grabbing only the homes
# homes = df['Doing Business As'][df['Doing Business As'] == 'nan']

homes = df[df['Doing Business As'] == 'nan']

# need to do these +/- 3 stds of the mean
plt.hist(homes['Appraised Value'][homes['Appraised Value'] < 1e6], bins=100)
plt.show()
plt.hist(homes['Appraised Value'][homes['Appraised Value'] >= 1e6], bins=100)
plt.show()

print(homes['Appraised Value'].describe())

# https://dash-building-blocks.readthedocs.io/en/latest/examples/multigraph.html


# cluster to separate into groups
# have a map where you can do graphs
# simple map with a histogram
# build a predictor, have a certain zip code,
# use training data, some of the addresses