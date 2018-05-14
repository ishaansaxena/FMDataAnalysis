from FMQ import FMQ

def main():
    f = FMQ("dataset.csv")
    print(f.shape())
    print(f.summary())

if __name__ == '__main__':
    main()
