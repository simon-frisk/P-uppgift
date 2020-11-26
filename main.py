import sys
from graph import Graph
from gui import Gui


def main():
    graph = Graph()
    mode = sys.argv[1] if len(sys.argv) == 2 else None
    if mode == '-gui':
        gui = Gui(graph)
        gui.run()
    elif mode == '-cli':
        pass
    else:
        print('No mode choosen')


if __name__ == '__main__':
    main()
