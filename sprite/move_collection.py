import pygame
import random

#def some color [R,B,G]
GREEN = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

#def size screen
screen_width=700
screen_height=400

#define target
class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.xsp = 0
        self.ysp = 0

    def set_pos(self):
        # width = block.image.get_size()[0]
        # height = block.image.get_size()[1]
        self.rect.x = random.randrange(20, 680)
        self.rect.y = random.randrange(15, 385)
        self.xsp = random.randrange(-3, 3)
        self.ysp = random.randrange(-3, 3)


    def update(self):
        #updata the pos of block
        self.rect.x += self.xsp
        self.rect.y += self.ysp
        # Bounce the spirit if needed
        if self.rect.x >= 675 or self.rect.x <= 0:
            self.xsp = self.xsp * -1
        if self.rect.y >=385 or self.rect.y <= 0:
            self.ysp = self.ysp * -1

#def player
class Player(Block):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

pygame.init()
#set screen
screen = pygame.display.set_mode([screen_width,screen_height])
block_list = pygame.sprite.Group()
for i in range(1):
    block = Block(BLACK, 20, 15)
    block.set_pos()
    block_list.add(block)

player = Player(GREEN,20,15)
score = 0


done = False
clock = pygame.time.Clock()

produce_ball = pygame.constants.USEREVENT + 1
pygame.time.set_timer(produce_ball,1000)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            player.update()
            block_list.update()
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
            for block in blocks_hit_list:
                score += 1
                print(score)


        if event.type == produce_ball:
            block = Block(BLACK, 20, 15)
            block.set_pos()
            block_list.add(block)

    screen.fill(WHITE)
    player.update()
    block_list.update()
    block_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()



