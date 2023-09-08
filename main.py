import pygame
from rainbowsquare import RainbowSquare

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('rainbowSquare')
clock = pygame.time.Clock()

squares = []

count = 0
for y in range(4):
    x = 0
    for x in range(6):
        squares.append(RainbowSquare())
        squares[count].rect.x = 100 * x
        squares[count].rect.y = 100 * y
        count += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for square in squares:
        square.collision(pygame.mouse.get_pos())
        screen.blit(square.surf,square.rect)
    pygame.display.update()

    clock.tick(60)