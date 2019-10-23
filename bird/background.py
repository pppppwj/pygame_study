import pygame
import random
import constants
from pipe import pipe
from pipe import gameover
from pipe import score
class Level():
    platform_list = None
    score=0
    score_list = None
    background = None

    world_shift = 0
    #level_limit = -1000

    def __init__(self,player):
        self.player = player
        self.platform_list = pygame.sprite.Group()
        self.score_list = pygame.sprite.Group()
        self.score_list.add(score(0,0))
        l = random.randrange(200, 300)
        pipe_top = pipe(150,l,"up")
        pipe_down = pipe(150, 400-l, "down")
        self.platform_list.add(pipe_top)
        self.platform_list.add(pipe_down)


    def update(self):
        self.platform_list.update()
        flag = 0
        for pipe in self.platform_list:
            if pipe.rect.right+50 < self.player.rect.left:
                self.platform_list.remove(pipe)
                flag = 1

        if flag:
            self.score += 1
            self.add_pipe()



    def add_pipe(self):
        l = random.randrange(200, 300)
        pipe_top = pipe(self.player.rect.right,l,"up")
        pipe_down = pipe(self.player.rect.right, 400-l, "down")
        self.platform_list.add(pipe_top)
        self.platform_list.add(pipe_down)

        self.score_list.empty()
        scoreDigits = [int(x) for x in list(str(self.score))]
        for i in range(len(scoreDigits)):
            self.score_list.add(score(scoreDigits[i],i))


    def draw(self,screen):
        screen.fill(constants.GREEN)

        screen.blit(self.background, ((self.world_shift // 3) % (-288), 0))
        screen.blit(self.background, ((self.world_shift // 3)% (-288) + 288, 0))
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.score_list.draw(screen)


    def shift_world(self,shift_x):

        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

    def gameover(self):
        self.platform_list.empty()
        self.platform_list.add(gameover())




class Level_day(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("./sprites/background-day.png").convert()
        #self.background.set_colorkey(constants.WHITE)

        # Array with type of platform, and x, y location of the platform.

        #
        # # Go through the array above and add platforms
        # for platform in level:
        #     block = Platform.Platform(platform[0],platform[1],platform[2],"tiles_spritesheet.png")
        #     block.player = self.player
        #     self.platform_list.add(block)



