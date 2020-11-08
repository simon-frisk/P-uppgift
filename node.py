import math


class Node:
    def __init__(self, wind):
        self.wind = wind
        self.distance = math.inf
        self.is_goal = False
        self.neighBors = [None for _ in range(8)]

    def __lt__(self, other):
        return self.distance < other.distance
