import pygame


def createGUI(graph, sea_dimensions):
    FPS = 50

    windowWidth = 600
    windowHeight = (sea_dimensions['height'] //
                    sea_dimensions['width']) * windowWidth

    boxWidth = windowWidth / sea_dimensions['width']

    pygame.init()
    display_surface = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Sailing')
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 90)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for index, node in enumerate(graph.nodes):
            dimensions = (
                index % sea_dimensions['width'] * boxWidth,
                index // sea_dimensions['width'] * boxWidth,
                boxWidth,
                boxWidth
            )

            pygame.draw.rect(display_surface, (0, 0, 255), dimensions)
            text = font.render(str(node.distance),
                               False, (100, 255, 100))
            display_surface.blit(text, dimensions)

        pygame.display.update()
        clock.tick(FPS)
