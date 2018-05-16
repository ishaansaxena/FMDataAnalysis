#!/usr/bin/python

from time import time
from scipy.spatial import distance
import matplotlib.pylab as plt

from FMQ import FMQ


MAIN_HELP = """
    0:  Help

    1:  Player by UID
        Requires:   UID

    2:  Players by Name
        Requires:   Name

    3:  Attribute List
        Requires:   None

    4:  Filter by Attributes
        Requires:   **kwargs

    5:  Get Attributes in Range
        Requires:   UID, lower, higher

    6:  Get Average Attributes
        Requires:   UID

    7:  Similar Players (Table)
        Requires:   UID

    8:  Similar Players (Table + Graph)
        Requires:   UID, factor (default = 2)

    -1: Exit
"""

def main():

    print("Initializing db")
    f = FMQ.FMQ("dataset.csv")
    print("\nWelcome to FMQS. Press 0 for help.\n")

    user_input = input(">> ")
    user_input = user_input.strip().split(" ")
    opt = int(user_input[0])

    while (opt != -1):

        start = time()
        success = False

        if opt == 0:
            print(MAIN_HELP)

        elif opt == 1:
            try:
                uid = int(user_input[1])
                print(f.get_player_by_id(uid))
                success = True
                end = time()
            except:
                print("Error\n")

        elif opt == 2:
            try:
                name = " ".join(user_input[1:])
                print(f.get_players_by_name(name))
                success = True
                end = time()
            except:
                print("Error\n")

        elif opt == 3:
            for k, v in f.get_attr_list().items():
                print(k, ":")
                print(v)
                print()

        elif opt == 4:
            # TODO: Fix
            kwargs = {}
            for i in range(1, len(user_input)):
                kv = user_input[i].split("=")
                k, v = kv[0], kv[1]
                kwargs[k] = v
            print(f.filter_by_attr(**kwargs))
            success = True
            end = time()

        elif opt == 5:
            try:
                uid = int(user_input[1])
                l = int(user_input[2])
                h = int(user_input[3])
                print(f.get_attr_in_range(uid, l, h))
                success = True
                end = time()
            except:
                print("Error\n")

        elif opt == 6:
            try:
                uid = int(user_input[1])
                print(f.get_average_player_attr(uid))
                success = True
                end = time()
            except:
                print("Error\n")

        elif opt == 7 or opt == 8:
            try:
                uid = int(user_input[1])
                factor = 2
                if len(user_input) > 2:
                    factor = int(user_input[2])
                df = f.get_similar_players(uid, factor).head(10 + 1)
                print(df)
                if opt == 8:
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
                success = True
                end = time()
                plt.show()
            except:
                print("Error\n")

        if success:
            print("Completed in ", end - start, "seconds\n")

        user_input = input(">> ")
        user_input = user_input.strip().split(" ")
        opt = int(user_input[0])

if __name__ == '__main__':
    main()
