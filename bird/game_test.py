import pygame

import constants
from birds import Bird
from pipe import pipe
import background



pygame.init()
screen = pygame.display.set_mode([constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT])
pygame.display.set_caption("bird_test")

done = False

clock = pygame.time.Clock()

#pipe_game = pipe()
bird = Bird()
sprite_list = pygame.sprite.Group()
sprite_list.add(bird)
level_list = []
level_list.append(background.Level_day(bird))

current_level_no = 0
current_level = level_list[current_level_no]

active_sprite_list = pygame.sprite.Group()
#player.level = current_level

bird.rect.x = 0
bird.rect.y = (constants.SCREEN_HEIGHT - bird.rect.height)//2
active_sprite_list.add(bird)
#active_spr ite_list.add(pipe_game)
# print_di ff = pygame.constants.USEREVENT + 1
# pygame.time.set_timer(print_diff,1000)
gameover = False

#GAMEOVER



while not done:
    # --- Event Pro cessing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if not gameover and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                bird.jump()
        if gameover and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameover = False
                current_level.platform_list.empty()
                current_level.add_pipe()
                current_level.score_list.empty()
                current_level.score = 0

    # Update items in the level
    if not gameover:
        active_sprite_list.update()
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if bird.rect.right >= 100:
            diff = bird.rect.right - 100
            bird.rect.right = 100
            current_level.shift_world(-diff)

        check_hit = pygame.sprite.spritecollide(bird,current_level.platform_list,False)
        for hit in check_hit:
            gameover = True
        # If the player gets near the left side, shift the world right (+x)

        # # If the player gets to the end of the level, go to the next level
        # current_position = player.rect.x + current_level.world_shift
        # if current_position < current_level.level_limit:
        #     player.rect.x = 120
        #     if current_level_no < len(level_list) - 1:
        #         current_level_no += 1
        #         current_level = level_list[current_level_no]
        #         player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
    else:
        current_level.gameover()
        current_level.draw(screen)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down
pygame.quit()
