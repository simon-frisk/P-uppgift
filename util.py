import node
import heapq
import copy


def read_wind_data():
    '''Reads wind data from file'''
    data_file = open('wind_data.txt', 'r')
    width, height = data_file.readline().strip().split(' ')
    raw_wind_data = data_file.readline().strip().split(' ')
    wind_data = []
    for node in raw_wind_data:
        strength, direction = node.split('/')
        wind_data.append({'strength': int(strength),
                          'direction': int(direction)})
    return {'width': int(width), 'height': int(height)}, wind_data


def initGraph(dimensions, wind_data):
    '''Initializes a graph for the wind map, consisting of nodes with a relation to each other'''
    nodes = []
    for y in range(dimensions['height']):
        for x in range(dimensions['width']):
            index = x + y * dimensions['width']
            currentNode = node.Node(wind_data[index])
            nodes.append(currentNode)

            # Check if neighboring nodes exist, and if they do, add a relation.
            if index % dimensions['width'] != 0:
                leftNode = nodes[index - 1]
                leftNode.rightNode = currentNode
                currentNode.leftNode = leftNode
            if index % dimensions['width'] != 0 and not index < dimensions['width']:
                leftUpNode = nodes[index - 1 - dimensions['width']]
                leftUpNode.rightDownNode = currentNode
                currentNode.leftUpNode = leftUpNode
            if not index < dimensions['width']:
                upNode = nodes[index - dimensions['width']]
                upNode.downNode = currentNode
                currentNode.upNode = upNode
            if not index < dimensions['width'] and index % dimensions['width'] != dimensions['width'] - 1:
                rightUpNode = nodes[index + 1 - dimensions['width']]
                rightUpNode.leftDownNode = currentNode
                currentNode.rightUpNode = rightUpNode
    return nodes


def setGraphStartAndGoal(graph, start_pos, goal_pos, width):
    graph[start_pos[1] * width + start_pos[0]].distance = 0
    graph[goal_pos[1] * width + goal_pos[0]].is_goal = True


def getPriorityQueue(graph):
    graph_copy = copy.copy(graph)
    heapq.heapify(graph_copy)
    return graph_copy
