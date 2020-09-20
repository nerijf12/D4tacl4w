import os
import glob
import pandas as pd
import pickle
import numpy as np

os.chdir("../_propcsv_zipnames")

class Dataclaw:
    def __init__(self):
        self.df = self.read_data()
        # print(self.df.columns)
        # print(len(self.df))
        # print(self.df['Unnamed: 8'][0])

    def read_data(self):
        extension = 'csv'
        all_filenames = glob.glob('*.{}'.format(extension))
        all_filenames.sort(key=os.path.getmtime)

        # getting column headings of known correct csv
        df = pd.read_csv(all_filenames[0])
        headings = list(df.columns)

        frames = []

        # go through and find which csv cannot become df
        for f in all_filenames:
            # print(f)
            try:
                a = pd.read_csv(f)
                if a.empty:  # skip empty
                    continue
            except:  # checks to make df out of each of csvs in errorfiles
                # collect all bad csvs
                a = pd.read_csv(f, names=headings)  # idk why but this fixes it
                a = a.drop(a.index[0])
            # a[len(a.columns) > 8]
            # find rows where columns > 8
            # delete rows where this occurs


            a['Zipcode'] = f.split('.')[-2]
            frames.append(a)

        combined_df = pd.concat(frames)

        # 268 errors where NaN values in a weird 9th column, so dropped those
        reshape_df = combined_df.drop(labels='Unnamed: 8', axis=1)

        return self.preprocess_data(reshape_df)

    def preprocess_data(self, df):
        # changing data types of numbers (str to numbers)
        df['Property ID'] = df['Property ID'].values.astype(int)
        df['Doing Business As'] = df['Doing Business As'].values.astype(str)

        a = []
        # df = self.clean_appraised_nans(df)
        print('preprocess_data before \n', df.head())
        for num in df['Appraised Value']:
            # removing commas from numbers like 100,000
            try:
                a.append(int(num.replace(",", "")))
            except: # in case of float NaN
                a.append(0)
        df['Appraised Value'] = a
        print('preprocess_data after \n', df.head())

        return df

dataset = Dataclaw()
os.chdir("C:/Users/KayZac/Desktop")
dataset.df.to_pickle('bcad_propval.pkl')
# dataset.df.to_pickle('../../bcad_propval.pkl')
