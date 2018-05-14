#!/usr/bin/python

import pandas

class FMQ:

    # Class constructor
    def __init__(self, url):
        self.url = url
        self.df  = pandas.read_csv(self.url)

    # Return dataset shape
    def shape(self):
        # Print shape
        return self.df.shape

    # Statistical summary
    def summary(self):
        return self.df.describe()

    # Data head
    def head(self):
        return self.df.head(5)

    def head(self, n):
        return self.df.head(n)
