import pygame

y = 0
dir = 1
running = 1
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
linecolor = 255, 0, 0
bgcolor = 0, 0, 0

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill(bgcolor)

    #point1 = (400, y+100)
    #point2 = (400, y)
    #pygame.draw.aaline(screen, linecolor, point1, point2)

    pygame.draw.aaline(screen, linecolor, (0, y), (width-1, y))

    y += dir
    if y == 0 or y == height-1: dir *= -1

    pygame.display.flip()
