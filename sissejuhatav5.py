import pygame
import random
import time
pygame.init()
 
#värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
 
#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Surface")
screen.fill(lBlue)
clock = pygame.time.Clock()
posX, posY = 0, 0
speedX, speedY = 2, 4

####################################################
#Surface kasutamine
#surf = pygame.Surface((200,200))
#pygame.draw.circle(surf,blue,(140,100), 100)
#pygame.draw.circle(surf,green,(100,160), 80)
#pygame.draw.circle(surf,pink,(50,100), 60)
#screen.blit(surf,(0,0))
####################################################

####################################################
#Surface kasutamine 2
#surf = pygame.Surface((200,200))
#surf.set_colorkey((0,0,0))
#pygame.draw.circle(surf,blue,(140,100), 100)
#pygame.draw.circle(surf,green,(100,160), 80)
#pygame.draw.circle(surf,pink,(50,100), 60)
#screen.blit(surf,(0,0))
#screen.blit(surf,(100,100))
#screen.blit(surf,(400,300))
####################################################

####################################################
#Rect kasutamine
#player = pygame.Rect(0,0, 120, 140)
#pygame.draw.rect(screen, red, player)
#playerImage = pygame.image.load("img/seller.webp")
#playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

#screen.blit(playerImage,player)
#screen.blit(playerImage,player.center)
####################################################

####################################################
#Kokkupõrke tuvastamine
#player
player = pygame.Rect(posX, posY, 120, 140)
playerImage = pygame.image.load("img/seller.webp")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

#enemy - tekitame 5 suvalist vaenlast
enemies = []
for i in range(5):
    enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))
enemyImage = pygame.image.load('img/tort.png')
enemyImage = pygame.transform.scale(enemyImage, [enemies[0].width, enemies[0].height])


enemyCounter = 0
totalEnemies = 20
score = 0

gameover = False
while not gameover:
    #mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    #player liikumine
    player = pygame.Rect(posX, posY, 120, 140)
    screen.blit(playerImage,player)
    
    posX += speedX
    posY += speedY

    if posX > screenX-playerImage.get_rect().width or posX < 0:
        speedX = -speedX
 
    if posY > screenY-playerImage.get_rect().height or posY < 0:
        speedY = -speedY


    #enemy loomine
    enemyCounter += 1
    if enemyCounter >= totalEnemies:
        enemyCounter = 0
        enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1
    
    for enemy in enemies:
        screen.blit(enemyImage, enemy)

    pygame.display.flip()
    screen.fill(lBlue)
    
    print(score)
    if score == 20:
        gameover = True
pygame.quit()