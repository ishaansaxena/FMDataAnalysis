#!/usr/bin/python

from scipy.spatial import distance
from time import time
from FMQ import FMQ
import sys
import matplotlib.pylab as plt

def main():
    uid = int(sys.argv[1])
    if len(sys.argv) > 2:
        factor = float(sys.argv[2])
    else:
        factor = 2
    f = FMQ.FMQ("dataset.csv")
    start = time()
    # f.get_player_by_id(uid)
    # f.get_players_by_name('lionel')
    # f.get_attr_list()
    # f.filter_by_attr(Flair=19)
    # f.get_attr_in_range(uid, 15, 20)
    # f.get_average_player_attr(uid)
    # f.get_euclidean_distance(uid, 18007344)
    df = f.get_similar_players(uid, factor).head(10 + 1)
    print(df)
    #
    # plt.scatter(df.e_delta, df.f_delta)
    # plt.text(df.e_delta, df.f_delta, df.Name)
    # plt.show()
    labels = df.Name
    x_data = df.e_delta
    y_data = df.f_delta
    plt.scatter(x_data, y_data)
    for label, x, y in zip(labels, x_data, y_data):
        plt.annotate(
            label,
            xy = (x, y),
            xytext=(5, 0), textcoords="offset points",
            ha='left', va='center',
        )
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    print(time() - start, "seconds")
    plt.show()

if __name__ == '__main__':
    main()
