import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import pygame_gui
import math


def createGUI(graph):
    FPS = 50
    guiWidth = 250
    seaHeight = 650
    seaWidth = round((graph.width / graph.height) * seaHeight)
    nodeWidth = seaWidth // graph.width
    screenDimensions = (seaWidth + guiWidth, seaHeight)

    pygame.init()
    display_surface = pygame.display.set_mode(screenDimensions)
    pygame.display.set_caption('Sailing')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, round(nodeWidth / 2.5))
    uiManager = pygame_gui.UIManager(screenDimensions)

    windArrow = pygame.image.load('assets/arrow.png')
    windArrow = pygame.transform.scale(windArrow, (nodeWidth, nodeWidth))

    newGraphButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((seaWidth + 10, 10), (guiWidth - 20, 40)),
        text='Generate new graph',
        manager=uiManager
    )

    while True:
        time_delta = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // nodeWidth
                column = event.pos[0] // nodeWidth
                if pressed[pygame.K_s]:
                    graph.setStart((column, row))
                if pressed[pygame.K_g]:
                    graph.setGoal((column, row))
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                 if event.ui_element == newGraphButton:
                    graph.generateRandom(graph.width, graph.height)
            uiManager.process_events(event)

        renderGraph(graph, display_surface, windArrow, font, nodeWidth)
        uiManager.update(time_delta)
        uiManager.draw_ui(display_surface)
        pygame.display.update()

def renderGraph(graph, surface, image, font, width):
    for index, node in enumerate(graph.nodes):
        x = index % graph.width * width
        y = index // graph.width * width

        pygame.draw.rect(surface, (0, 100, 255), (x, y, width, width))
        if node == graph.startNode:
            pygame.draw.rect(surface, (255, 200, 0), (x, y, width, width), 2)
        elif node == graph.goalNode:
            pygame.draw.rect(surface, (255, 0, 0), (x, y, width, width), 2)
        elif node in graph.bestPath:
            pygame.draw.rect(surface, (100, 255, 0), (x, y, width, width), 2)
        rotatedImage = pygame.transform.rotate(image, 180 - node.wind['direction'])
        surface.blit(rotatedImage, (x, y))

        distanceString = str(round(node.distance, 2))
        text = font.render(distanceString, False, (0, 0, 0))
        surface.blit(text, (x, y))
        
        strengthString = str(node.wind['strength'])
        text = font.render(strengthString, False, (255, 255, 255))
        textX = x + width / 2 - font.size(strengthString)[0] / 2
        textY = y + width / 2 - font.size(strengthString)[1] / 2
        surface.blit(text, (textX, textY))
