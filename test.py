from FMQ import FMQ
from time import time
import sys

def main():
    uid = int(sys.argv[1])
    if len(sys.argv) > 2:
        factor = float(sys.argv[2])
    else:
        factor = 2
    f = FMQ.FMQ("dataset.csv")
    start = time()
    # df = f.get_similar_players(uid, factor)
    # df['sum'] = df['mental'] + df['technical']
    # df.sort_values(by=['sum'], inplace=True)
    # print(df)
    f.get_player_by_id(uid)
    f.get_players_by_name('lionel')
    f.get_attr_list()
    f.filter_by_attr(Flair=19)
    f.get_attr_in_range(uid, 15, 20)
    f.get_average_player_attr(uid)
    f.get_euclidean_distance(uid, 18007344)
    print(f.get_similar_players(uid, factor))
    print(time() - start, "seconds")

if __name__ == '__main__':
    main()
