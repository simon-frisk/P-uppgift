import util


def main():
    dimensions, wind_data = util.read_wind_data()
    graph = util.initGraph(dimensions, wind_data)


if __name__ == '__main__':
    main()
