#!/usr/bin/python

from .attributes import attributes
from scipy.spatial import distance
import numpy as np
import pandas

class FMQ:

    attributes = attributes
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
        # Return occurence when UID matches
        return df.loc[df["UID"] == uid]

    # Get players with name similar to
    def get_players_by_name(self, name):
        df = self.df
        # Return all occurence where name is similar
        return df[df["Name"].str.contains(name, case=False)]

    # Get ability list
    def get_attr_list(self):
        return attributes.toDict()

    # Get players with attributes more than threshold: (k, v == ability, lower bound)
    def filter_by_attr(self, *args, **kwargs):
        df = self.df
        # subset data with ability k at least of value v
        for k, v in kwargs.items():
            df = df.loc[df[k] >= v]
        return df

    # Get player attributes in range
    def get_attr_in_range(self, uid, low, high):
        df = self.get_player_by_id(uid).select_dtypes(include=[np.number])
        df = df[self.attributes.all + self.attributes.hidden]
        # Get series for a player
        r = df.squeeze()
        # Return column values when in the given range
        return r.loc[r.between(low, high) == True]

    # Get ability average
    def get_average_player_attr(self, uid):
        df = self.get_player_by_id(uid).select_dtypes(include=[np.number])
        avg = {}
        # Get average values for each subclass
        for k, v in self.attributes.items():
            m = df[v].mean(axis=1)
            avg[k] = m.iat[0]
        return avg

    # Euclidean distance
    def get_euclidean_distance(self, uid, vid):
        # Get both players
        df = self.get_player_by_id(uid)
        to = self.get_player_by_id(vid)
        m = {}
        exclude = ["all", "footedness", "hidden"]
        # For each subclass, calculate euclidean distance
        for k, v in self.attributes.items():
            if k in exclude: continue
            q = df[v]
            r = to[v]
            d = distance.euclidean(q, r)
            m[k] = d
        return m

    # Get players similar to current player (euclidean distance and stddev)
    def get_similar_players(self, uid, factor=None):
        # OPTIMIZE: Improve execution time of this method

        # Set factor to 2 by default
        if factor is None:
            factor = 2
        df = self.df

        # Get player to compare with
        player = self.get_player_by_id(uid)
        # Get threshold value for choosing attributes
        threshold = self.get_average_player_attr(uid)['all']
        # Choose all attributes above threshold value as critical
        # critical_attributes = [
            # col for col in self.get_attr_in_range(uid, threshold, 20).index
            # if col in self.attributes.all()
        # ]
        critical_attr_e = [column for column in self.get_attr_in_range(uid, threshold, 20).index if column in self.attributes.all]
        critical_attr_f = [column for column in self.get_attr_in_range(uid, 0, threshold - 1).index if column in self.attributes.all]

        # Squeeze player into series
        player_series = player.squeeze()
        # Get subset within one stddev of each critical attribute
        for attr in critical_attr_e:
            m = player_series.at[attr]
            s = self.stddev.at[attr]
            # if only_lower:
            df = df.loc[df[attr] >= m - factor * s]
            # else:
                # df = df.loc[df[index] >= m - s].loc[df[index] <= m + s]

        # Get similar players
        similar = []
        title = ["UID", "Name", "e_delta", "f_delta"]
        for row in df.itertuples():
            # Get distance e
            q = player[critical_attr_e]
            r = [getattr(row, attr) for attr in critical_attr_e]
            e_delta = distance.euclidean(q, r)
            # Get distance f
            q = player[critical_attr_f]
            r = [getattr(row, attr) for attr in critical_attr_f]
            f_delta = distance.euclidean(q, r)
            similar.append([getattr(row, "UID"), getattr(row, "Name"), e_delta, f_delta])
        df = pandas.DataFrame(similar, columns=title)
        df.sort_values(by=['e_delta', 'f_delta'], inplace=True)
        return df
