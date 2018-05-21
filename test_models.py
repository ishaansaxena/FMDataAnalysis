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

from multiprocessing import cpu_count
from multiprocessing.dummy import Pool as ThreadPool
from threading import Lock, current_thread

from FMQ import FMQ
from FMQ import positions
from FMQ import attributes

# Mutex
mutex = Lock()

# Model evaluation
results = []
names = []

def test_model(mtuple):
    # Get model name and model instance
    name, model = mtuple

    # Start processing model in thread X
    print("Testing %s analysis in Thread: \t%s" % (name, current_thread()))
    start = time()

    # Fix for joblib issue
    # TODO: Find better fix
    current_thread().name = 'MainThread'

    # Train model with training data
    try:
        kfold = model_selection.KFold(n_splits=8, random_state=seed)
        cv_results = model_selection.cross_val_score(
            model, X_train, Y_train,
            cv=kfold, scoring=scoring
        )
    except Exception as e:
        # Print exception
        print("Exception: %s at testModel(%s)" % (e, name))

    # Logging Statistics
    t = time() - start
    result = "Complete training %s:\t%f (%f)\tin %s seconds" % (name, cv_results.mean(), cv_results.std(), t)

    # Write results
    mutex.acquire()
    try:
        results.append(cv_results)
        names.append(name)
        print(result)
    except Exception as e:
        # Print exception
        print("Exception: %s at testModel(%s)" % (e, name))
    finally:
        mutex.release()

    return None

def main():

    # Data subsets
    global X_train, X_validation, Y_train, Y_validation

    # Validation parameters
    global validation_size
    global seed
    global scoring

    # Load database
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
    X = df[a.all].values                  # Abilities
    Y = df["Position"].values.ravel()     # Positions

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

    # Training process
    numThreads = min([len(models), cpu_count()])
    threadPool = ThreadPool(numThreads)
    # Start threads
    threadPool.map(test_model, models)
    # Wait for threads to finish
    threadPool.close()
    threadPool.join()

    # Compare model results visually
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()

if __name__ == '__main__':
    main()
