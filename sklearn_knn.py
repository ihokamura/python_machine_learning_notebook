"""
show sample of how to use KNeighborsClassifier
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from data_utility import IrisData
from plot_utility import plot_decision_regions


def main():
    # prepare sample data and target variable
    labels = ['setosa', 'versicolor', 'virginica']
    features = ['petal length (cm)', 'petal width (cm)']
    D = IrisData(features, labels)
    X = D.X
    y = D.y

    # split sample data into training data and test data and standardize them
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
    sc = StandardScaler().fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    # combine training data and test data
    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))

    # fit classifiers
    classifiers = [
        KNeighborsClassifier(n_neighbors=4, p=2, metric='minkowski').fit(X_train_std, y_train),
        KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski').fit(X_train_std, y_train),
        KNeighborsClassifier(n_neighbors=6, p=2, metric='minkowski').fit(X_train_std, y_train),
        KNeighborsClassifier(n_neighbors=5, p=1, metric='minkowski').fit(X_train_std, y_train)
    ]

    for classifier in classifiers:
        # show accuracy
        y_pred = classifier.predict(X_test_std)
        print('misclassified samples: {}'.format(np.sum(y_test != y_pred)))

        # show decision regions
        plot_decision_regions(X_combined_std, y_combined, classifier=classifier, test_idx=list(range(len(y_train), len(y))))


if __name__ == '__main__':
    main()
