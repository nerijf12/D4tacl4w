import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir("../_zipcsv/")
taxrates = pd.read_csv("78201.csv", header=None)
labels = list(taxrates[0])
sizes = list((taxrates[1]/sum(taxrates[1]))*100)

# for zip in ZIPs:
#     zip = ZIPs[0]
#     print('Searching properties under ' + str(zip) + ' ZIP code...')
#     print('Property ID is ' + str(pIDs[ZIPs.index(zip)]))


# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
explode = (0, 0, 0, 0, 0, 0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()