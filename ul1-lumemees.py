import pygame
pygame.init()

# Seadista aken
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Lumemees - Kristjan Kangur")

# Jooksuta kuni kasutaja sulgeb aken
running = True
while running:

    # Kui kasutaja vajutab sulgemisnuppu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pane taust valgeks
    screen.fill((102, 178, 255))

    # Joonista ekraani keskele lumememm (3 ringi)
    pygame.draw.circle(screen, (0, 0, 0), (250, 165), 40)
    pygame.draw.circle(screen, (0, 0, 0), (250, 250), 50)
    pygame.draw.circle(screen, (0, 0, 0), (250, 350), 60)

    # Joonista lumememmele silmad
    pygame.draw.circle(screen, (255, 255, 255), (240, 150), 5)
    pygame.draw.circle(screen, (255, 255, 255), (260, 150), 5)
    
    # Joonista lumememmele nina (kolmnurk)
    pygame.draw.polygon(screen, (255, 0, 0), [(250, 155), (245, 160), (255, 160)])

    # Joonista lumememmele käed
    pygame.draw.line(screen, (0, 0, 0), (200, 250), (150, 200), 5)
    pygame.draw.line(screen, (0, 0, 0), (300, 250), (350, 200), 5)

    # Joonista lumememmele 3 nööpi
    pygame.draw.circle(screen, (0, 0, 0), (250, 250), 5)
    pygame.draw.circle(screen, (0, 0, 0), (250, 280), 5)
    pygame.draw.circle(screen, (0, 0, 0), (250, 310), 5)

    # Joonista lumememmele müts
    pygame.draw.rect(screen, (0, 0, 0), (225, 100, 50, 50), 0)
    pygame.draw.polygon(screen, (0, 0, 0), [(200, 100), (300, 100), (250, 50)])

    # Joonista lumememmele kätte hari
    pygame.draw.line(screen, (0, 0, 0), (150, 200), (100, 150), 5)
    pygame.draw.line(screen, (0, 0, 0), (350, 200), (400, 150), 5)

    # Joonista päike
    pygame.draw.circle(screen, (255, 255, 0), (700, 50), 80)

    # Joonista 3 pilve
    pygame.draw.circle(screen, (255, 255, 255), (100, 50), 40)
    pygame.draw.circle(screen, (255, 255, 255), (150, 50), 40)
    pygame.draw.circle(screen, (255, 255, 255), (200, 50), 40)
    pygame.draw.circle(screen, (255, 255, 255), (300, 50), 40)
    pygame.draw.circle(screen, (255, 255, 255), (350, 50), 40)
    pygame.draw.circle(screen, (255, 255, 255), (400, 50), 40)
    pygame.draw.circle(screen, (255, 255, 255), (500, 50), 40)
    pygame.draw.circle(screen, (255, 255, 255), (550, 50), 40)
    pygame.draw.circle(screen, (255, 255, 255), (600, 50), 40)

    # Uuenda ekraan
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
