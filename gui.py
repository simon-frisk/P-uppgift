import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import pygame_gui
import math

class Gui:
    '''Class for GUI object, which handles creating and running GUI and rendering on the screen'''

    def __init__(self, graph):
        '''GUI contructor'''
        self.graph = graph
        self.FPS = 50
        self.gui_width = 250
        self.sea_height = None
        self.sea_width = None
        self.node_width = None
        
        pygame.init()
        self.windArrowImage = pygame.image.load('assets/arrow.png')
        self.updateDimensions()
        self.surface = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption('Sailing')
        self.ui_manager = pygame_gui.UIManager((self.gui_width, self.sea_height))
        self.initGui()

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, round(self.node_width / 2.5))

    def updateDimensions(self):
        '''Update dimensions of window and sea according to graph'''
        self.sea_height = 650
        self.sea_width = round((self.graph.width / self.graph.height) * self.sea_height)
        self.node_width = self.sea_width // self.graph.width
        self.surface = pygame.display.set_mode(self.dimensions)
        self.scaledWindArrowImage = pygame.transform.scale(self.windArrowImage, (self.node_width, self.node_width))


    def initGui(self):
        '''Init the user interface'''
        self.generateNewGraphButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10, 10), (self.gui_width - 20, 40)),
            manager=self.ui_manager,
            text='Generate new graph',
        )
        self.widthTextBox = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((10, 60), (self.gui_width / 2 - 20, 40)),
            manager=self.ui_manager,
        )
        self.heightTextBox = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.gui_width / 2 + 10, 60), (self.gui_width / 2 - 20, 40)),
            manager=self.ui_manager,
        )
        self.widthTextBox.set_text(str(self.graph.width))
        self.heightTextBox.set_text(str(self.graph.height))
        self.widthTextBox.set_allowed_characters('numbers')
        self.heightTextBox.set_allowed_characters('numbers')

    @property
    def dimensions(self):
        return (self.sea_width + self.gui_width, self.sea_height)

    def run(self):
        '''Run the GUI main loop'''
        while True:
            time_delta = self.clock.tick(self.FPS) / 1000.0
            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = (event.pos[0] - self.gui_width) // self.node_width
                    y = event.pos[1] // self.node_width
                    if y >= 0 and y < self.sea_height and x >= 0 and x < self.sea_height:
                        if pressed[pygame.K_s]:
                            self.graph.setStart((x, y))
                        if pressed[pygame.K_g]:
                            self.graph.setGoal((x, y))
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.generateNewGraphButton:
                            if self.widthTextBox.get_text() != '' and self.heightTextBox.get_text() != '':
                                width = int(self.widthTextBox.get_text())
                                height = int(self.heightTextBox.get_text())
                                self.graph.generateRandom(width, height)
                                self.updateDimensions()
                self.ui_manager.process_events(event)

            self.surface.fill((0, 0, 0))
            self.renderUI(time_delta)
            self.renderGraph()
            
            pygame.display.update()

    def renderUI(self, time_delta):
        '''Render control ui'''
        self.ui_manager.update(time_delta)
        self.ui_manager.draw_ui(self.surface)
        
    def renderGraph(self):
        '''Render the graph on the screen'''
        for index, node in enumerate(self.graph.nodes):
            x = index % self.graph.width * self.node_width + self.gui_width
            y = index // self.graph.width * self.node_width

            pygame.draw.rect(self.surface, (0, 100, 255), (x, y, self.node_width, self.node_width))
            if node == self.graph.startNode:
                pygame.draw.rect(self.surface, (255, 200, 0), (x, y, self.node_width, self.node_width), 2)
            elif node == self.graph.goalNode:
                pygame.draw.rect(self.surface, (255, 0, 0), (x, y, self.node_width, self.node_width), 2)
            elif node in self.graph.bestPath:
                pygame.draw.rect(self.surface, (100, 255, 0), (x, y, self.node_width, self.node_width), 2)

            rotatedImage = pygame.transform.rotate(self.scaledWindArrowImage, 180 - node.wind['direction'])
            self.surface.blit(rotatedImage, (x, y))

            distanceString = str(round(node.distance, 2))
            text = self.font.render(distanceString, False, (0, 0, 0))
            self.surface.blit(text, (x, y))
            
            strengthString = str(node.wind['strength'])
            text = self.font.render(strengthString, False, (255, 255, 255))
            textX = x + self.node_width / 2 - self.font.size(strengthString)[0] / 2
            textY = y + self.node_width / 2 - self.font.size(strengthString)[1] / 2
            self.surface.blit(text, (textX, textY))
