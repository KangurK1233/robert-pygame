import pygame
pygame.init()

# Seadista aken
screen = pygame.display.set_mode([500, 800])
pygame.display.set_caption("Foor - Kristjan Kangur")

# Jooksuta kuni kasutaja sulgeb aken
running = True
while running:

    # Kui kasutaja vajutab sulgemisnuppu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pane taust valgeks
    screen.fill((255, 255, 255))

    # Joonista ekraani keskele valgusfoor
    pygame.draw.rect(screen, (0, 0, 0), (200, 100, 100, 300), 0)
    pygame.draw.circle(screen, (255, 0, 0), (250, 150), 45)
    pygame.draw.circle(screen, (255, 255, 0), (250, 250), 45)
    pygame.draw.circle(screen, (0, 255, 0), (250, 350), 45)
    pygame.draw.line(screen, (0, 0, 0), (250, 400), (250, 700), 20)

    # Joonista foorile alus, mis näeb välja nagu /_\
    pygame.draw.polygon(screen, (0, 0, 0), [(200, 100), (300, 100), (250, 50)])
    pygame.draw.polygon(screen, (0, 0, 0), [(200, 400), (300, 400), (250, 450)])
    pygame.draw.polygon(screen, (0, 0, 0), [(200, 100), (200, 400), (150, 250)])
    pygame.draw.polygon(screen, (0, 0, 0), [(300, 100), (300, 400), (350, 250)])
    pygame.draw.polygon(screen, (0, 0, 0), [(200, 700), (300, 700), (250, 800)])

    # Joonista foori aluse sisse eesti lipp
    pygame.draw.rect(screen, (0, 0, 255), (200, 720, 100, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), (200, 740, 100, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255), (200, 760, 100, 20), 0)




    


    # Uuenda ekraan
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
