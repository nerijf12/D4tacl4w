import os
import glob
import pandas as pd
os.chdir("../_propcsv")

zipcodes = [78002, 78023, 78054, 78069, 78073, 78101, 78109, 78112, 78148,
            78150, 78152, 78201, 78202, 78203, 78204, 78205, 78206, 78207,
            78208, 78209, 78210, 78211, 78212, 78213, 78214, 78215, 78216,
            78217, 78218, 78219, 78220, 78221, 78222, 78223, 78224, 78225,
            78226, 78227, 78228, 78229, 78230, 78231, 78232, 78233,	78234,
            78235, 78236, 78237, 78238,	78239, 78240, 78241, 78242, 78243,
            78244, 78245, 78246, 78247, 78248, 78249, 78250, 78251, 78252,
            78253, 78254, 78255, 78256, 78257, 78258, 78259, 78260, 78261,
            78262, 78263, 78264, 78265, 78268, 78269, 78270, 78275, 78278,
            78279, 78280, 78283, 78284, 78285, 78286, 78287, 78288, 78289,
            78291, 78292, 78293, 78294, 78295, 78296, 78297, 78298, 78299]
extension = 'csv'
all_filenames = glob.glob('*.{}'.format(extension))

# This Section Re-orders the CSV files so that they're in the same order as the ZIP code list above


# This definition grabs last 4 characters of the file name:
def last_8chars(x):
    return(x[-8:])


all_filenames = sorted(all_filenames, key = last_8chars)
filename_order = list(range(90, 99)) + list(range(0, 90))
all_filenames = [all_filenames[f] for f in filename_order]
errorfiles = []
propIDs = dict()

# combine all files in the list
for f in all_filenames:
    # print(f)
    try:
        a = pd.read_csv(f)
        propIDs[zipcodes[all_filenames.index(f)]] = a['Property ID'][0]
        if a.empty:
            print("File " + str(all_filenames.index(f)+1) + "is empty. Skipping...")
            propIDs[zipcodes[all_filenames.index(f)]] = 'NaN'
            continue
    except:
        # print(f)
        errorfiles.append(f)
        # print(f"{f}\n{len(pd.read_csv(f).columns)}.")
# print(propIDs)
# print(len(propIDs))

# save zip-to-propID dictionary to CSV file
newcsvfilename = '../_py/zip2propID.csv'
propIDs_df = pd.DataFrame.from_dict(propIDs, orient="index", columns=['Property ID'])
# propIDs_df1 = propIDs_df.rename(columns = {"ZIP" : "Signal"})
# propIDs_df.columns.values[0] = 'ZIP Code'
# propIDs_df.columns.values[1] = 'Property ID'
print(propIDs_df)
propIDs_df.to_csv(newcsvfilename, header=["Property ID"])
