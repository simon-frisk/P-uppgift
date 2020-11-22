import sys
from graph import Graph
import gui


def main():
    graph = Graph()
    #graph.setStart((1, 1))
    #graph.setGoal((10, 10))
    #graph.calculateFastestRoute()
    mode = sys.argv[1] if len(sys.argv) == 2 else None
    if mode == '-gui':
        gui.createGUI(graph)
    elif mode == '-cli':
        #print(str(graph))
        pass
    else:
        print('No mode choosen')


if __name__ == '__main__':
    main()
