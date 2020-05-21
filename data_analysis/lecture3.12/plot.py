import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


### Regression ###

def plot_regression(ax, X, y, reg, scaler=None):

    # plot the examples
    ax.scatter(X, y, alpha=0.6)

    # create feature matrix
    xmin, xmax = ax.get_xlim()
    x_line = np.linspace(xmin, xmax, 30).reshape(-1, 1)
    x_line_predict = scaler.transform(x_line) if scaler else x_line
    
    # predict
    y_line = reg.predict(x_line_predict)

    # plot the hypothesis
    ax.plot(x_line, y_line, c='g', linewidth=3)

    # formatting
    ax.set_xlim(xmin, xmax)
    ax.set_xlabel('planned online time (norm)')
    ax.set_ylabel('time spent online (min)')
    ax.set_title('Online Procrastination');


def compare_regression(X, y, regs, titles, scaler=None):
    fig = plt.figure(figsize=(14, 4), dpi=100)
    for i, reg in enumerate(regs):
        ax = fig.add_subplot(1, len(regs), i+1)
        plot_regression(ax, X, y, reg, scaler)
        ax.set_title(titles[i])
