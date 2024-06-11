import pygame # Impordib pygame'i mooduli
pygame.init() # Initsialiseerib pygame'i

# Seadista akna suurus
screen = pygame.display.set_mode([500, 800])

# Jooksuta kuni kasutaja sulgeb aken
running = True
while running:

    # Kui kasutaja vajutab sulgemisnuppu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pane taust valgeks
        screen.fill([204, 255, 255])

        # Joon
        #pygame.draw.line(screen, [255,0,0], [100,100], [200,200], 2)

        # Ristkülik
        #pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2)

        # Ring
        #pygame.draw.circle(screen, [255,0,0], [250, 400], 50, 0)

        # Ellips
        #pygame.draw.ellipse(screen, [0,0,255], [100, 100, 200, 100], 2)

        # Polügoon
        #pygame.draw.polygon(screen, [0,0,255], [[100,100], [200,200], [300,100]], 0)

        # Kaar (arc)
        #pygame.draw.arc(screen, [0,0,0], [100, 100, 200, 100], 0, 3.14, 2)
        
    # Uuenda ekraan
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
