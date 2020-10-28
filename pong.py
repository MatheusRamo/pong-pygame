import pygame
from random import randint


pygame.display.init()
pygame.font.init()

white = (255,255,255)
black = (0,0,0)
cor = (255, 255, 255)

pygame.display.set_caption("Pong Game")
screen = pygame.display.set_mode((600,600), 0)

# Board
board = pygame.Rect(((0,0),(600,600)))

# Players
rectLeft = pygame.Rect((20,260),(20,80))
rectRight = pygame.Rect((560,260),(20,80))

scoreLeft = 0
scoreRight = 0

# Ball
ball = pygame.Rect((300,300),(20,20))
ball_dx = 1
ball_dy = -1

font = pygame.font.SysFont("Arial", 24, bold=1)

runing = True
while runing:

    text = font.render(f"Player Left: {scoreLeft}  Player Right: {scoreRight}", True, cor)
    screen.fill(black)
    pygame.draw.rect(screen, cor, board, 10)

    pygame.draw.rect(screen, cor, rectLeft)

    pygame.draw.rect(screen, cor, rectRight)

    pygame.draw.rect(screen, white, ball)

    screen.blit(text,[150,20])

    ball.x = ball.x + ball_dx
    ball.y = ball.y + ball_dy

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False


    key = pygame.key.get_pressed()
    # Player Left
    if key[pygame.K_w]:

        if rectLeft.y < 0:
            rectLeft.y = 0
        else:
            rectLeft.y = rectLeft.y - 1

    if key[pygame.K_s]:

        if rectLeft.y > 520:
            rectLeft.y = 520
        else:
            rectLeft.y = rectLeft.y + 1
    
    # Player Right
    if key[pygame.K_UP]:

        if rectRight.y < 0:
            rectRight.y = 0
        else:
            rectRight.y = rectRight.y - 1

    if key[pygame.K_DOWN]:

        if rectRight.y > 520:
            rectRight.y = 520
        else:
            rectRight.y = rectRight.y + 1

    # Board Colision
    if ball.x > 580:
        ball_dx = ball_dx * (-1)
        scoreLeft +=1
        
    if ball.y > 580:
        ball_dy = ball_dy * (-1)
    
    if ball.x < 0:
        ball_dx = ball_dx *(-1)
        scoreRight +=1

    if ball.y < 0:
        ball_dy = ball_dy *(-1)

    # Colision between Players and ball
    if (ball.x < 40 and ball.x > 20) and (ball.y > rectLeft.y and ball.y < rectLeft.y + 80):
        ball.x = 40
        ball_dx = ball_dx * (-1)
        cor = (randint(100, 255), randint(100, 255), randint(100, 255))

    if (ball.x > 540 and ball.x < 560) and (ball.y > rectRight.y and ball.y < rectRight.y + 80):
        ball.x = 540
        ball_dx = ball_dx * (-1)
        cor = (randint(100,255), randint(100, 255), randint(100, 255))



    pygame.display.update()