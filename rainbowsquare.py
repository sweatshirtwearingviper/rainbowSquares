import pygame

class RainbowSquare:
    
    def __init__(self):
        self.surf = pygame.Surface((100,100))
        self.surf.fill('red')
        self.rect = pygame.Rect(self.surf.get_rect())
        self.mode = True
        self.increase_index = 1
        self.decrease_index = 0
        self.speed = 20
        self.rgb = [255, 0, 0]

    def collision(self, mouse_pos):
        '''
        Mode determines which index is active
        True, color on increase index is filled to 255, then increase index is incremented
        False, color on decrease index is drained to 0, then decrease index is decremented
        '''
        if self.rect.collidepoint(mouse_pos):
            if self.mode:
                self.rgb[self.increase_index] += 1 * self.speed
                if self.rgb[self.increase_index] >= 255:
                    self.rgb[self.increase_index] = 255
                    self.mode = False
                    self.increase_index += 1
                    if self.increase_index > 2:
                        self.increase_index = 0
            else:
                self.rgb[self.decrease_index] -= 1 * self.speed
                if self.rgb[self.decrease_index] <= 0:
                    self.rgb[self.decrease_index] = 0
                    self.mode = True
                    self.decrease_index += 1
                    if self.decrease_index > 2:
                        self.decrease_index = 0

            self.surf.fill(self.rgb)
    '''
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
    '''