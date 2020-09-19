import pandas as pd

zcpi = pd.read_csv("zip2propID.csv", index_col='ZIPCode', header=0)
ZIPs = list(zcpi.index.values)
pIDs = list(zcpi.PropertyID)
for zip in ZIPs:
    zip = ZIPs[0]
    print('Searching properties under ' + str(zip) + ' ZIP code...')
    print('Property ID is ' + str(pIDs[ZIPs.index(zip)]))
