import pygame

import constants
import get_image

pipe_weight = 52
class pipe(pygame.sprite.Sprite):
    def __init__(self,xpos,len,dir):
        super().__init__()
        if(dir=="up"):
            self.image = get_image.Get_Image((pipe_weight,len), "./sprites/pipe-green.png")
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect = self.image.get_rect()
            self.rect.x=xpos+320
            self.rect.y=0
        if(dir=="down"):
            self.image = get_image.Get_Image((pipe_weight,len), "./sprites/pipe-green.png")
            self.rect = self.image.get_rect()
            self.rect.x=xpos+320
            self.rect.bottom = 512

class gameover(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = get_image.Get_Image(get_image.GO, "./sprites/gameover.png")
        self.rect = self.image.get_rect()
        self.rect.x= (constants.SCREEN_WIDTH-get_image.GO[0])//2
        self.rect.y=(constants.SCREEN_HEIGHT-get_image.GO[1])//2

class score(pygame.sprite.Sprite):
    def __init__(self,score,pos):
        super().__init__()
        self.image = get_image.Get_Image((16,36), "./sprites/" + str(score) +".png")
        self.rect = self.image.get_rect()
        self.rect.x= 0+16*pos
        self.rect.y=0