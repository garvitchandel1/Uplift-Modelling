import numpy as np
from numpy import trapezoid


def max_profit(fractions, profits):
    idx = np.argmax(profits)
    return fractions[idx], profits[idx]


def qini_auc(qini_curve):
    return trapezoid(qini_curve)