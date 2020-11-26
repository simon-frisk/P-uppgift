import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import pygame_gui
import math

class Gui:
    '''Class for GUI object, which handles creating and running GUI'''

    def __init__(self, graph):
        self.graph = graph
        self.FPS = 50
        self.gui_width = 250
        self.sea_height = 650
        self.sea_width = seaWidth = round((self.graph.width / self.graph.height) * self.sea_height)
        self.node_width = self.sea_width // self.graph.width

        pygame.init()
        self.surface = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption('Sailing')
        self.ui_manager = pygame_gui.UIManager(self.dimensions)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, round(self.node_width / 2.5))

        windArrowImage = pygame.image.load('assets/arrow.png')
        self.windArrowImage = pygame.transform.scale(windArrowImage, (self.node_width, self.node_width))

        self.initGui()

    def initGui(self):
        '''Init the user interface'''
        self.generateNewGraphButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.sea_width + 10, 10), (self.gui_width - 20, 40)),
            text='Generate new graph',
            manager=self.ui_manager
        )

    @property
    def dimensions(self):
        return (self.sea_width + self.gui_width, self.sea_height)

    def run(self):
        while True:
            time_delta = self.clock.tick(self.FPS) / 1000.0
            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    row = event.pos[1] // self.node_width
                    column = event.pos[0] // self.node_width
                    #TODO: clicked outside sea
                    if pressed[pygame.K_s]:
                        self.graph.setStart((column, row))
                    if pressed[pygame.K_g]:
                       self.graph.setGoal((column, row))
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.generateNewGraphButton:
                            self.graph.generateRandom(self.graph.width, self.graph.height)
                self.ui_manager.process_events(event)

            self.updateGui(time_delta)
            self.renderGraph()
            
            pygame.display.update()

    def updateGui(self, time_delta):
        self.ui_manager.update(time_delta)
        self.ui_manager.draw_ui(self.surface)
        
    def renderGraph(self):
        '''Render the graph on the screen'''
        for index, node in enumerate(self.graph.nodes):
            x = index % self.graph.width * self.node_width
            y = index // self.graph.width * self.node_width

            pygame.draw.rect(self.surface, (0, 100, 255), (x, y, self.node_width, self.node_width))
            if node == self.graph.startNode:
                pygame.draw.rect(self.surface, (255, 200, 0), (x, y, self.node_width, self.node_width), 2)
            elif node == self.graph.goalNode:
                pygame.draw.rect(self.surface, (255, 0, 0), (x, y, self.node_width, self.node_width), 2)
            elif node in self.graph.bestPath:
                pygame.draw.rect(self.surface, (100, 255, 0), (x, y, self.node_width, self.node_width), 2)

            rotatedImage = pygame.transform.rotate(self.windArrowImage, 180 - node.wind['direction'])
            self.surface.blit(rotatedImage, (x, y))

            distanceString = str(round(node.distance, 2))
            text = self.font.render(distanceString, False, (0, 0, 0))
            self.surface.blit(text, (x, y))
            
            strengthString = str(node.wind['strength'])
            text = self.font.render(strengthString, False, (255, 255, 255))
            textX = x + self.node_width / 2 - self.font.size(strengthString)[0] / 2
            textY = y + self.node_width / 2 - self.font.size(strengthString)[1] / 2
            self.surface.blit(text, (textX, textY))
