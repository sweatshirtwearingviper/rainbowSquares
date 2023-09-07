import pygame
from rainbowsquare import RainbowSquare

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('rainbowSquare')
clock = pygame.time.Clock()

square = RainbowSquare()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    square.collision(pygame.mouse.get_pos())

    #rygibv
    square.rect.left += 1

    screen.blit(square.surf,square.rect)
    pygame.display.update()

    clock.tick(60)