from FMQ import FMQ

def main():
    f = FMQ.FMQ("dataset.csv")
    print(f.shape())
    print(f.summary())
    print([k for k, v in f.abilities.items()])

if __name__ == '__main__':
    main()
