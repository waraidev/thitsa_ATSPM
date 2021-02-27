import numpy as np
import math as m


# Define some useful functions

# Matrix element-wise absolute value
def mat_abs(X):
    rows, cols = np.shape(X)
    output = np.zeros([rows, cols])

    for i in range(rows):
        for j in range(cols):
            output[i][j] = abs(X[i][j])
    return output


# Matrix element-wise maximum
def mat_max(X, a):
    rows, cols = np.shape(X)
    output = np.zeros([rows, cols])

    for i in range(rows):
        for j in range(cols):
            output[i][j] = max(X[i][j], a)
    return output


# Matrix shrinkage function
def shrink(X, tau):
    rows, cols = np.shape(X)
    # Below, we use ELEMENT-WISE multiplication
    return np.multiply(np.sign(X), mat_max(mat_abs(X) - tau * np.ones([rows, cols]), 0))


# Singular value shrinkage operator
def SVT(X, tau):
    # full_matrices=False below gives economy SVD
    U, S, V = np.linalg.svd(X, full_matrices=False)
    # The np.linalg.svd returns S as a VECTOR of s.v.'s,
    # but we want a diagonal matrix.
    S = np.diag(S)
    # Notice the matrix multiplication function instead of
    # element-wise multiplication
    return U @ shrink(S, tau) @ V


def RPCA(X, lambda0=1):
    rows, cols = np.shape(X)
    # np.linalg.norm(X,1) is the l1 operator norm of X
    mu = rows * cols / (4 * np.linalg.norm(X, 1))
    lambda1 = lambda0 / m.sqrt(max(rows, cols))
    # norm(X,'fro') is Frobenius norm
    thresh = 1e-7 * np.linalg.norm(X, 'fro')

    L = np.zeros([rows, cols])
    S = np.zeros([rows, cols])
    Y = np.zeros([rows, cols])
    count = 0

    while ((np.linalg.norm(X - L - S, 'fro') > thresh) and (count < 1000)):
        L = SVT(X - S + (1 / mu) * Y, 1 / mu)
        S = shrink(X - L + (1 / mu) * Y, lambda1 / mu)
        Y = Y + mu * (X - L - S)
        count = count + 1

    return L, S


def build_SIMPLS(Z, Y, rank=None, path_to_save=None, svthreshold=None):
    rowsZ, colsZ = np.shape(Z)
    rowsY, colsY = np.shape(Y)

    # Standardize predictors and responses
    Ztilde = np.zeros([rowsZ, colsZ])
    Ytilde = np.zeros([rowsY, colsY])

    meanZcols = np.mean(Z, axis=0)
    meanYcols = np.mean(Y, axis=0)
    stdZcols = np.std(Z, axis=0)
    stdYcols = np.std(Y, axis=0)

    for i in range(rowsZ):
        for j in range(colsZ):
            Ztilde[i][j] = Z[i][j] - meanZcols[j]
            if stdZcols[j] != 0:
                Ztilde[i][j] = Ztilde[i][j] / stdZcols[j]
    for i in range(rowsY):
        for j in range(colsY):
            Ytilde[i][j] = Y[i][j] - meanYcols[j]
            if stdYcols[j] != 0:
                Ytilde[i][j] = Ytilde[i][j] / stdYcols[j]

    # Compute SVD of correlation matrix
    U0, E0, V0 = np.linalg.svd(np.transpose(Ztilde) @ Ytilde, full_matrices=False)

    # Because np.linalg.SVD is an interative method, it can result in tiny s.v.'s that result in NANs when
    # dividing other numbers by them. So, lets delete any singular values below some threshold.
    if svthreshold == None:
        svthreshold = 1e-3
    for i in range(np.size(E0)):
        if E0[i] < svthreshold:
            E0 = E0[:i]
            break

    # If no rank is specified, use full-rank.
    if rank == None:
        rank = np.size(E0)

    E0 = np.diag(E0)  # turn this into a diagonal matrix (svd function gives array of s.v.'s)

    U = U0[:, :rank]  # do rank-r truncation.
    E = E0[:rank, :rank]
    V = V0[:, :rank]

    T = np.zeros([rowsZ, rank])
    P = np.zeros([colsZ, rank])
    C = np.zeros([colsY, rank])

    # Build the SIMPLS model
    for i in range(rank):
        r = U[:, i]
        Zr = np.reshape(Ztilde @ r, [rowsZ, 1])
        T[:, [i]] = Zr / np.linalg.norm(Zr)
        P[:, [i]] = np.transpose(Ztilde) @ T[:, [i]]  # here the [i] forces this to be a column vector
        C[:, [i]] = np.transpose(Ytilde) @ T[:, [i]]

        Ztilde = Ztilde - T[:, [i]] @ np.transpose(T[:, [i]]) @ Ztilde
        Ytilde = Ytilde - T[:, [i]] @ np.transpose(T[:, [i]]) @ Ytilde

    model = np.linalg.pinv((np.transpose(P))) @ np.transpose(C)

    # Now, we need to store the model and the descriptive statistics
    # of Y
    if path_to_save == None:
        path_to_save = 'test_model'
    np.savez(path_to_save + '.npz', SIMPLS=model, stdYcols=stdYcols, meanYcols=meanYcols)

    return path_to_save


def predict_SIMPLS(Zs, path_to_model=None):
    rowsZs, colsZs = np.shape(Zs)

    # Standardize predictors
    Ztildes = np.zeros([rowsZs, colsZs])
    meanZscols = np.mean(Zs, axis=0)
    stdZscols = np.std(Zs, axis=0)
    for i in range(rowsZs):
        for j in range(colsZs):
            Ztildes[i][j] = Zs[i][j] - meanZscols[j]
            if stdZscols[j] != 0:
                Ztildes[i][j] = Ztildes[i][j] / stdZscols[j]

    # Load model
    if path_to_model is None:
        path_to_model = 'test_model.npz'
    savedData = np.load(path_to_model)

    meanYcols = savedData['meanYcols']
    stdYcols = savedData['stdYcols']
    model = savedData['SIMPLS']

    # Predict responses using model
    Ys = Ztildes @ model

    # De-standardize the responses using descriptive statistics from training
    rowsYs, colsYs = np.shape(Ys)
    for i in range(rowsYs):
        for j in range(colsYs):
            Ys[i][j] = Ys[i][j] * stdYcols[j] + meanYcols[j]
    return Ys
