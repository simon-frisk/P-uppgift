import sys
import re


class TextInterface:
  '''Class for the command line interface'''

  def __init__(self, graph):
    '''Textinterface constructor'''
    self.graph = graph

  def run(self):
    '''The main loop of the command line interface'''
    running = True

    # Help function for extracting two numbers from input string, see further down
    extractNumbers = lambda string : list(map(lambda x: int(x), userInput.split(' ')[1:]))

    while running:
      userInput = input('Enter input ...\n')

      if userInput == 'print':
        self.printGraph()

      elif re.match('^random \d+ \d+$', userInput):
        self.graph.generateRandom(*extractNumbers(userInput))

      elif re.match('^start \d+ \d+$', userInput):
        numbers = extractNumbers(userInput)
        if self.graph.isCoordInGraph(numbers):
          self.graph.setStart(numbers)
        else: print('Coordinate outside graph')

      elif re.match('^goal \d+ \d+$', userInput):
        numbers = extractNumbers(userInput)
        if self.graph.isCoordInGraph(numbers):
          self.graph.setGoal(numbers)
        else: print('Coordinate outside graph')

      elif userInput == 'save':
        self.graph.saveToFile()

      elif userInput == 'quit':
        running = False

      elif userInput == 'help':
        print(
          'Press random n m to generate a new sea of n * m dimension',
          'Press print to print the current graph',
          'Press start n m to set node at coordinate n m to the start node',
          'Press goal n m to set node at coordinate n m to the goal node',
          'Press save to save current sea',
          'Press quit to exit program',
          sep='\n'
        )

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
      elif node.bestPathIndex != None:
        nodeCharacter = node.bestPathIndex

      print(
        nodeCharacter,
        node.wind['strength'],
        self.getWindAngleString(node.wind['direction']),
        sep='', end='  '
      )
    print('\n\n', end='')


  def getWindAngleString(self, angle):
    '''Get a short string describing the wind direction based on the angle of the wind'''
    windLetters = {
      0: 'N ',
      45: 'NE',
      90: 'E ',
      135: 'SE',
      180: 'S ',
      225: 'SW',
      270: 'W ',
      315: 'NW',
    }
    return windLetters[angle]