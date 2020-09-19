import os
import glob
import pandas as pd
os.chdir("C:/Users/KayZac/Downloads")

extension = 'csv'
all_filenames = glob.glob('*.{}'.format(extension))
all_filenames.sort(key=os.path.getmtime)
errorfiles = []

#combine all files in the list
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

# clean up this shit
# ['PropertySearchResults(33).csv', 'PropertySearchResults(34).csv',
# 'PropertySearchResults(39).csv', 'PropertySearchResults(44).csv',
# 'PropertySearchResults(49).csv', 'PropertySearchResults(50).csv',
# 'PropertySearchResults(51).csv', 'PropertySearchResults(55).csv',
# 'PropertySearchResults(56).csv', 'PropertySearchResults(60).csv',
# 'PropertySearchResults(65).csv', 'PropertySearchResults(66).csv',
# 'PropertySearchResults(67).csv', 'PropertySearchResults(68).csv',
# 'PropertySearchResults(69).csv', 'PropertySearchResults(72).csv',
# 'PropertySearchResults(74).csv', 'PropertySearchResults(30).csv']
# 18


# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
#export to csv
# combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')