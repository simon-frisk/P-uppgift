import sys
import re

class TextInterface:
  '''Command line interface'''

  def __init__(self, graph):
    '''Textinterface constructor'''
    self.graph = graph

  def run(self):
    '''The main loop of the command line interface'''
    running = True

    extractNumbers = lambda string : list(map(lambda x: int(x), userInput.split(' ')[1:]))

    while running:
      userInput = input('Enter input ...\n')
      if userInput == 'p':
        self.printGraph()
      elif re.match('^r \d+ \d+$', userInput):
        self.graph.generateRandom(*extractNumbers(userInput))
      elif re.match('^s \d+ \d+$', userInput):
        numbers = extractNumbers(userInput)
        if self.graph.isCoordInGraph(numbers):
          self.graph.setStart(numbers)
        else: print('Coordinate outside graph')
      elif re.match('^g \d+ \d+$', userInput):
        numbers = extractNumbers(userInput)
        if self.graph.isCoordInGraph(numbers):
          self.graph.setGoal(numbers)
        else: print('Coordinate outside graph')
      elif userInput == 'save':
        self.graph.saveToFile()
      elif userInput == 'q':
        running = False
      else: print('Input invalid')

  def printGraph(self):
    '''Prints the graph to the command line'''
    for index, node in enumerate(self.graph.nodes):
      if index % self.graph.width == 0:
        print('\n', end='')

      nodeCharacter = '_'
      if node == self.graph.startNode:
        nodeCharacter = 'S'
      elif node == self.graph.goalNode:
        nodeCharacter = 'G'
      elif node in self.graph.bestPath:
        nodeCharacter = 'P'

      print(
        nodeCharacter,
        node.wind['strength'],
        self.getWindAngleString(node.wind['direction']),
        sep='', end='  '
      )
    print('\n\n', end='')

  def getWindAngleString(self, angle):
    '''Get a short string describing the wind direction'''
    windLetters = {
      0: 'N_',
      45: 'NE',
      90: 'E_',
      135: 'SE',
      180: 'S_',
      225: 'SW',
      270: 'W_',
      315: 'NW',
    }
    return windLetters[angle]