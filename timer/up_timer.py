import pygame

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
done = False
start = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 100)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONUP:
            start = True
            start_ticks = pygame.time.get_ticks()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = False



    # Set the screen background
    screen.fill(white)
    if(start):
        diffs = (pygame.time.get_ticks() - start_ticks)/1000
        mins = diffs // 60
        secs = diffs % 60

        output_string = "Time left: {0:.0f}:{1:.2f}".format(mins , secs)
        text = font.render(output_string, True, green)
        screen.blit(text, [100, 200])
    else:
        output_string = "Time left: {0:.0f}:{1:.2f}".format(0 , 0)
        text = font.render(output_string, True, green)
        screen.blit(text, [100, 200])

    clock.tick(60)

    pygame.display.flip()

pygame.quit()