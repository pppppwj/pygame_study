import pygame
import constants
background = (288,512)
birds = (34,24)
GO = (192,42)

def Get_Image(pic_size,filename):

    image = pygame.Surface([pic_size[0],pic_size[1]])
    load_image = pygame.image.load(filename).convert_alpha()
    image.blit(load_image,(0,0),(0,0,pic_size[0],pic_size[1]))
    image.set_colorkey(constants.BLACK)
    return image