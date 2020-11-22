import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import math


def createGUI(graph):
    FPS = 50
    windowWidth = 600
    windowHeight = (graph.height // graph.width) * windowWidth
    boxWidth = windowWidth // graph.width

    pygame.init()
    display_surface = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Sailing')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, boxWidth // 3)

    windArrow = pygame.image.load('assets/arrow.png')
    windArrow = pygame.transform.scale(windArrow, (boxWidth, boxWidth))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // boxWidth
                column = event.pos[0] // boxWidth
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_s]:
                    graph.setStart((column, row))
                if pressed[pygame.K_g]:
                    graph.setGoal((column, row))
        renderGraph(graph, display_surface, windArrow, font, boxWidth)
        pygame.display.update()
        clock.tick(FPS)

def renderGraph(graph, surface, image, font, width):
    for index, node in enumerate(graph.nodes):
        x = index % graph.width * width
        y = index // graph.width * width

        pygame.draw.rect(surface, (0, 100, 255), (x, y, width, width))
        if node == graph.startNode:
            pygame.draw.rect(surface, (255, 200, 0), (x, y, width, width), 10)
        elif node == graph.goalNode:
            pygame.draw.rect(surface, (255, 0, 0), (x, y, width, width), 10)
        elif node in graph.bestPath:
            pygame.draw.rect(surface, (100, 255, 0), (x, y, width, width), 10)

        rotatedImage = pygame.transform.rotate(image, 180 - node.wind['direction'])
        surface.blit(rotatedImage, (x, y))

        textString = str(node.wind['strength'])
        text = font.render(textString, False, (255, 255, 255))
        textX = x + width / 2 - font.size(textString)[0] / 2
        textY = y + width / 2 - font.size(textString)[1] / 2
        surface.blit(text, (textX, textY))
