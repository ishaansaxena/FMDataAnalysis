#!/usr/bin/python

from time import time
import sys
from scipy.spatial import distance
import matplotlib.pylab as plt

from sklearn import model_selection

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from FMQ import FMQ
from FMQ import positions
from FMQ import attributes


def main():

    print("Loading DB")
    f = FMQ.FMQ("dataset.csv")

    # Get dataset
    df = f.df
    p = positions.positions
    a = attributes.attributes

    # Create position classes
    df["Position"] = df[p.all].idxmax(axis=1)

    # Import models
    models = []
    models.append(("LR", LogisticRegression()))
    models.append(("CART", DecisionTreeClassifier()))
    models.append(("KNN", KNeighborsClassifier()))
    models.append(("LDA", LinearDiscriminantAnalysis()))
    models.append(("NB", GaussianNB()))
    models.append(("SVC", SVC()))

    # Create predictors
    X = df[a.all].values        # Abilities
    Y = df["Position"].values   # Positions

    # Validation parameters
    validation_size = 0.50
    seed = 7
    scoring = "accuracy"

    # Create sets
    print("Creating Test/Validation Data")
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
        X, Y,
        test_size=validation_size,
        random_state=seed
    )

    # Model evaluation
    results = []
    names = []

    for name, model in models:
        print("Testing %s" % name)
        kfold = model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = model_selection.cross_val_score(
            model, X_train, Y_train,
            cv=kfold, scoring=scoring
        )
        results.append(cv_results)
        names.append(name)
        result = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(result)

    # Compare model results visually
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()

if __name__ == '__main__':
    main()
