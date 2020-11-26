import node
import heapq
import copy
import random


class Graph:
    '''Class for Graph objects, which represents the whole sea. Stores all nodes,
    can manipulate graph and calculate fastest route'''

    def __init__(self):
        '''Graph constructor'''
        self.width = None
        self.height = None
        self.nodes = []
        self.goalNode = None
        self.startNode = None
        self.bestPath = []
        self.loadFromFile()

    def buildGraph(self, wind_data, width, height):
        '''Build the graph from wind_data. Store nodes in self.nodes'''
        self.width = width
        self.height = height
        self.nodes = []
        self.startNode = None
        self.goalNode = None
        self.bestPath = []
        for y in range(self.height):
            for x in range(self.width):
                index = x + y * self.width
                currentNode = node.Node(wind_data[index])
                self.nodes.append(currentNode)
                # Check if neighboring nodes exist, and if they do, add a relation.
                if index % self.width != 0:
                    leftNode = self.nodes[index - 1]
                    leftNode.neighBors[3] = currentNode
                    currentNode.neighBors[7] = leftNode
                if index % self.width != 0 and not index < self.width:
                    leftUpNode = self.nodes[index - 1 - self.width]
                    leftUpNode.neighBors[4] = currentNode
                    currentNode.neighBors[0] = leftUpNode
                if not index < self.width:
                    upNode = self.nodes[index - self.width]
                    upNode.neighBors[5] = currentNode
                    currentNode.neighBors[1] = upNode
                if not index < self.width and index % self.width != self.width - 1:
                    rightUpNode = self.nodes[index + 1 - self.width]
                    rightUpNode.neighBors[6] = currentNode
                    currentNode.neighBors[2] = rightUpNode


    def loadFromFile(self):
        '''Reads wind data from file and builds graph from this'''
        data_file = open('wind_data.txt', 'r')

        width, height = data_file.readline().strip().split(' ')
        width = int(width)
        height = int(height)

        raw_wind_data = data_file.readline().strip().split(' ')
        wind_data = []
        for node in raw_wind_data:
            strength, direction = node.split('/')
            wind_data.append({'strength': int(strength),
                            'direction': int(direction)})
        self.buildGraph(wind_data, width, height)

    def generateRandom(self, width, height):
        '''Randomly generate a new graph'''
        wind_data = []
        for h in range(height):
            for w in range(width):
                strength = random.randrange(10)
                direction = random.choice([0, 45, 90, 135, 180, 225, 270, 315])
                wind_data.append({'strength': strength, 'direction': direction})
        self.buildGraph(wind_data, width, height)

    def setStart(self, start_pos):
        self.startNode = self.nodes[start_pos[1] * self.width + start_pos[0]]
        self.calculateFastestRoute()

    def setGoal(self, goal_pos):
        self.goalNode = self.nodes[goal_pos[1] * self.width + goal_pos[0]]
        self.calculateFastestRoute()

    def reset(self):
        for node in self.nodes:
            node.reset()
        self.startNode.distance = 0
        self.bestPath = []

    def calculateFastestRoute(self):
        if not self.startNode or not self.goalNode: return
        self.reset()
        prioQueue = self.getPriorityQueue()
        while True:
            node = heapq.heappop(prioQueue)
            if node == self.goalNode:
                while node != None:
                    self.bestPath.append(node)
                    node = node.previous
                self.bestPath.reverse()
                break
            node.visit()
            heapq.heapify(prioQueue)

    def getPriorityQueue(self):
        graph_copy = copy.copy(self.nodes)
        heapq.heapify(graph_copy)
        return graph_copy