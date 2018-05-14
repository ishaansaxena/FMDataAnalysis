#!/usr/bin/python

from .abilities import abilities
import pandas
import numpy

class FMQ:
    
    abilities = abilities

    ### Constructors
    # Initialize with a specific url
    def __init__(self, url):
        self.url = url
        self.df  = pandas.read_csv(self.url)

    ### Summary Methods
    # Datafram shape
    def shape(self):
        return self.df.shape

    # Statistical summary
    def summary(self):
        return self.df.describe()

    # Data head default
    def head(self):
        return self.df.head(5)

    # Data head specific
    def head(self, n):
        return self.df.head(n)

    ### Query methods
    # Get player by UID
    def get_player_by_id(self, uid):
        df = self.df
        return df.loc[df["UID"] == uid]

    # Get players with name similar to
    def get_players_by_name(self, name):
        df = self.df
        return df[df["Name"].str.contains(name, case=False)]
