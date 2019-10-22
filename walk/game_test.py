import pygame

import constants
from player import Player
import level



pygame.init()
screen = pygame.display.set_mode([constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT])
pygame.display.set_caption("gane_test")

done = False

clock = pygame.time.Clock()


player = Player()
sprite_list = pygame.sprite.Group()
sprite_list.add(player)
level_list = []
level_list.append(level.Level_01(player))

current_level_no = 0
current_level = level_list[current_level_no]

active_sprite_list = pygame.sprite.Group()
player.level = current_level

player.rect.x = 340
player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
active_sprite_list.add(player)
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.go_left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.go_right()
            if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                player.jump()


        if event.type == pygame.KEYUP:
            # if event.key == pygame.K_LEFT and player.change_x < 0 or event.key == pygame.K_a and player.change_x < 0:
            #     player.stop()
            # if event.key == pygame.K_RIGHT and player.change_x > 0 or event.key == pygame.K_d and player.change_x > 0:
            #     player.stop()

            if event.key == pygame.K_LEFT and player.direction == "L" or event.key == pygame.K_a and player.direction == "L":
                player.stop()
            if event.key == pygame.K_RIGHT and player.direction == "R" or event.key == pygame.K_d and player.direction == "R":
                player.stop()

    active_sprite_list.update()

    # Update items in the level
    current_level.update()

    # If the player gets near the right side, shift the world left (-x)
    if player.rect.right >= 500:
        diff = player.rect.right - 500
        player.rect.right = 500
        current_level.shift_world(-diff)

    # If the player gets near the left side, shift the world right (+x)
    if player.rect.left <= 120:
        diff = 120 - player.rect.left
        player.rect.left = 120
        current_level.shift_world(diff)

    # If the player gets to the end of the level, go to the next level
    current_position = player.rect.x + current_level.world_shift
    if current_position < current_level.level_limit:
        player.rect.x = 120
        if current_level_no < len(level_list) - 1:
            current_level_no += 1
            current_level = level_list[current_level_no]
            player.level = current_level

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    current_level.draw(screen)
    active_sprite_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down
pygame.quit()
