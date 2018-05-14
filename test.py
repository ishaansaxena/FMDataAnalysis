from FMQ import FMQ

def main():
    f = FMQ.FMQ("dataset.csv")
    df = f.df
    print(f.get_player_by_id(7458500))
    print(f.get_players_by_name("lionel"))

if __name__ == '__main__':
    main()
