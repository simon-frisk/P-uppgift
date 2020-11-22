import util
from graph import Graph
import gui


def main():
    dimensions, wind_data = util.read_wind_data()
    graph = Graph(dimensions, wind_data)
    graph.setStart((1, 1))
    graph.setGoal((10, 10))
    graph.calculateFastestRoute()
    print(str(graph))
    gui.createGUI(graph, dimensions)


if __name__ == '__main__':
    main()
