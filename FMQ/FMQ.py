#!/usr/bin/python

from .abilities import abilities
from scipy.spatial import distance
import numpy as np
import pandas

class FMQ:

    abilities = abilities
    stddev = None

    ### Constructors
    # Initialize with a specific url
    def __init__(self, url):
        self.url = url
        self.df  = pandas.read_csv(self.url)
        self.stddev = self.df.std()

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
    def get_average_player_ability(self, uid):
        df = self.get_player_by_id(uid).select_dtypes(include=[np.number])
        avg = {}
        for k, v in self.abilities.items():
            m = df[v].mean(axis=1)
            avg[k] = m.iat[0]
        return avg

    # Euclidean distance
    def get_euclidean_distance(self, uid, vid):
        df = self.get_player_by_id(uid)
        to = self.get_player_by_id(vid)
        m = {}
        exclude = ["all", "footedness", "hidden"]
        for k, v in self.abilities.items():
            if k in exclude: continue
            q = df[v]
            r = to[v]
            d = distance.euclidean(q, r)
            m[k] = d
        return m

    # Get players similar to current player (euclidean distance and stddev)
    def get_similar_players(self, uid):
        # OPTIMIZE: Improve execution time of this method
        df = self.df
        player = self.get_player_by_id(uid)
        player_series = player.squeeze()
        threshold = self.get_average_player_ability(uid)['all']
        critical_abilities = self.get_abilities_in_range(uid, threshold, 20)
        for index in critical_abilities.index:
            m = player_series.at[index]
            s = 3 * self.stddev.at[index]
            df = df.loc[df[index] >= m - s].loc[df[index] <= m + s]
        euclidean = []
        title = None
        for player in df.itertuples():
            vid = getattr(player, "UID")
            name = getattr(player, "Name")
            dist = self.get_euclidean_distance(uid, vid)
            euclidean.append([vid, name] + list([v for k, v in dist.items()]))
            if title == None:
                title = ["UID", "Name"] + list([k for k, v in dist.items()])
        return pandas.DataFrame(euclidean, columns=title)
