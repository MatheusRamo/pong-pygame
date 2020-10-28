import pygame

pygame.display.init()
white = (255,255,255)
black = (0,0,0)
screen = pygame.display.set_mode((600,600), 0)
screen.fill(black)

board = pygame.draw.rect(screen, white, ((0,0),(600,600)), 2)

rectLeft = pygame.draw.rect(screen,white , ((20,260),(20,80)))
rectRight = pygame.draw.rect(screen,white , ((560,260),(20,80)))


pygame.display.update()

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False