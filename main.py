import pygame
import random

# Initialize Pygame
pygame.init()


# Set the window size
size = (800, 600)

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)


# --- Set the ball variables ---
ball_pos = [random.randint(100, size[0] - 100), 50]
ball_radius = 10
ball_vel = [random.randint(-5, 5), 5]

# --- Set the paddle variables ---
paddle_width = 100
paddle_height = 10
paddle_pos = [(size[0] - paddle_width) // 2, size[1] - 2 * paddle_height]
paddle_vel = 0





# Create the screen
screen = pygame.display.set_mode(size)

# Set the window title
pygame.display.set_caption("Pinball")

# Set the font
font = pygame.font.Font(None, 36)

# Set the ball radius and speed
ball_radius = 10
ball_speed = 10

# Set the paddle dimensions and speed
paddle_width = 100
paddle_height = 10
paddle_speed = 10

# Initialize the ball position and velocity
ball_pos = [random.randint(ball_radius, size[0] - ball_radius), size[1] // 2]
ball_vel = [random.randint(-5, 5), random.randint(-5, 5)]

# Initialize the paddle position
paddle_pos = [(size[0] - paddle_width) // 2, size[1] - paddle_height * 2]

# Initialize the score and timer
score = 0
time_remaining = 60

# Set the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # --- Event processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # --- Update the ball position ---
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # --- Handle the ball bouncing off the walls ---
    if ball_pos[0] <= ball_radius or ball_pos[0] >= size[0] - ball_radius:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] <= ball_radius:
        ball_vel[1] = -ball_vel[1]
    
    # --- Handle the ball bouncing off the paddle ---
    if ball_pos[1] >= size[1] - ball_radius - paddle_height and ball_pos[0] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[0] + paddle_width:
        ball_vel[1] = -ball_vel[1]
        score += 1
    
    # --- Handle the paddle movement ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_pos[0] < size[0] - paddle_width:
        paddle_pos[0] += paddle_speed
    
        # --- Handle the timer ---
    time_remaining -= 1 / 60
    if time_remaining <= 0:
        time_remaining = 0
        game_over_font = pygame.font.Font(None, 72)
        game_over_text = game_over_font.render("Game Over", True, RED)
        screen.blit(game_over_text, ((size[0] - game_over_text.get_width()) // 2, (size[1] - game_over_text.get_height()) // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        exit()
    
    # --- Clear the screen ---
    screen.fill(WHITE)
    
    # --- Draw the ball ---
    colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, PINK]
    ball_color = random.choice(colors)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    
    # --- Draw the paddle ---
    pygame.draw.rect(screen, BLACK, (paddle_pos[0], paddle_pos[1], paddle_width, paddle_height))
    
    # --- Draw the score and timer ---
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))
    time_text = font.render("Time: " + str(int(time_remaining)), True, BLACK)
    screen.blit(time_text, (size[0] - time_text.get_width() - 10, 10))
    
    # --- Update the screen ---
    pygame.display.update()
    
        # --- Set the game's frame rate ---
    clock.tick(60)
    
    # --- Handle user input ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_vel = -5
            elif event.key == pygame.K_RIGHT:
                paddle_vel = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_vel = 0
    
    # --- Update the position of the paddle ---
    paddle_pos[0] += paddle_vel
    if paddle_pos[0] < 0:
        paddle_pos[0] = 0
    elif paddle_pos[0] > size[0] - paddle_width:
        paddle_pos[0] = size[0] - paddle_width
    
    # --- Check for collision between the ball and the paddle ---
    if ball_pos[1] + ball_radius >= paddle_pos[1] and ball_pos[1] + ball_radius <= paddle_pos[1] + paddle_height and ball_pos[0] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[0] + paddle_width:
        score += 1
        ball_vel[1] = -ball_vel[1]
    
    # --- Update the position of the ball ---
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # --- Check for collision between the ball and the walls ---
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= size[0]:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] - ball_radius <= 0:
        ball_vel[1] = -ball_vel[1]
    
    # --- Check if the ball has gone out of bounds ---
    if ball_pos[1] - ball_radius >= size[1]:
        game_over_font = pygame.font.Font(None, 72)
        game_over_text = game_over_font.render("Game Over", True, BLACK)
        screen.blit(game_over_text, ((size[0] - game_over_text.get_width()) // 2, (size[1] - game_over_text.get_height()) // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        exit()


