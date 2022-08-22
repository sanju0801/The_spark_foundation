from unicodedata import numeric
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression


def marks_prediction(marks):
    X = pd.read_csv("X_values.csv")  
    Y = pd.read_csv("Y_values.csv")

    X = X.values
    Y = Y.values

    model = LinearRegression()  
    model.fit(X, Y)

    x_test = np.array(marks, dtype= int)
    x_test = x_test.reshape((1,-1))

    return model.predict(x_test)