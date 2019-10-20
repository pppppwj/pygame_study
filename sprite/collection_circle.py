import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Block(pygame.sprite.Sprite):

    def __init__(self, color, radius):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2*radius, 2*radius])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.radius = radius
        pygame.draw.circle(self.image, RED, [radius,radius],radius)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

player = Block(RED, 1)
all_sprites_list.add(player)
#produce a target
block = Block(WHITE, 20)
#dont let it outside the canvas
block.rect.center = (random.randrange(20,screen_width-20),random.randrange(20,screen_height-20))

block_list.add(block)
all_sprites_list.add(block)


done = False

clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            player.rect.center = (pos[0],pos[1])
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True, collided=pygame.sprite.collide_circle)
            for block in blocks_hit_list:
                score += 1
                print(score)
                block = Block(WHITE, 20)
                block.rect.center = (random.randrange(20, screen_width - 20), random.randrange(20, screen_height - 20))
                block_list.add(block)
                all_sprites_list.add(block)



        screen.fill(WHITE)
        block_list.draw(screen)
        #all_sprites_list.draw(screen)


        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

pygame.quit()
