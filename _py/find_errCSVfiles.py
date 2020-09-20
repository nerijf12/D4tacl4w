import os
import glob
import pandas as pd
os.chdir("../_propcsv")

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
        if a.empty: #skip empty
            continue
    except: # checks to make df out of each of csvs in errorfiles
        # collect all bad csvs
        a = pd.read_csv(f, names=headings)  # idk why but this fixes it
        a = a.drop(a.index[0])
    a['Zipcode'] = f.split('.')[-2]
    frames.append(a)

combined_df = pd.concat(frames)


# for myerr in errorfiles:
#     b = pd.read_csv(myerr, names=headings)  # idk why but this fixes it
#     newb = b.drop(b.index[0])
#     print(newb.head())
