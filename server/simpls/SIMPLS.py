import base64
from io import BytesIO

import numpy as np
import matplotlib.pyplot as plt
import time

# Function Imports
from server.simpls.ReshapeData import reshape
from server.simpls.MatrixFunctions import RPCA, build_SIMPLS, predict_SIMPLS


def SIMPLS_Chart():
    path_to_data = ""

    data = reshape(path_to_data)

    # Visual update for users
    # implement on web
    print("Loading...")

    start = time.time()

    # Load and de-noise data
    A = np.array(data)
    L, S = RPCA(A[:-1, :])  # Here, we take out the last row...
    # it will be used during validation of the model.

    split = 44

    Z = L[:, :split]
    Y = L[:, split:]

    # Train a test model
    build_SIMPLS(Z, Y)

    # Load test data
    # Append new predictor variables to Z
    Z = np.vstack((Z, A[-0, :split]))

    # Predict using a test model
    Prediction = predict_SIMPLS(Z)

    # Visual update for users
    print("Loading...")

    # For comparison to model, de-noise data after response variable is collected
    L, S = RPCA(A)

    # Plot the prediction versus actual
    [rowsZ, colsZ] = np.shape(Z)
    TimeZ = [i * 0.25 for i in range(colsZ)]

    [rowsY, colsY] = np.shape(Y)
    TimeY = [(i + colsZ) * 0.25 for i in range(colsY)]

    Time = np.concatenate((TimeZ, TimeY))

    fig = plt.figure(figsize=(6, 4), dpi=150)
    plt.style.use('seaborn')
    axs = fig.subplots(1, 1)
    fig.suptitle("Intersection 1663")
    axs.set_xlabel("Time (hr)")
    axs.set_ylabel("Cars / 15 mins")
    axs.plot(TimeZ, L[-1, :split], 'g', label='Denoised predictors')
    axs.plot(TimeY, L[-1, split:], 'r', label='Denoised response')
    axs.plot(TimeY, Prediction[-1, :], 'g--', label='Predicted response')
    axs.plot(Time, A[-1, :], 'b:', label='Measured')
    plt.legend(framealpha=1, frameon=True)

    buf = BytesIO()
    fig.savefig(buf, format="png")
    graph = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{graph}'/>"

# print('It took', time.time() - start, 'seconds to load data, build model, predict, and plot the results.')

# Displaying Downloadable CSV files

# import pandas as pd
# from server.simpls.GetData import OutputPredData

# Output prediction data, comment out if not needed
# p = pd.DataFrame(data=Prediction[1:, 1:],  # values
#                  index=Prediction[1:, 0],  # 1st column as index
#                  columns=Prediction[0, 1:])
#
# OutputPredData(p)
