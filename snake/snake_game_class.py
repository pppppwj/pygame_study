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
        self.rect.x = random.randrange(0, n)
        self.rect.y = random.randrange(0, m)

    def update(self):
        #self.rect.x += x_change
        #self.rect.y += y_change

        if self.rect.x<0 or self.rect.x>screen_width:
            self.rect.x = self.rect.x % screen_width

        if self.rect.y<0 or self.rect.y>screen_height:
            self.rect.y = self.rect.y % screen_height


class Game(object):
    #sprite list
    target_list = None
    snake_sprites_list = None
    snake = None
    target = None
    game_over = False
    x_change = None
    y_change = None

    def __init__(self):
        self.game_over = False
        self.target_list =  pygame.sprite.Group()
        self.snake_sprites_list = pygame.sprite.Group()
        self.snake=[]
        self.x_change = 0
        self.y_change = (grid_margin + grid_height)

        x = random.randrange(0, n)
        y = random.randrange(0, m)
        head = unit(x * (grid_margin + grid_width), y * (grid_height + grid_margin))
        self.snake.append(head)
        self.snake_sprites_list.add(head)

        x_target = random.randrange(0, n)
        y_target = random.randrange(0, m)

        self.target = unit(x_target * (grid_margin + grid_width), y_target * (grid_height + grid_margin))
        self.target_list.add(self.target)

        for i in range(4):
            y -= 1
            body = unit(x * (grid_margin + grid_width), y * (grid_height + grid_margin))
            self.snake.append(body)
            self.snake_sprites_list.add(body)

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.x_change = -(grid_width + grid_margin)
                    self.y_change = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.x_change = (grid_width + grid_margin)
                    self.y_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.y_change = -(grid_height + grid_margin)
                    self.x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.y_change = (grid_height + grid_margin)
                    self.x_change = 0
                if event.key == pygame.K_ESCAPE:
                    self.game_over = True

        return False

    def run_logic(self):
        if not self.game_over:
            tail = self.snake.pop()
            self.snake_sprites_list.remove(tail)

            new_head = unit(self.snake[0].rect.x + self.x_change, self.snake[0].rect.y + self.y_change)
            self.snake.insert(0, new_head)
            self.snake_sprites_list.add(new_head)

            blocks = pygame.sprite.spritecollide(self.target, self.snake_sprites_list, False)
            for block in blocks:
                new_tail = unit(self.snake[-1].rect.x - self.x_change, self.snake[-1].rect.y - self.y_change)
                self.snake.append(new_tail)
                self.snake_sprites_list.add(new_tail)
                self.target.reset_pos()

            self.snake_sprites_list.update()

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(BLACK)
        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over", True, GREEN)
            center_x = (screen_width // 2) - (text.get_width() // 2)
            center_y = (screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.snake_sprites_list.draw(screen)
            self.target_list.draw(screen)
        pygame.display.flip()

def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()

    size = [screen_width, screen_height]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("snake")
    pygame.mouse.set_visible(False)

    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    # Main game loop
    while not done:

        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(30)

    # Close window and exit
    pygame.quit()

# Call the main function, start up the game
if __name__ == "__main__":
    main()
