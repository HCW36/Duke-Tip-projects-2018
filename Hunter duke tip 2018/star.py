import pygame

screen = pygame.display.set_mode((640,480))
running = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame. QUIT:
        running = 0

    Yellow = 255, 255, 0
    point1 = 360, 0
    point2 = 550,480
    pygame.draw.aaline(screen, Yellow, point1, point2)
    pygame.display.flip()

    Yellow = 255, 255, 0
    point1 = 360, 0
    point2 = 150, 480
    pygame.draw.aaline(screen, Yellow, point1, point2)
    pygame.display.flip()

    Yellow = 255, 255, 0
    point1 = 150, 480
    point2 = 640, 150
    pygame.draw.aaline(screen, Yellow, point1, point2)
    pygame.display.flip()

    Yellow = 255, 255, 0
    point1 = 0, 150
    point2 = 640, 150
    pygame.draw.aaline(screen, Yellow, point1, point2)
    pygame.display.flip()

    Yellow = 255, 255, 0
    point1 = 0, 0
    point2 = 400, 150
    pygame.draw.aaline(screen, Yellow, point1, point2)
    pygame.display.flip()

