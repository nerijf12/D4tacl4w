import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import csv

os.chdir("../_zipcsv/")
all_csvs = glob.glob('*.{}'.format('csv'))

for csv in all_csvs:
    os.chdir("../_zipcsv/")
    taxrate_df = pd.read_csv(csv, header=None)
    ziplabel = csv[:-4]
    labels = list(taxrate_df[0])
    taxrates = list(taxrate_df[1])
    print(taxrates)
    # pcts = (taxrates / sum(taxrates)) * 100
    # new_TRpcts = pd.DataFrame(str(pcts), index=labels, columns=['Tax Rate'])

    # with open(ziplabel + '.csv', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in taxrate_df:
    #         pct = (row[1] / sum(row[1])) * 100
    #         print(row[0], pct)
    os.chdir("../_taxratepct_csvs/")
    f = open(ziplabel + '.csv', 'a')
    for row in taxrates:
        pct = (row / sum(taxrates)) * 100
        together = labels[taxrates.index(row)] + ", " + str(pct) + "\n"
        print(together)
        f.write(together)

    f.close()
