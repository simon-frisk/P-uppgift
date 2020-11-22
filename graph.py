import node
import heapq
import copy


class Graph:
    def __init__(self, dimensions, wind_data):
        self.dimensions = dimensions
        self.nodes = []

        for y in range(dimensions['height']):
            for x in range(dimensions['width']):
                index = x + y * dimensions['width']
                currentNode = node.Node(wind_data[index])
                self.nodes.append(currentNode)

                # Check if neighboring nodes exist, and if they do, add a relation.
                if index % dimensions['width'] != 0:
                    leftNode = self.nodes[index - 1]
                    leftNode.neighBors[3] = currentNode
                    currentNode.neighBors[7] = leftNode
                if index % dimensions['width'] != 0 and not index < dimensions['width']:
                    leftUpNode = self.nodes[index - 1 - dimensions['width']]
                    leftUpNode.neighBors[4] = currentNode
                    currentNode.neighBors[0] = leftUpNode
                if not index < dimensions['width']:
                    upNode = self.nodes[index - dimensions['width']]
                    upNode.neighBors[5] = currentNode
                    currentNode.neighBors[1] = upNode
                if not index < dimensions['width'] and index % dimensions['width'] != dimensions['width'] - 1:
                    rightUpNode = self.nodes[index + 1 - dimensions['width']]
                    rightUpNode.neighBors[6] = currentNode
                    currentNode.neighBors[2] = rightUpNode

    def setStart(self, start_pos):
        startNode = self.nodes[start_pos[1] * self.dimensions['width'] +
                               start_pos[0]]
        startNode.distance = 0
        startNode.numNodesFromStart = 0

    def setGoal(self, goal_pos):
        self.nodes[goal_pos[1] * self.dimensions['width'] +
                   goal_pos[0]].is_goal = True

    def calculateFastestRoute(self):
        prioQueue = self.getPriorityQueue()
        while True:
            node = heapq.heappop(prioQueue)
            if node.is_goal:
                while node != None:
                    node.pathIndex = 1
                    node = node.previous
                break
            node.visit()
            heapq.heapify(prioQueue)

    def getPriorityQueue(self):
        graph_copy = copy.copy(self.nodes)
        heapq.heapify(graph_copy)
        return graph_copy

    def __str__(self):
        decoration = '-' * self.dimensions['width']
        string = decoration + '\n'

        for index, node in enumerate(self.nodes):
            string += str(node.numNodesFromStart) if node.pathIndex else ' '
            if (index + 1) % self.dimensions['width'] == 0:
                string += '\n'
        string += decoration
        return string
