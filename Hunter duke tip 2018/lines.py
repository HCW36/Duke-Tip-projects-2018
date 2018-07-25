import pygame

screen = pygame.display.set_mode((640,480))
running = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame. QUIT:
        running = 0

    green= 0, 255, 0
    point1 = 0, 0
    point2 = 640, 480
    pygame.draw.aaline(screen, green, point1, point2)
    pygame.display.flip()

    white= 255, 255, 255
    point1 = 0, 480
    point2 = 640, 0
    pygame.draw.aaline(screen, white, point1, point2)
    pygame.display.flip()

    red = 255, 0, 0
    point1 = 320, 480
    point2 = 320, 0
    pygame.draw.aaline(screen, red, point1, point2)
    pygame.display.flip()

    yellow = 255, 255, 0
    point1 = 0, 240
    point2 = 640, 240
    pygame.draw.aaline(screen, yellow, point1, point2)
    pygame.display.flip()
