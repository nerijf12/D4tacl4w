import os
import glob
import pandas as pd
os.chdir("../_propcsv_zipnames")

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
####################################################################################################

# Rename all CSV files in the '_propcsv' folder and save into the'_propcsv_zipnames folder
for f in all_filenames:

    old_filename = 'C:/Users/KayZac/Documents/GitHub/D4tacl4w/_propcsv_zipnames/' + f
    new_filename = 'C:/Users/KayZac/Documents/GitHub/D4tacl4w/_propcsv_zipnames/' + str(zipcodes[all_filenames.index(f)]) + '.csv'
    os.rename(old_filename, new_filename)
