import pygame
import time
import random

# Initialize the pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Display dimensions
WIDTH = 600
HEIGHT = 400

# Snake block size and speed
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Set up display
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up clock to control the speed of the game
clock = pygame.time.Clock()

# Fonts for text display
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Score function
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    display.blit(value, [0, 0])

# Snake function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, GREEN, [x[0], x[1], snake_block, snake_block])

# Message function to display text on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = WIDTH / 2
    y = HEIGHT / 2

    # Initial movement
    x_change = 0
    y_change = 0

    # Snake body list and initial length
    snake_list = []
    length_of_snake = 1

    # Random position for the food
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(BLUE)
            message("You Lost! Press C to Play Again or Q to Quit", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        # Snake movement
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change
        display.fill(BLACK)

        # Draw food
        pygame.draw.rect(display, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        # Snake growing logic
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Run the game
game_loop()
