import pygame
from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    # speed
    change_x = 0
    change_y = 0

    #walk action
    walking_frames_l=[]
    walking_frames_r = []

    #direction
    direction = "R"

    def __init__(self):
        super().__init__()
        walk_sheet = SpriteSheet("p3_spritesheet.png")
        #walk 01
        image = walk_sheet.get_image(0,0,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 02
        image = walk_sheet.get_image(73,0,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 03
        image = walk_sheet.get_image(146,0,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 04
        image = walk_sheet.get_image(0,98,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 05
        image = walk_sheet.get_image(73,98,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 06
        image = walk_sheet.get_image(146,98,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 07
        image = walk_sheet.get_image(219,0,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 08
        image = walk_sheet.get_image(292,0,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 09
        image = walk_sheet.get_image(219,98,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 10
        image = walk_sheet.get_image(365,0,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #walk 11
        image = walk_sheet.get_image(292,98,72,97)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #init start
        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()

    def update(self):

        #move left\right
        self.rect.x += self.change_x
        #pos = self.rect.x + self.level.world_shift
        pos = self.rect.x

        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]


    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
