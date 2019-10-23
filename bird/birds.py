import pygame
import constants
#from get_image import Get_Image
import get_image

class Bird(pygame.sprite.Sprite):
    #speed
    change_x = 3
    change_y = 0

    #fly action
    fly_frames_up=[]
    fly_frames_down=[]

    #direction
    direction = "DOWN"
    #level = None

    def __init__(self):
        super().__init__()
        image = get_image.Get_Image(get_image.birds,"./sprites/yellowbird-upflap.png")
        self.fly_frames_up.append(image)

        image = get_image.Get_Image(get_image.birds,"./sprites/yellowbird-midflap.png")
        self.fly_frames_up.append(image)
        self.fly_frames_down.append(image)

        image = get_image.Get_Image(get_image.birds,"./sprites/yellowbird-downflap.png")
        self.fly_frames_up.append(image)

        #init start
        self.image = self.fly_frames_down[0]
        self.rect = self.image.get_rect()

    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        pos = self.rect.y

        if self.direction == "UP":
            frame = (pos // 30) % len(self.fly_frames_up)
            self.image = self.fly_frames_up[frame]
        else:
            self.image = self.fly_frames_down[0]

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 0.5
        else:
            self.change_y += .15

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
            self.change_y -= 4

