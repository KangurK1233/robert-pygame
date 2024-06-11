import pygame
import random
pygame.init()

# Värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
black = [0, 0, 0]

# Ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Snake Game")
screen.fill(lBlue)
snake_speed = 15
directionX = 0
directionY = 0
posX, posY = screenX/2, screenY/2

# Heli lisamine
sounds = ['techno1.mp3', 'hiphop1.mp3', 'house1.mp3', 'lofi1.mp3']
pygame.mixer.music.load('music/'+random.choice(sounds))
pygame.mixer.music.play()

# Õuna loomine 
apple = pygame.Rect(0, 0, 20, 20)
appleImage = pygame.image.load("img/apple.png")
appleImage = pygame.transform.scale(appleImage, [apple.width, apple.height])
apple.x = random.randint(0, screenX - apple.width)
apple.y = random.randint(0, screenY - apple.height)

# Skoor
score = 0
font = pygame.font.Font(None, 36)

# Raami kiirus
clock = pygame.time.Clock()
FPS = 30  # See on raami kiirus. Vähendage seda, et mängu aeglustada.

# Mao loomine
snake_body = [pygame.Rect(posX, posY, 20, 20)]

gameover = False
while not gameover:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        #klahvivajutus
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                directionX = "move_right"
                posX += 3
            elif event.key == pygame.K_LEFT:
                directionX = "move_left"
                posX -= 3
            elif event.key == pygame.K_UP:
                directionY = "move_up"
                posY -= 3
            elif event.key == pygame.K_DOWN:
                directionY = "move_down"
                posY += 3

        #klahvivajutuse vabastamine
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                directionX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                directionY = 0
    screen.fill(lBlue)

    # Spawning the snake
    snake_head = pygame.Rect(posX, posY, 20, 20)
    snake_body.insert(0, snake_head)  # Add the new head to the body

    # Õuna kokkupõrge
    if snake_head.colliderect(apple):
        apple.x = random.randint(0, screenX - apple.width)
        apple.y = random.randint(0, screenY - apple.height)
        score += 1
        pygame.mixer.Sound.play(pygame.mixer.Sound('sounds/hit.wav'))
    else:
        snake_body.pop()  # Remove the last segment of the snake if it didn't eat an apple

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, green, segment)


    # mängu piirjoonte tuvastamine
    if directionX == "move_left":
        if posX > 0:
            posX -= 3
    elif directionX == "move_right":
        if posX + snake_body[0].width < screenX:  # Adjust the boundary check to account for the size of the snake
            posX += 3
    if directionY == "move_up":
        if posY > 0:
            posY -= 3
    elif directionY == "move_down":
        if posY + snake_body[0].height < screenY:  # Adjust the boundary check to account for the size of the snake
            posY += 3

    # Skoori kuvamine
    score_text = font.render("Score: "+str(score), True, black)
    screen.blit(score_text, (10, 10))

    # Õuna kuvamine
    screen.blit(appleImage, (apple.x, apple.y))


    pygame.display.flip()

pygame.quit()