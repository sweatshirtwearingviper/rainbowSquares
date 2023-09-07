import pygame

class RainbowSquare:
    
    def __init__(self):
        self.surf = pygame.Surface((100,100))
        self.surf.fill('red')
        self.rect = pygame.Rect(self.surf.get_rect())
        self.mode = 0
        self.speed = 20
        self.r = 255
        self.g = 0
        self.b = 0

    def collision(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            match self.mode:
                # 255 0 0
                case 0:
                    self.g += 1 * self.speed
                    if self.g >= 255:
                        self.g = 255
                        self.mode= 1
                # 255 255 0
                case 1:
                    self.r -= 1 * self.speed
                    if self.r <= 0:
                        self.r = 0
                        self.mode= 2
                # 0 255 0
                case 2:
                    self.b+= 1 * self.speed
                    if self.b >= 255:
                        self.b = 255
                        self.mode= 3
                # 0 255 255
                case 3:
                    self.g -= 1 * self.speed
                    if self.g <= 0:
                        self.g = 0
                        self.mode= 4
                # 0 0 255
                case 4:
                    self.r += 1 * self.speed
                    if self.r >= 255:
                        self.r = 255
                        self.mode= 5
                # 255 0 255
                case 5:
                    self.b-= 1 * self.speed
                    if self.b <= 0:
                        self.b = 0
                        self.mode= 0
            
            self.surf.fill((self.r, self.g, self.b))

        #rygibv