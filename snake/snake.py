import pygame
import random

#--Globals--

#color RGB
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

#set grid size
grid_width = 10
grid_height = 10
#set grid margin
grid_margin = 2

#screen size m*n
m,n=60,80
screen_width = n*(grid_width+grid_margin)
screen_height = m*(grid_height+grid_margin)

#moving speed
x_change = 0
y_change = (grid_margin+grid_height)

class unit(pygame.sprite.Sprite):
    #def init
    #args location
    def __init__(self,x,y):
        super().__init__()
        #set surface size as unit of grid
        self.image = pygame.Surface([grid_width,grid_height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset_pos(self):
        self.rect.x = random.randrange(0, n)*(grid_margin+grid_width)
        self.rect.y = random.randrange(0, m)*(grid_margin+grid_height)

    def update(self):
        #self.rect.x += x_change
        #self.rect.y += y_change

        if self.rect.x<0 or self.rect.x>screen_width:
            self.rect.x = self.rect.x % screen_width

        if self.rect.y<0 or self.rect.y>screen_height:
            self.rect.y = self.rect.y % screen_height


pygame.init()

screen = pygame.display.set_mode([screen_width,screen_height])

pygame.display.set_caption("Snake")
target_list = pygame.sprite.Group()
snake_sprites_list = pygame.sprite.Group()
snake=[]

x = random.randrange(0, n)
y = random.randrange(0, m)
head = unit(x*(grid_margin+grid_width),y*(grid_height+grid_margin))
snake.append(head)
snake_sprites_list.add(head)


x_target = random.randrange(0, n)
y_target = random.randrange(0, m)

target = unit(x_target*(grid_margin+grid_width),y_target*(grid_height+grid_margin))
target_list.add(target)


for i in range(4):
    y-=1
    body = unit(x*(grid_margin+grid_width),y*(grid_height+grid_margin))
    snake.append(body)
    snake_sprites_list.add(body)


clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -(grid_width + grid_margin)
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (grid_width + grid_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                y_change = -(grid_height + grid_margin)
                x_change = 0
            if event.key == pygame.K_DOWN:
                y_change = (grid_height + grid_margin)
                x_change = 0

    screen.fill(BLACK)
    tail = snake.pop()
    snake_sprites_list.remove(tail)

    new_head=unit(snake[0].rect.x+x_change,snake[0].rect.y+y_change)
    snake.insert(0,new_head)
    snake_sprites_list.add(new_head)

    blocks = pygame.sprite.spritecollide(target, snake_sprites_list, False)
    for block in blocks:
        new_tail = unit(snake[-1].rect.x - x_change, snake[-1].rect.y - y_change)
        snake.append(new_tail)
        snake_sprites_list.add(new_tail)
        target.reset_pos()


    snake_sprites_list.update()
    snake_sprites_list.draw(screen)
    #target.update()
    target_list.draw(screen)
    pygame.display.flip()

    # Pause
    clock.tick(10)

pygame.quit()

