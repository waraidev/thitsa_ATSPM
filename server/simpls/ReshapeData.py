import pandas as pd
import numpy as np
from io import BytesIO


def find_indexes(series, dates):
    # The last item in index should be removed.
    # It is the last item in the list.
    idx = []
    for d in dates:
        temp = series.tolist()
        temp.reverse()
        idx.append(len(temp) - temp.index(d))

    return idx


# 'file_body' is the CSV file from Amazon S3
def reshape(file_url):
    df = pd.read_csv(file_url, skiprows=2)

    for c in df.columns:
        if c.find("Total") != -1:
            del df[c]

    cols = df.columns

    # cols[0] is the column of dates
    df[cols[0]] = pd.to_datetime(df[cols[0]])

    dates = df[cols[0]].map(lambda d: d.date()).unique()  # creates an array of dates

    # adds the times needed for amount of movements
    new_df = pd.DataFrame(df[cols[1]][0:96 * (len(cols) - 2)])

    # indexes for date changes
    idx = find_indexes(df[cols[0]], dates)

    for i in range(0, len(idx)):
        row_to_add = np.empty(0)
        for k in range(2, len(cols)):
            c = cols[k]
            if i == 0:
                row_to_add = np.append(row_to_add, df[c][0:idx[0]].array)
            else:
                row_to_add = np.append(row_to_add, df[c][idx[i - 1]:idx[i]].array)
        new_df[dates[i]] = row_to_add

    pd.set_option('display.max_rows', 1000)

    new_df = new_df.iloc[:, 1:]
    return new_df.T
