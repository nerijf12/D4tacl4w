# import clevercsv as csv
import os
import glob
import pandas as pd

os.chdir("../_propcsv")

extension = 'csv'
all_filenames = glob.glob('*.{}'.format(extension))
all_filenames.sort(key=os.path.getmtime)
errorfiles = []

# combine all files in the list
for f in all_filenames:
    # print(f)
    try:
        a = pd.read_csv(f)
        if a.empty:
            # print("File " + str(all_filenames.index(f)+1) + "is empty. Skipping...")
            continue
        # print(a.head())
    except:
        # print(f)
        errorfiles.append(f)
        # print(f"{f}\n{len(pd.read_csv(f).columns)}.")
    # print(a)

print(errorfiles)
print(len(errorfiles))

# getting column headings
df = pd.read_csv(all_filenames[0])
headings = list(df.columns)

# checks to make df out of each of csvs in errorfiles
for myerr in errorfiles:
    b = pd.read_csv(myerr, names=headings)  # idk why but this fixes it
    newb = b.drop(b.index[0])
    print(newb.head())
