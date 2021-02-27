from ReshapeData import reshape
import pandas as pd


# Get original reshaped data
def OutputOriginalData():
    # path_to_data = "atspm_signalID_1663_start_download_date_09_09_2020.csv"
    path_to_data = "atspm_signalID_1663_start_download_date_11_03_2020.csv"

    data = reshape(path_to_data)

    data.to_csv('1663Data_11-3_to_11-16.csv', index=False, header=False)


# Get prediction data
def OutputPredData(pred_df):
    pred_df.to_csv('prediction.csv', index=False, header=False)
