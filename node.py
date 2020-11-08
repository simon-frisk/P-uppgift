import math


class Node:
    def __init__(self, wind):
        self.wind = wind
        self.distance = math.inf
        self.is_goal = False
        self.upNode = None
        self.downNode = None
        self.rightNode = None
        self.leftNode = None
        self.rightUpNode = None
        self.leftDownNode = None
        self.rightDownNode = None
        self.leftUpNode = None
