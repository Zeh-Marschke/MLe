import numpy as np

# --- define the linear model
def calc_linear_y_values (x :np.ndarray, m :float, b :float) -> np.ndarray :
    """
    calculate datapoints on a line y = m * x + b 
    :input
      x : input to function [shape: arbitrary]
      m : slope
      b : intercept
    :return m * x + b [shape: same as x]
    """
    return m * x + b

# --- define the calculation of the mean squared error
def mse (x1 :np.ndarray, x2 :np.ndarray) -> float:
    """ 
    calculate the mean square error (mse) of two vectors 
    it's the distance between the two vector with the L2-metric,
    divided by the dimension of the vectors
    input:
      x1 : first vector [shape arbitrary]
      x2 : second vector [shape: same as x]
    return: mse 
    """
    n = x1.size
    return np.sum ((x1 - x2) **2) / n

# --- Linear Regression manual
def LinReg_manual (x : np.ndarray, y : np.ndarray):
    """
    calculate the line according the linear regression method 
    and the coefficient of correlation 
    input:
      x: x-values of the datapoints 
      y: y-values of the datapoints
    return:
      m: slope of the line
      b: intercept of the line
      r2: squared coefficient of correlation
    """
    n = x.size
    sum_x = np.sum (x)
    sum_y = np.sum (y)
    sum_x2 = np.sum (x * x)
    sum_xy = np.sum (x * y)
    sum_y2 = np.sum (y * y)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x **2)
    b = (sum_x2 * sum_y - sum_x * sum_xy) / (n * sum_x2 - sum_x **2)
    r = (n * sum_xy - sum_x * sum_y) / (np.sqrt (n *sum_x2 - sum_x **2) * np.sqrt (n * sum_y2 - sum_y **2))
    r2 = r * r
    return m, b, r2