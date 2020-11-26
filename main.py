import sys
from graph import Graph
import gui


def main():
    graph = Graph()
    mode = sys.argv[1] if len(sys.argv) == 2 else None
    if mode == '-gui':
        gui.createGUI(graph)
    elif mode == '-cli':
        pass
    else:
        print('No mode choosen')


if __name__ == '__main__':
    main()
