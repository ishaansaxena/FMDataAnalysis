from FMQ import FMQ

def main():
    f = FMQ.FMQ("dataset.csv")
    # print(f.get_players_by_name("lionel"))
    # print(f.get_player_by_id(7458500))
    # print(f.get_ability_list())
    # print(f.filter_by_ability(OneOnOnes=19, AerialAbility=10))
    # print(f.get_abilities_in_range(7458500, 15, 20))
    # print(f.get_average_ability(7458500))

if __name__ == '__main__':
    main()
