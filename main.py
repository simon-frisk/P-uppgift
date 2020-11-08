import util


def main():
    dimensions, wind_data = util.read_wind_data()
    graph = util.initGraph(dimensions, wind_data)
    start_pos = (1, 1)
    goal_pos = (3, 3)
    util.setGraphStartAndGoal(graph, start_pos, goal_pos, dimensions['width'])


if __name__ == '__main__':
    main()
