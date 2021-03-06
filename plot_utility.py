"""
utility to plot data
"""

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


def plot_features(
    X, y,
    test_idx=None,
    xlabel='x', ylabel='y', title=None,
    loc='best'):
    """
    plot features

    # Parameters
    -----
    * X : array-like, shape = (n_samples, 2)
        sample data
    * y : array-like, shape = (n_samples, )
        target variable
    * test_idx : list
        list of indexes of test data in X and y
    * xlabel : string
        label of x-axis
    * ylabel : string
        label of y-axis
    * title : string or None
        title of graph
    * loc : string or int
        location of legend

    # Notes
    -----
    * n_samples represents the number of samples.
    """

    # prepare for markers and color maps
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')

    # plot training data
    for color, marker, label in zip(colors, markers, np.unique(y)):
        plot_index = (y == label)
        plt.scatter(x=X[plot_index, 0], y=X[plot_index, 1],
                    alpha=0.8, c=color, marker=marker, edgecolor='black', label=label)

    # plot test data
    if test_idx:
        plt.scatter(x=X[test_idx, 0], y=X[test_idx, 1],
                    alpha=1.0, c='', marker='o', edgecolor='black', linewidth=1, s=100, label='test_set')

    # configure plot area
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    plt.legend(loc=loc)

    # show plot
    plt.show()


def plot_decision_regions(
    X, y,
    classifier,
    test_idx=None,
    resolution=0.02,
    xlabel='x', ylabel='y', title=None,
    loc='best'):
    """
    plot decision regions

    # Parameters
    -----
    * X : array-like, shape = (n_samples, 2)
        sample data
    * y : array-like, shape = (n_samples, )
        target variable
    * classifier : object
        instance of classifier, which needs to implement the following methods
            * classifier.predict : returns the prediction value of a sample
    * test_idx : list
        list of indexes of test data in X and y
    * resolution : float
        resolution of plot area
    * xlabel : string
        label of x-axis
    * ylabel : string
        label of y-axis
    * title : string or None
        title of graph
    * loc : string or int
        location of legend
    """

    # prepare for markers and color maps
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    color_map = ListedColormap(colors[:len(np.unique(y))])

    # prepare for plot area and generate grid points
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    x1, x2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    # predict each grid points
    z = classifier.predict(np.array([x1.ravel(), x2.ravel()]).T)
    z = z.reshape(x1.shape)

    # plot the contour
    plt.contourf(x1, x2, z, alpha=0.3, cmap=color_map)

    # plot training data
    for color, marker, label in zip(colors, markers, np.unique(y)):
        plot_index = (y == label)
        plt.scatter(x=X[plot_index, 0], y=X[plot_index, 1],
                    alpha=0.8, c=color, marker=marker, edgecolor='black', label=label)

    # plot test data
    if test_idx:
        plt.scatter(x=X[test_idx, 0], y=X[test_idx, 1],
                    alpha=1.0, c='', marker='o', edgecolor='black', linewidth=1, s=100, label='test_set')

    # configure plot area
    plt.xlim(x1.min(), x1.max())
    plt.ylim(x2.min(), x2.max())
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    plt.legend(loc=loc)

    # show plot
    plt.show()


def plot_predictions(
    x, y,
    regressor,
    test_idx=None,
    xlabel='x', ylabel='y', title=None,
    loc='best'):
    """
    plot predictions of regressor

    # Parameters
    -----
    * x : array-like, shape = (n_samples, )
        sample data
    * y : array-like, shape = (n_samples, )
        target variable
    * regressor : object
        instance of regressor, which needs to implement the following methods
            * regressor.predict : returns the prediction value of a sample
    * test_idx : list
        list of indexes of test data in X and y
    * xlabel : string
        label of x-axis
    * ylabel : string
        label of y-axis
    * title : string or None
        title of graph
    * loc : string or int
        location of legend
    """

    # plot prediction of regressor
    plt.plot(
        x, regressor.predict(x[:, np.newaxis]),
        color='black', lw=1)

    # plot training data
    plt.scatter(
        x=x, y=y,
        c='steelblue', edgecolor='white', s=70, label='training data')

    # plot test data
    if test_idx:
        plt.scatter(
            x=x[test_idx], y=y[test_idx],
            alpha=1.0, c='', marker='o', edgecolor='black', linewidth=1, s=100, label='test data')

    # configure plot area
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    if test_idx is not None:
        plt.legend(loc=loc)

    # show plot
    plt.show()


def plot_residuals(
    X, y,
    regressor,
    test_idx=None,
    xlabel='predicted values', ylabel='residuals', title=None,
    loc='best'):
    """
    plot residuals of regressor

    # Parameters
    -----
    * X : array-like, shape = (n_samples, n_features)
        sample data
    * y : array-like, shape = (n_samples, )
        target variable
    * regressor : object
        instance of regressor, which needs to implement the following methods
            * regressor.predict : returns the prediction value of a sample
    * test_idx : list
        list of indexes of test data in X and y
    * xlabel : string
        label of x-axis
    * ylabel : string
        label of y-axis
    * title : string or None
        title of graph
    * loc : string or int
        location of legend
    """

    # plot residual of training data
    y_pred = regressor.predict(X)
    scatter_x, scatter_y = y_pred, y_pred - y
    plt.scatter(
        x=scatter_x, y=scatter_y,
        c='steelblue', marker='o', edgecolor='white', label='training data')

    # mark residual of test data
    if test_idx:
        plt.scatter(
            x=scatter_x[test_idx], y=scatter_y[test_idx],
            alpha=1.0, c='', marker='o', edgecolor='black', linewidth=1, s=75, label='test data')

    # plot perfect prediction
    plt.hlines(y=0, xmin=-10, xmax=50, color='black', lw=1)

    # configure plot area
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    if test_idx is not None:
        plt.legend(loc=loc)

    # show plot
    plt.show()
