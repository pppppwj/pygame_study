import pygame
from spritesheet import SpriteSheet

class item(pygame.sprite.Sprite):

    def __init__(self,x_pos,y_pos,x,y,width,height,sheetname):
        super().__init__()
        items_sheet = SpriteSheet(sheetname)
        self.image = items_sheet.get_image(x,y,width,height)

        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class items(object):
    items_list = None
    items_sheet = None

    def __init__(self,sheetname):
        self.items_sheet = sheetname
        self.items_list = pygame.sprite.Group()

    def add(self,x_pos,y_pos,x,y,width,height):
        item_image = self.items_list.add(item(x_pos,y_pos,x,y,width,height,self.items_sheet))










