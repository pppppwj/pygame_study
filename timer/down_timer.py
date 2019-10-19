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

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 100)

start_ticks = 0
# set time
start_time = 90

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONUP:
            start_ticks = pygame.time.get_ticks()


    # Set the screen background
    screen.fill(white)
    if(start_ticks!=0):
        diff = start_time - (pygame.time.get_ticks() - start_ticks)/1000
        if diff < 0:
            diff = 0


    # Divide by 60 to get total minutes
        minutes = diff // 60

    # Use modulus (remainder) to get seconds
        seconds = diff % 60

    # Use python string formatting to format in leading zeros
        output_string = "Time left: {0:.0f}:{1:.0f}".format(minutes, seconds)

    # Blit to the screen
        text = font.render(output_string, True, black)
    #[700, 500]
        screen.blit(text, [100, 200])

    else:
        output_string = "Time left: {0:.0f}:{1:02}".format(start_time//60, start_time%60)
        text = font.render(output_string, True, green)
        screen.blit(text, [100, 200])
    # Limit to 20 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
