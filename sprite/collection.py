import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

player = Block(RED, 20, 15)

#produce a target
block = Block(BLACK, 20, 15)
#dont let it outside the canvas
block.rect.x = random.randrange(20,screen_width-20)
block.rect.y = random.randrange(15,screen_height-15)
block_list.add(block)


done = False

clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            player.rect.x = pos[0]
            player.rect.y = pos[1]
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
            for block in blocks_hit_list:
                score += 1
                print(score)
                block = Block(BLACK, 20, 15)
                block.rect.x = random.randrange(screen_width)
                block.rect.y = random.randrange(screen_height)
                block_list.add(block)



        screen.fill(WHITE)
        block_list.draw(screen)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

pygame.quit()
