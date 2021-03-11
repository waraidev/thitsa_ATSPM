import base64
from io import BytesIO

import numpy as np
import matplotlib.figure as plt
import matplotlib.style as plt_style
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Function Imports
from simpls.ReshapeData import reshape
from simpls.MatrixFunctions import RPCA, build_SIMPLS, predict_SIMPLS


def SIMPLS_Chart(csv_url, filename):

    data = reshape(csv_url)
    signal_index = filename.find("signalID_")
    signal = filename[signal_index + 9:signal_index + 9 + 4]

    # Visual update for users
    # implement on web
    print("Loading...")

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

    fig = plt.Figure(figsize=(6, 4), dpi=150)
    plt_style.use('seaborn')
    axs = fig.subplots(1, 1)
    fig.suptitle("Intersection {}".format(signal))
    axs.set_xlabel("Time (hr)")
    axs.set_ylabel("Cars / 15 mins")
    axs.plot(TimeZ, L[-1, :split], 'g', label='Denoised predictors')
    axs.plot(TimeY, L[-1, split:], 'r', label='Denoised response')
    axs.plot(TimeY, Prediction[-1, :], 'g--', label='Predicted response')
    axs.plot(Time, A[-1, :], 'b:', label='Measured')
    fig.legend(framealpha=1, frameon=True)

    image = BytesIO()
    FigureCanvas(fig).print_png(image)
    image_b64_str = "data:image/png;base64,"
    image_b64_str += base64.b64encode(image.getvalue()).decode('utf8')

    print("SIMPLS finished!")

    return image_b64_str

# Displaying Downloadable CSV files

# import pandas as pd
# from server.simpls.GetData import OutputPredData

# Output prediction data, comment out if not needed
# p = pd.DataFrame(data=Prediction[1:, 1:],  # values
#                  index=Prediction[1:, 0],  # 1st column as index
#                  columns=Prediction[0, 1:])
#
# OutputPredData(p)
