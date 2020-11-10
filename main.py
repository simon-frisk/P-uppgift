import util
from graph import Graph


def main():
    dimensions, wind_data = util.read_wind_data()
    graph = Graph(dimensions, wind_data)
    graph.setStart((0, 0))
    graph.setGoal((1, 2))
    graph.calculateFastestRoute()
    print(str(graph))


if __name__ == '__main__':
    main()
