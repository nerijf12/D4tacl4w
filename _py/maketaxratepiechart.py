import matplotlib.pyplot as plt
# from matplotlib.gridspec import GridSpec
import pandas as pd
import os
import glob
import numpy as np

# os.chdir("../_zipcsv/")
# all_csvs = glob.glob('*.{}'.format('csv'))
all_csvs = ['78222.csv', '78256.csv']

for csv in all_csvs:
    os.chdir("../_zipcsv/")
    taxrates = pd.read_csv(csv, header=None)
    ziplabel = csv[:-4]
    labels = list(taxrates[0])
#######################################################################################
    fig, ax = plt.subplots(figsize=(12, 6), subplot_kw=dict(aspect="equal"))
    cmap = plt.get_cmap('Spectral')
    colors = [cmap(i) for i in np.linspace(0, 1, 8)]


    def func(pct):  # , allvals):
        # absolute = pct/100.*np.sum(allvals)
        # return "{:.1f}%\n({:.3f} %)".format(pct, absolute)
        return "{:.1f}%".format(pct)


    wedges, texts, autotexts = ax.pie(taxrates[1], autopct=lambda pct: func(pct),
                                      textprops=dict(color="k"), colors=colors)
    plt.setp(autotexts, size=12)
    ax.legend(wedges, labels,
              title="Tax Rates",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    ax.set_title(str(ziplabel) + " Property Tax Breakdown",size=16)
    plt.tight_layout()
    # plt.show()
    os.chdir("../_taxratefigs/")
    plt.savefig(str(ziplabel) + "_taxrates.png")

#################################################################################################

#
#
#
# cmap = plt.get_cmap('Spectral')
# colors = [cmap(i) for i in np.linspace(0, 1, 8)]
# # colors = ['#FFFAF3', '#57B19F', '#F15B5D', '#79242F', '#6CA9DE', '#4F5362', '#FFFFFF']
#
# #explsion
# explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
#
# # fig1, ax1 = plt.subplots()
# plt.pie(taxrate_df[1], colors=colors, labels=labels, autopct='%1.1f%%', startangle=90,
# pctdistance=0.55, explode=explode)  # draw circle
# centre_circle = plt.Circle((0, 0), 0.70, fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)  # Equal aspect ratio ensures that pie is drawn as a circle
# # ax1.axis('equal')
# plt.tight_layout()
# plt.show()
###############################################################################################
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# explode = (0, 0, 0, 0, 0, 0, 0.1, 0)  # only "explode" the 7th slice
#
# fig1, ax1 = plt.subplots()
# plt.subplot(the_grid[0, 1], aspect=1, title='78201 ZIP Property Tax Breakdown')
# taxrates_pie = plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, colors=colors)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()
# plt.savefig("78201_taxrates.png")

###############################################################################################
    # import plotly.graph_objects as go

    # cmap = plt.get_cmap('Spectral')
    # colors = [cmap(i) for i in np.linspace(0, 1, 8)]
    # # colors = ['#FFFAF3', '#57B19F', '#F15B5D', '#79242F', '#6CA9DE', '#4F5362', '#FFFFFF']
    # cmap2lbls = dict()
    # for c in colors:
    #     cmap2lbls[labels[colors.index(c)]] = c
    # # fig = go.Figure(data=[go.Pie(labels=labels, values=taxrates[1], textinfo='label+percent',
    # #                              insidetextorientation='radial')])
    # # # fig.show()
    # # os.chdir("../_taxratehtmls/")
    # # fig.write_html(str(ziplabel) + "_taxrates.html")
    # # fig.to_image(format="png", engine="kaleido", width=6000, height=3500, scale=2)
    # # fig.write_image("78201_taxrates.png")
    #
    # import plotly.express as px
    # df = px.data.tips()
    # tr_df = pd.DataFrame({'Name': taxrates[0], 'TaxRate': taxrates[1]})
    # # print(tr_df)
    # fig = px.pie(tr_df, values='TaxRate', names='Name', color='Name', color_discrete_map=cmap2lbls)
    # # fig.show()
    # os.chdir("../_taxratefigs/")
    # fig.write_html(str(ziplabel) + "_taxrates.html")
    # fig.write_image(str(ziplabel) + "_taxrates.png")


###############################################################################################

# import cufflinks as cf

# Correct datatypes cufflinks does not support CategoryType so we make them strings and rebuild the dataframe.
# source_df  = pd.DataFrame(source_counts).reset_index()



# flavor_pie = taxrate_df.iplot(kind='pie', labels=labels, values=sizes, colors=colors, title='78201 ZIP Property Tax Breakdown')
#
# display(source_pie, flavor_pie)