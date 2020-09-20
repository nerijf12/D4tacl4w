import os
import glob
import pandas as pd
import pickle
import numpy as np
import matplotlib as plt



os.chdir("C:/Users/KayZac/Desktop/")
with open('bcad_propval.pkl', 'rb') as f:
    data = pickle.load(f)
data_non0 = data[data['Appraised Value'] > 0]

data_realonly = data_non0[data_non0['Type'] == 'Real']
data_dbananonly = data_realonly[data_realonly['Doing Business As'] == 'nan']
data_lblrmv1 = data_dbananonly[~data_dbananonly['Owner Name'].str.contains('CORP', na=False)]
data_lblrmv2 = data_lblrmv1[~data_lblrmv1['Owner Name'].str.contains('LLC', na=False)]
data_lblrmv3 = data_lblrmv2[~data_lblrmv2['Owner Name'].str.contains('TRUST', na=False)]
data_lblrmv4 = data_lblrmv3[~data_lblrmv3['Owner Name'].str.contains('INC', na=False)]
data_lblrmv5 = data_lblrmv4[~data_lblrmv4['Owner Name'].str.contains('LTD', na=False)]
data_lblrmv6 = data_lblrmv5[~data_lblrmv5['Owner Name'].str.contains('STATE OF TEXAS', na=False)]
data_hbs = data_lblrmv6[~data_lblrmv6['Owner Name'].str.contains('I S D', na=False)]

print(data_hbs)
print(data_hbs['Appraised Value'].describe())
# print(data_hbs[data_hbs['Appraised Value'] < 100])

# save as PKL file
os.chdir("C:/Users/KayZac/Desktop")
data_hbs.to_pickle('bcad_propval_cleaned.pkl')

# plt.hist(data['Appraised Value'][data['Appraised Value'] < 1e6], bins=100)
# plt.show()