import pygame
import sys
pygame.init()

# Colors
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# Screen settings
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Animation")
screen.fill(lBlue)

# Ball creation
ball = pygame.Rect(0, 0, 20, 20)
ballImage = pygame.image.load("img/ball.png")
ballImage = pygame.transform.scale(ballImage, [ball.width, ball.height])
ballSpeedX = 7
ballSpeedY = 7

# Base creation
base = pygame.Rect(0, screenY/1.5, 120, 20)
baseImage = pygame.image.load("img/pad.png")
baseImage = pygame.transform.scale(baseImage, [base.width, base.height])
baseSpeed = 6
baseDirection = 1  # 1 for right, -1 for left

# Score
score = 0
font = pygame.font.Font(None, 36)

# Frame rate
clock = pygame.time.Clock()
FPS = 30  # This is the frame rate. Lower it to slow down the game.

gameover = False
while not gameover:
    # Closing the game from the cross
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # Ball movement and collision with walls
    ball.move_ip(ballSpeedX, ballSpeedY)
    if ball.left < 0 or ball.right > screenX:
        ballSpeedX *= -1
    if ball.top < 0:
        ballSpeedY *= -1
    if ball.bottom > screenY:
        ballSpeedY *= -1
        score -= 1  # Deduct point when ball misses the base

    # Base movement and collision with walls
    base.move_ip(baseSpeed * baseDirection, 0)
    if base.left <= 0:
        baseDirection = 1
    elif base.right >= screenX:
        baseDirection = -1

    # Collision detection between ball and base
    if ball.colliderect(base):
        ballSpeedY *= -1
        score += 1  # Add point when ball hits the base

    # Draw everything
    screen.fill(lBlue)
    screen.blit(ballImage, ball)
    screen.blit(baseImage, base)

    # Display score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()