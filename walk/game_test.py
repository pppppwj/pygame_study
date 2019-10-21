import pygame

import constants
from spritesheet import SpriteSheet
from player import Player


pygame.init()
screen = pygame.display.set_mode([constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT])
pygame.display.set_caption("gane_test")

done = False

clock = pygame.time.Clock()


player = Player()
sprite_list = pygame.sprite.Group()
sprite_list.add(player)

while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()

    screen.fill(constants.GREEN)
    sprite_list.update()
    sprite_list.draw(screen)
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down
pygame.quit()
