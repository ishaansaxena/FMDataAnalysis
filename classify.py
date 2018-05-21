#!/usr/bin/python

import numpy as np

from sklearn import model_selection
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from FMQ import FMQ
from FMQ import positions
from FMQ import attributes

def main():

    # Data subsets
    global X_train, X_validation, Y_train, Y_validation

    # Validation parameters
    global validation_size
    global seed

    # Load database
    print("Loading DB")
    f = FMQ.FMQ("dataset.csv")

    # Get dataset
    df = f.df
    p = positions.positions
    a = attributes.attributes

    # Create position classes
    df["Position"] = df[p.all].idxmax(axis=1)

    # Create predictors
    X = df[a.all].values                  # Abilities
    Y = df["Position"].values.ravel()     # Positions

    # Validation parameters
    validation_size = 0.50
    seed = 7

    # Create sets
    print("Creating Test/Validation Data")
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
        X, Y,
        test_size=validation_size,
        random_state=seed
    )

    lda = LinearDiscriminantAnalysis()
    lda.fit(X_train, Y_train)
    predictions = lda.predict(X_validation)
    print("Validation results:")
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))

if __name__ == '__main__':
    main()
