import pygame
import sys
import random


def intro():
    # INITIALIZE MODULES
    pygame.init()

    # WINDOW SIZE
    # Length x Breadth of our window
    window = pygame.display.set_mode((300, 200))

    # WINDOW NAME
    pygame.display.set_caption('Flappy Bird - Main Menu')

    # BACKGROUND
    # Set bg (keep it on same folder and same size as window)
    background_image = pygame.image.load('brown_background.jpg')

    # TEXTS
    def display_texts():
        font = pygame.font.Font('freesansbold.ttf', 25)
        disp_msg = font.render("Welcome !!", True, (255, 255, 255))
        disp_msg_rect = disp_msg.get_rect()
        disp_msg_rect.center = (150, 20)
        window.blit(disp_msg, disp_msg_rect)

        font = pygame.font.Font('freesansbold.ttf', 15)
        start_msg = font.render("Start Game", True, (0, 255, 0))
        start_msg_rect = start_msg.get_rect()
        start_msg_rect.center = (150, 80)
        window.blit(start_msg, start_msg_rect)

        font = pygame.font.Font('freesansbold.ttf', 15)
        quit_msg = font.render("Quit Game", True, (255, 0, 0))
        quit_msg_rect = quit_msg.get_rect()
        quit_msg_rect.center = (150, 120)
        window.blit(quit_msg, quit_msg_rect)

        font = pygame.font.Font('freesansbold.ttf', 15)
        credits_msg = font.render("Credits : Mayank Pandit", True, (0, 0, 255))
        credits_msg_rect = credits_msg.get_rect()
        credits_msg_rect.center = (150, 180)
        window.blit(credits_msg, credits_msg_rect)

    # ARROW
    # Set img (keep it on same folder and small size as compared to window)
    arrow_image = pygame.image.load('arrow_image.png')
    arrow_pos_x = 40
    arrow_pos_y = 55
    arrow_change_pos_y = 0

    value = True

    running = True
    while running:
        window.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            arrow_change_pos_y = 40
            value = False

        if key[pygame.K_UP]:
            arrow_change_pos_y = -40
            value = True

        arrow_pos_y += arrow_change_pos_y

        if arrow_pos_y <= 55:
            arrow_pos_y = 55

        if arrow_pos_y >= 95:
            arrow_pos_y = 95

        window.blit(arrow_image, (arrow_pos_x, arrow_pos_y))
        display_texts()

        if key[pygame.K_RETURN] and value:
            pygame.quit()
            game_loop()

        if key[pygame.K_RETURN] and not value:
            pygame.quit()
            sys.exit()

        pygame.display.update()

    pygame.quit()
    sys.exit()


def game_loop():
    # INITIALIZE MODULES
    pygame.init()

    # WINDOW SIZE
    # Length x Breadth of our window
    window = pygame.display.set_mode((600, 500))

    # WINDOW NAME
    pygame.display.set_caption('Flappy Bird - Game')

    # BACKGROUND
    # Set bg (keep it on same folder and same size as window)
    background_image = pygame.image.load('background_image.jpg')

    # BIRD
    # Set img (keep it on same folder and small size as compared to window)
    bird_image = pygame.image.load('bird_image.png')
    bird_pos_x = 50
    bird_pos_y = 100
    bird_change_pos_y = 0

    # OBSTACLE
    obstacle_width = 50
    # Randomly change values of these rectangle b/w these values
    obstacle_height = random.randint(50, 260)
    # rgb value
    obstacle_colour = (102, 51, 0)
    obstacle_gap = 100
    obstacle_pos_x = 450
    top_obstacle_pos_y = 0
    obstacle_change_pos_x = -0.1

    # SCORE
    score = 0
    score_font = pygame.font.Font('freesansbold.ttf', 20)


    def display_bird():
        window.blit(bird_image, (bird_pos_x, bird_pos_y))


    def display_obstacle():
        pygame.draw.rect(window, obstacle_colour, (obstacle_pos_x, top_obstacle_pos_y, obstacle_width, obstacle_height))
        # Cuz height will change after each run
        bottom_obstacle_start_point = obstacle_height + obstacle_gap
        # Fill bottom height till 412px (grass of bg)
        bottom_obstacle_height = (412 - bottom_obstacle_start_point)
        pygame.draw.rect(window, obstacle_colour, (obstacle_pos_x, bottom_obstacle_start_point, obstacle_width, bottom_obstacle_height))
        return bottom_obstacle_start_point


    def detect_collision(bottom_obstacle_height):
        # Use this condition when obstacle is b/w 50 to 150 (b/w my bird's width)
        if bird_pos_x <= int(obstacle_pos_x) <= bird_pos_x + 50:
            # Edge to edge bird detection as pic has some extra borders
            if int(bird_pos_y + 10) <= int(obstacle_height) or int(bird_pos_y) >= int(bottom_obstacle_height - 38):
                return True
        return False


    def display_score():
        disp_score = score_font.render("Score : " + str(score), True, (255, 255, 255))
        window.blit(disp_score, (5, 5))


    running = True
    while running:
        # Put our image on canvas at (0, 0) of window so it fulls up our screen
        window.blit(background_image, (0, 0))

        # Check for a event (action taken by user. Eg - pressing keyboard, clicking buttons, etc) to happen
        # We will say if user clicks "X" button (cancel), run it
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Bird moves only vertically (i.e. - y value)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # If you press space bar, it'll move up by 0.14
                bird_change_pos_y = -0.14

            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                # If you release space bar, it'll move down automatically by 0.07 (half of 0.14 for smoothness)
                bird_change_pos_y = 0.07

        # Moving bird up and down
        bird_pos_y += bird_change_pos_y

        # If bird goes way up of window, keep bird at top of window rather than making it gone forever
        if bird_pos_y <= 0:
            bird_pos_y = 0
        # If bird goes way down of window, keep bird at floor of background rather than making it gone forever
        if bird_pos_y >= 367:
            bird_pos_y = 367

        # Obstacle moves left by 0.1
        obstacle_pos_x += obstacle_change_pos_x

        # Display the bird on window
        display_bird()
        # Display the obstacles on window & store return value in height
        height = display_obstacle()
        # Display score on window
        display_score()

        # Use the above parameter to check
        check_for_collison = detect_collision(height)
        if check_for_collison:
            pygame.quit()
            intro()

        # Obstacle goes beyond screen; for smooth flow
        if obstacle_pos_x <= -20:
            obstacle_pos_x = 600
            # Re-arrange heights
            obstacle_height = random.randint(50, 260)
            # Adding score
            score += 1

        # Update the display
        pygame.display.update()

    # QUIT
    pygame.quit()
    sys.exit()


intro()