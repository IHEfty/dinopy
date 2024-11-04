import pygame
import random
import configparser

pygame.init()

config = configparser.ConfigParser()
config.read('settings.ini')
theme = config['Settings'].get('theme', 'light')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game by IHEfty")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

if theme == 'dark':
    dino_img = pygame.image.load('res/dino1.png')
    cactus_img = pygame.image.load('res/cactus1.png')
    background_color = BLACK
else:
    dino_img = pygame.image.load('res/dino.png')
    cactus_img = pygame.image.load('res/cactus.png')
    background_color = WHITE

dino_x = 50
ground_level = SCREEN_HEIGHT - dino_img.get_height() - 10
dino_y = ground_level
dino_velocity_y = 0
jump_height = 15
gravity = 1
is_jumping = False

obstacles = []
base_obstacle_speed = 10
obstacle_speed = base_obstacle_speed
min_obstacle_gap = 150
max_obstacle_gap = 300
last_obstacle_x = SCREEN_WIDTH

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

def create_obstacles():
    global last_obstacle_x
    num_cactuses = random.choice([1, 2])
    new_obstacles = []
    for i in range(num_cactuses):
        x_pos = last_obstacle_x + (i * cactus_img.get_width() + 10)
        y_pos = SCREEN_HEIGHT - cactus_img.get_height() - 10
        new_obstacles.append(pygame.Rect(x_pos, y_pos, cactus_img.get_width(), cactus_img.get_height()))
    last_obstacle_x += random.randint(min_obstacle_gap, max_obstacle_gap)
    return new_obstacles

while running:
    screen.fill(background_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                dino_velocity_y = -jump_height
                is_jumping = True

    dino_y += dino_velocity_y
    if is_jumping:
        dino_velocity_y += gravity
        if dino_y >= ground_level:
            dino_y = ground_level
            is_jumping = False
            dino_velocity_y = 0

    obstacle_speed = base_obstacle_speed + int(score // 10)

    if len(obstacles) == 0 or obstacles[-1].x < SCREEN_WIDTH - last_obstacle_x:
        obstacles.extend(create_obstacles())

    for obstacle in obstacles:
        obstacle.x -= obstacle_speed
    obstacles = [obs for obs in obstacles if obs.x > -cactus_img.get_width()]

    dino_rect = dino_img.get_rect(topleft=(dino_x, dino_y))
    for obstacle in obstacles:
        if dino_rect.colliderect(obstacle):
            running = False

    screen.blit(dino_img, (dino_x, dino_y))
    for obstacle in obstacles:
        screen.blit(cactus_img, (obstacle.x, obstacle.y))

    score += 0.1
    score_text = font.render("Score: " + str(int(score)), True, (0, 0, 0) if theme == 'light' else (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    
    clock.tick(30)

pygame.quit()
