import pandas as pd


def clean_appraised_nans(df):
    # df = pd.read_csv('PropertySearchResults(2).csv')
    # print(type(df.iloc[548]['Appraised Value']))
    # print(type(df.iloc[547]['Appraised Value']))
    a = []
    index = 0

    def get_index(x, index):
        if type(x['Appraised Value']) == str:
            a.append(index)
            index += 1
        else:
            index += 1

    df.apply(lambda x: get_index(x, index), axis=1)
    newdf = df.iloc[a]
    return newdf
