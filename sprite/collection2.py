#pppppwj
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
font = pygame.font.Font(None,80)
gameover = False

#def produce ball
produce_ball = pygame.constants.USEREVENT + 1
pygame.time.set_timer(produce_ball,400)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            start_ticks = pygame.time.get_ticks()
            pos = pygame.mouse.get_pos()
            player.rect.x = pos[0]
            player.rect.y = pos[1]
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
            for block in blocks_hit_list:
                score += 1
                print(score)
        if event.type == produce_ball and not gameover:
            block = Block(BLACK, 20, 15)
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_height)
            block_list.add(block)


        if(len(block_list)>=10 or score>10):
            gameover = True

        screen.fill(WHITE)
        if not gameover:
            block_list.draw(screen)
        elif(score > 10):
            output_string = "WELL DONE!"
            text = font.render(output_string, True, RED)
            screen.blit(text, [200, 200])
        else:
            output_string = "GAME OVER"
            text = font.render(output_string, True, RED)
            screen.blit(text, [200, 200])

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

pygame.quit()
