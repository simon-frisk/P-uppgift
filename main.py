import util


def main():
    dimensions, wind_data = util.read_wind_data()
    print(dimensions, wind_data)


if __name__ == '__main__':
    main()
