import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('rainbowSquare')
surf = pygame.Surface((100,100))
surf.fill('red')
rect = pygame.Rect(surf.get_rect())
clock = pygame.time.Clock()

mode = 0
speed = 20
r = 255
g = 0
b = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if rect.collidepoint(pygame.mouse.get_pos()):
        match mode:
            # 255 0 0
            case 0:
                g += 1 * speed
                if g >= 255:
                    g = 255
                    mode = 1
            # 255 255 0
            case 1:
                r -= 1 * speed
                if r <= 0:
                    r = 0
                    mode = 2
            # 0 255 0
            case 2:
                b += 1 * speed
                if b >= 255:
                    b = 255
                    mode = 3
            # 0 255 255
            case 3:
                g -= 1 * speed
                if g <= 0:
                    g = 0
                    mode = 4
            # 0 0 255
            case 4:
                r += 1 * speed
                if r >= 255:
                    r = 255
                    mode = 5
            # 255 0 255
            case 5:
                b -= 1 * speed
                if b <= 0:
                    b = 0
                    mode = 0

        #rygibv

        surf.fill((r,g,b))

    screen.blit(surf,(0,0))
    pygame.display.update()

    clock.tick(60)