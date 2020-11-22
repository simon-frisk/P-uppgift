import pygame
import math


def createGUI(graph, sea_dimensions):
    FPS = 50
    windowWidth = 600
    windowHeight = (sea_dimensions['height'] //
                    sea_dimensions['width']) * windowWidth
    boxWidth = windowWidth // sea_dimensions['width']

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
        for index, node in enumerate(graph.nodes):
            renderNode(node, windArrow, font, display_surface, (
                index % sea_dimensions['width'] * boxWidth,
                index // sea_dimensions['width'] * boxWidth,
                boxWidth,
                boxWidth
            ))
        pygame.display.update()
        clock.tick(FPS)


def renderNode(node, image, font, surface, dimensions):
    pygame.draw.rect(surface, (0, 100, 255), dimensions)

    if node.is_goal:
        pygame.draw.rect(surface, (255, 0, 0), dimensions, 10)
    elif node.distance == 0:
        pygame.draw.rect(surface, (255, 200, 0), dimensions, 10)
    elif node.pathIndex:
        pygame.draw.rect(surface, (100, 255, 0), dimensions, 10)
        pathIndexSurface = font.render(
            str(node.pathIndex), False, (255, 0, 0))
        surface.blit(pathIndexSurface, dimensions)

    rotatedImage = pygame.transform.rotate(image, node.wind['direction'])
    surface.blit(rotatedImage, dimensions)

    textString = str(node.wind['strength'])
    text = font.render(textString, False, (255, 255, 255))
    textX = dimensions[0] + dimensions[2] / 2 - font.size(textString)[0] / 2
    textY = dimensions[1] + dimensions[2] / 2 - font.size(textString)[1] / 2
    surface.blit(text, (textX, textY))
