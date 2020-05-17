import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

### Classification ### 

def make_meshgrid(x, y, h=.02):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid, optional

    Returns
    -------
    xx, yy : ndarray
    """
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy


def plot_decision_boundary(ax, clf, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out


def plot_contours(ax, clf, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    plot_decision_boundary(ax, clf, xx, yy, **params)


def plot_classification(ax, X, y, clf):
    X0, X1 = X[:, 0], X[:, 1]
    xx, yy = make_meshgrid(X0, X1)
    plot_contours(ax, clf, xx, yy,
                      cmap=plt.cm.coolwarm, alpha=0.8)
    scatter = ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k', alpha=1.0)
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_title('Bank Notes Classification')
    handles, labels = scatter.legend_elements()
    ax.legend(handles=handles, labels=['genuine', 'fake'])


def compare_classification(X, y, clfs, titles):
    fig = plt.figure(figsize=(14, 4), dpi=100)
    for i, clf in enumerate(clfs):
        ax = fig.add_subplot(1, len(clfs), i+1)
        plot_classification(ax, X, y, clf)
        ax.set_title(titles[i])

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
    ax.set_xlabel('planned online time (min)')
    ax.set_ylabel('time spent online (min)')
    ax.set_title('Online Procrastination');


def compare_regression(X, y, regs, titles, scaler=None):
    fig = plt.figure(figsize=(14, 4), dpi=100)
    for i, reg in enumerate(regs):
        ax = fig.add_subplot(1, len(regs), i+1)
        plot_regression(ax, X, y, reg, scaler)
        ax.set_title(titles[i])
