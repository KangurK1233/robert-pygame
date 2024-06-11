import pygame
import random

pygame.init()

# Colors
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
black = [0, 0, 0]
white = [255, 255, 255]

# Screen settings
screenX = 880
screenY = 640
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Snake Game")

# Background Image
background_image = pygame.image.load("img/Background.jpg")
background_image = pygame.transform.scale(background_image, (screenX, screenY))

# Snake speed
snake_speed = 10
directionX = 0
directionY = 0
posX, posY = screenX / 2, screenY / 2

# Apple creation
apple = pygame.Rect(0, 0, 20, 20)
appleImage = pygame.image.load("img/apple.png")
appleImage = pygame.transform.scale(appleImage, [apple.width, apple.height])
apple.x = random.randint(0, screenX - apple.width)
apple.y = random.randint(0, screenY - apple.height)

# High score loading and saving
def load_high_score():
    try:
        with open('highscore.txt', 'r') as file:
            high_score = int(file.read())
    except:
        high_score = 0
    return high_score

def save_high_score(high_score):
    with open('highscore.txt', 'w') as file:
        file.write(str(high_score))

# Hit sound
hit_sound = pygame.mixer.Sound("sounds/hit.wav")

# Background music
def play_music():
    music = ['music/hiphop1.mp3', 'music/house1.mp3', 'music/lofi1.mp3', 'music/techno1.mp3']
    
    current_music = random.choice(music)
    while current_music == pygame.mixer.music.get_busy():
        current_music = random.choice(music)
        
    pygame.mixer.music.load(current_music)
    pygame.mixer.music.play(-1)
    return current_music

# Score
score = 0
font = pygame.font.Font(None, 28)

# Frame rate
clock = pygame.time.Clock()
FPS = 30

star = pygame.image.load("img/star.png")

# Generate 1 to 5 star rating for game over screen
def generate_star_rating(score):
    if score < 5:
        stars = 1
    elif score < 10:
        stars = 2
    elif score < 15:
        stars = 3
    elif score < 20:
        stars = 4
    elif score >= 21:
        stars = 5
    
    return stars

# Place stars on screen based on rating
def place_stars(rating):
    star_spacing = 60  # Adjusted spacing between stars
    star_start_pos = (screenX - (star_spacing * rating)) // 2  # Center stars horizontally
    star_y_pos = 90

    for i in range(rating):
        screen.blit(pygame.transform.scale(star, (55, 55)), (star_start_pos + i * star_spacing, star_y_pos))  # Adjusted star size


# Game over function
def game_over():
    if score > high_score:
        save_high_score(score)

    star_rating = generate_star_rating(score)

    apple.x = -100
    apple.y = -100
    gameOverImage = pygame.image.load("img/Gameover.jpg")
    gameOverImage = pygame.transform.scale(gameOverImage, (screenX, screenY))
    screen.blit(gameOverImage, (0, 0))
    pygame.display.flip()

    font = pygame.font.Font(None, 36)
    text = font.render("Vajuta SPACE, et uuesti mängida..", True, white)
    textRect = text.get_rect()
    textRect.center = (screenX // 2, screenY // 2 + 190)
    screen.blit(text, textRect)

    # Display score
    score_text = font.render("Sinu skoor: " + str(score), True, white)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (250, screenY // 2 + 240)
    screen.blit(score_text, score_text_rect)

    # Display high score
    high_score_text = font.render("Suurim skoor: " + str(high_score), True, white)
    high_score_text_rect = high_score_text.get_rect()
    high_score_text_rect.center = (650, screenY // 2 + 240)
    screen.blit(high_score_text, high_score_text_rect)


    place_stars(star_rating)
    pygame.display.flip()
    pygame.mixer.music.pause()



# Snake creation
snake_body = [pygame.Rect(posX, posY, 20, 20)]
play_music()

def show_main_menu():
    menu = True
    while menu:
        screen.fill(white)
        font = pygame.font.Font(None, 50)
        title = font.render("(n)Ussimäng", True, black)
        title_rect = title.get_rect(center=(screenX // 2, screenY // 2 - 50))
        screen.blit(title, title_rect)

        font = pygame.font.Font(None, 36)
        play_text = font.render("Vajuta SPACE, et mängida", True, black)
        play_rect = play_text.get_rect(center=(screenX // 2, screenY // 2 + 50))
        screen.blit(play_text, play_rect)

        font = pygame.font.Font(None, 24)
        play_text = font.render("Vajuta R mängimise ajal, et muusikat vahetada", True, black)
        play_rect = play_text.get_rect(center=(screenX // 2, screenY // 2 + 100))
        screen.blit(play_text, play_rect)

        font = pygame.font.Font(None, 24)
        play_text = font.render("Skoor 1-5: 1 täht", True, black)
        play_rect = play_text.get_rect(center=(screenX // 2, screenY // 2 + 120))
        screen.blit(play_text, play_rect)

        font = pygame.font.Font(None, 24)
        play_text = font.render("Skoor 6-10: 2 tähte", True, black)
        play_rect = play_text.get_rect(center=(screenX // 2, screenY // 2 + 140))
        screen.blit(play_text, play_rect)

        font = pygame.font.Font(None, 24)
        play_text = font.render("Skoor 11-15: 3 tähte", True, black)
        play_rect = play_text.get_rect(center=(screenX // 2, screenY // 2 + 160))
        screen.blit(play_text, play_rect)

        font = pygame.font.Font(None, 24)
        play_text = font.render("Skoor 16-20: 4 tähte", True, black)
        play_rect = play_text.get_rect(center=(screenX // 2, screenY // 2 + 180))
        screen.blit(play_text, play_rect)

        font = pygame.font.Font(None, 24)
        play_text = font.render("Skoor 21+: 5 tähte", True, black)
        play_rect = play_text.get_rect(center=(screenX // 2, screenY // 2 + 200))
        screen.blit(play_text, play_rect)




        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False

# Main menu
show_main_menu()

gameover = False
while not gameover:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and directionX == 0:
                directionX = snake_speed
                directionY = 0
            elif event.key == pygame.K_LEFT and directionX == 0:
                directionX = -snake_speed
                directionY = 0
            elif event.key == pygame.K_UP and directionY == 0:
                directionX = 0
                directionY = -snake_speed
            elif event.key == pygame.K_DOWN and directionY == 0:
                directionX = 0
                directionY = snake_speed
            elif event.key == pygame.K_SPACE:
                posX, posY = screenX / 2, screenY / 2
                directionX = 0
                directionY = 0
                snake_body = [pygame.Rect(posX, posY, 20, 20)]
                score = 0
                apple.x = random.randint(0, screenX - apple.width)
                apple.y = random.randint(0, screenY - apple.height)
                play_music()
            elif event.key == pygame.K_r:
                play_music()

    screen.blit(background_image, (0, 0))
    high_score = load_high_score()

    posX += directionX
    posY += directionY

    snake_head = pygame.Rect(posX, posY, 20, 20)
    snake_body.insert(0, snake_head)

    if snake_head.colliderect(apple):
        apple.x = random.randint(0, screenX - apple.width)
        apple.y = random.randint(0, screenY - apple.height)
        score += 1
        hit_sound.play()
    else:
        snake_body.pop()

    for segment in snake_body:
        pygame.draw.rect(screen, green, segment)

    if posX < 0 or posX + snake_head.width > screenX or posY < 0 or posY + snake_head.height > screenY:
        game_over()

    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (450, 70))

    size_text = font.render("High Score: " + str(high_score), True, black)
    screen.blit(size_text, (280, 70))

    screen.blit(appleImage, (apple.x, apple.y))

    pygame.display.flip()

pygame.quit()
