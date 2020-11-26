import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import math


def createGUI(graph):
    FPS = 50
    windowHeight = 650
    windowWidth = round((graph.width / graph.height) * windowHeight)
    boxWidth = windowWidth // graph.width

    pygame.init()
    display_surface = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Sailing')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, round(boxWidth / 2.5))

    windArrow = pygame.image.load('assets/arrow.png')
    windArrow = pygame.transform.scale(windArrow, (boxWidth, boxWidth))

    while True:
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // boxWidth
                column = event.pos[0] // boxWidth
                if pressed[pygame.K_s]:
                    graph.setStart((column, row))
                if pressed[pygame.K_g]:
                    graph.setGoal((column, row))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if pressed[pygame.K_H] && pressed[pygame.K_U]
                    graph.generateRandom(width, height)

        renderGraph(graph, display_surface, windArrow, font, boxWidth)
        pygame.display.update()
        clock.tick(FPS)

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
