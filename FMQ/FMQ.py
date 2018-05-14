#!/usr/bin/python

from .abilities import abilities
import numpy as np
import pandas

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

    # Get ability list
    def get_ability_list(self):
        return abilities.toDict()

    # Get players with abilities more than threshold: (k, v == ability, lower bound)
    def filter_by_ability(self, *args, **kwargs):
        df = self.df
        for k, v in kwargs.items():
            df = df.loc[df[k] >= v]
        return df

    # Get player abilities in range
    def get_abilities_in_range(self, uid, low, high):
        df = self.get_player_by_id(uid).select_dtypes(include=[np.number])
        df = df[self.abilities.all + self.abilities.hidden]
        r = df.squeeze()
        return r.loc[r.between(low, high) == True]

    # Get ability average
    def get_average_ability(self, uid):
        df = self.get_player_by_id(uid).select_dtypes(include=[np.number])
        avg = {}
        for k, v in self.abilities.items():
            m = df[v].mean(axis=1)
            avg[k] = m.iat[0]
        return avg
