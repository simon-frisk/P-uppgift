import sys
from graph import Graph
from gui import Gui
import TextInterface


def main():
    graph = Graph()
    mode = sys.argv[1] if len(sys.argv) == 2 else None
    if mode == '-gui':
        gui = Gui(graph)
        gui.run()
    elif mode == '-cli':
        cli = TextInterface.TextInterface(graph)
        cli.run()
    else:
        print('No mode choosen')


if __name__ == '__main__':
    main()
