# Importing important stuff
import pygame
import os
# font library
pygame.font.init()
# for sounds
pygame.mixer.init()

# define width and height variables
WIDTH, HEIGHT = 900, 500

#Set window parameters using above variables
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# this sets the window title
pygame.display.set_caption("Sebastians First pyGame!")

# Setting colors as constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# draws rectangle for the "border" down the middle 
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

# Loading sounds
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('first_py_game/Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('first_py_game/Assets', 'Gun+Silencer.mp3'))

# Setting fonts
HEALTH_FONT = pygame.font.SysFont('arial', 30)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Define variables
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Unique event IDs
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# assigning spaceship images to variables
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('first_py_game/Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('first_py_game/Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Background
SPACE_BG = pygame.transform.scale(
    pygame.image.load(os.path.join(
        'first_py_game/Assets', 'space.png')), (WIDTH, HEIGHT))

#Drawing pygame window
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE_BG, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    # Health bar fonts
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)

    #Draw health bars
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    #Draw spaceships
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


# define function to handle bullet events
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    # Handles yellow bullets
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
            
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    # Handles red bullets
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

        elif bullet.x < 0:
            red_bullets.remove(bullet)

#Handling movements
def yellow_handle_movement(keys_pressed, yellow):
        # Key movement for Yellow 
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # LEFT
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x + 20: # RIGHT
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # UP
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # DOWN
            yellow.y += VEL

def red_handle_movement(keys_pressed, red):
        # Key movement for Red
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # LEFT
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH + 25: # RIGHT
            red.x += VEL
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # UP
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: # DOWN
            red.y += VEL
    
# Draw winner text and restart game after 5 seconds
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

# Main game function
def main():
    yellow = pygame.Rect(100, HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(800, HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # empty lists for bullets
    yellow_bullets = []
    red_bullets = []

    # starting health
    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # Handles yellow bullets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            # Handles red bullets
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            # Removes health
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            # Removes health
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        # Displays winner
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow wins!"

        if yellow_health <= 0:
            winner_text = "Red wins!"

        # Draws winner and breaks out of main loop
        if winner_text != "":
            draw_winner(winner_text)
            break

        # Draws functions for gameplay
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()

if __name__ == "__main__":
    main()