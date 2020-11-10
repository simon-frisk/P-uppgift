import math


class Node:
    def __init__(self, wind):
        self.wind = wind
        self.distance = math.inf
        self.numNodesFromStart = math.inf
        self.previous = None
        self.is_goal = False
        self.neighBors = [None for _ in range(8)]
        self.pathIndex = None

    def visit(self):
        for index, neighbor in enumerate(self.neighBors):
            if not neighbor:
                continue
            distance = self.distance + self.calculateDistance(index)
            if distance < neighbor.distance:
                neighbor.distance = distance
                neighbor.numNodesFromStart = self.numNodesFromStart + 1
                neighbor.previous = self

    def calculateDistance(self, neighborIndex):
        sailing_type = abs(self.wind['direction'] / 45 - neighborIndex + 1)
        distance = 1 if neighborIndex in [1, 3, 5, 7] else math.sqrt(2)
        if sailing_type == 0:
            return math.inf
        elif sailing_type == 1 or sailing_type == 7:
            return self.wind['strength'] * distance if self.wind['strength'] < 5 else math.inf
        elif sailing_type == 2 or sailing_type == 6:
            constant = .5 if self.wind['strength'] < 7 else .25
            return self.wind['strength'] * constant * distance
        elif sailing_type == 3 or sailing_type == 5:
            return self.wind['strength'] * .3 * distance
        else:
            constant = .25 if self.wind['strength'] < 9 else .5
            return self.wind['strength'] * constant * distance

    def __lt__(self, other):
        return self.distance < other.distance
