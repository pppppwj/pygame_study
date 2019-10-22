"""
Module for managing platforms.
"""
import pygame

import constants
import Platform

class Level():
    platform_list = None
    enemy_list = None

    background = None

    world_shift = 0
    level_limit = -1000

    def __init__(self,player):
        self.player = player
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self,screen):
        screen.fill(constants.GREEN)
        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self,shift_x):

        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [500, 500,Platform.GRASS_LEFT]
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform.Platform(platform[0],platform[1],platform[2],"tiles_spritesheet.png")
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = Platform.Moving_Platform(1350,280,Platform.STONE_PLATFORM_MIDDLE,"tiles_spritesheet.png")
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)



