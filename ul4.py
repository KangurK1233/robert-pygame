import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480

# Setup window
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Rally - Kristjan Kangur")

# Background image
bg = pygame.image.load("img/bg_rally.jpg")

# Red car image
red_car_img = pygame.image.load("img/f1_red.png")
red_car_rect = red_car_img.get_rect()
red_car_rect.centerx = 320
red_car_rect.bottom = 470

# Blue car image
blue_car_img = pygame.image.load("img/f1_blue.png")

# Game variables
score = 0
clock = pygame.time.Clock()
car_speed = 5
car_spawn_delay = 60
car_width = 40
car_height = 80
car_x_positions = [175, (screen_width - car_width) // 2, screen_width - 220]  # X-coordinates of three lanes
blue_cars = {i: [] for i in range(3)}  # Lists of blue cars in each lane

# Function to add blue cars
def add_blue_car(lane):
    if len(blue_cars[lane]) < 2:  # Limiting to 2 blue cars per lane
        blue_car_rect = blue_car_img.get_rect()
        blue_car_rect.left = car_x_positions[lane]
        blue_car_rect.top = -blue_car_rect.height
        blue_cars[lane].append(blue_car_rect)

# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control the red car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        red_car_rect.centerx -= car_speed
    if keys[pygame.K_RIGHT]:
        red_car_rect.centerx += car_speed

    # Update blue cars' position and check collision with red car
    for lane, blue_cars_lane in blue_cars.items():
        for blue_car_rect in blue_cars_lane:
            blue_car_rect.y += car_speed
            if blue_car_rect.colliderect(red_car_rect):
                # Reaction to collision
                pass
            if blue_car_rect.y > 480:
                blue_cars_lane.remove(blue_car_rect)
                add_blue_car(lane)
                score += 1

    # Update the screen
    screen.blit(bg, (0, 0))
    screen.blit(red_car_img, red_car_rect)
    for lane, blue_cars_lane in blue_cars.items():
        for blue_car_rect in blue_cars_lane:
            screen.blit(blue_car_img, blue_car_rect)
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    clock.tick(60)

    # Add blue cars
    car_spawn_delay -= 1
    if car_spawn_delay == 0:
        add_blue_car(random.randint(0, 2))
        car_spawn_delay = 60
        

# Quit the game
pygame.quit()
