import math


class Node:
    '''Class describing one node in the graph'''

    def __init__(self, wind):
        '''Node constructor'''
        self.wind = wind
        self.neighBors = [None for _ in range(8)]
        self.reset()

    def reset(self):
        '''Reset node to beginning state so Dijstra can be run again'''
        self.distance = math.inf
        self.previous = None
        self.bestPathIndex = None

    def visit(self):
        '''Visit node step of dijstra'''
        for index, neighbor in enumerate(self.neighBors):
            if not neighbor:
                continue
            distance = self.distance + self.calculateDistance(index)
            if distance < neighbor.distance:
                neighbor.distance = distance
                neighbor.previous = self

    def calculateDistance(self, neighborIndex):
        '''Calculates distance from this node to some neighbor node'''
        sailing_type = abs(self.wind['direction'] / 45 - (neighborIndex - 1))
        distance = 1 if neighborIndex in [1, 3, 5, 7] else math.sqrt(2)
        if sailing_type == 0 or sailing_type == 8:
            speed = 0
        elif sailing_type == 1 or sailing_type == 7:
            speed = self.wind['strength'] if self.wind['strength'] < 5 else 0
        elif sailing_type == 2 or sailing_type == 6:
            constant = .5 if self.wind['strength'] < 7 else .25
            speed = self.wind['strength'] * constant
        elif sailing_type == 3 or sailing_type == 5:
            speed = self.wind['strength'] * .3
        else:
            constant = .25 if self.wind['strength'] < 9 else .5
            speed = self.wind['strength'] * constant
        
        if speed == 0: return math.inf
        else: return distance / speed

    def __lt__(self, other):
        '''Compares two nodes so a node list can be sorted'''
        return self.distance < other.distance
