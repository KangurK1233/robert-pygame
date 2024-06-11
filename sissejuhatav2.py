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

        #lisame teksti
        #font = pygame.font.Font(pygame.font.match_font('arial'), 50)
        #font.set_underline(True)
        #text = font.render("Hello PyGame", True, [0,0,0])

        #tekstikasti suurus
        #text_width = text.get_rect().width
        #text_height = text.get_rect().height

        #screen.blit(text, [320-text_width/2,240-text_height/2])


        #Lisame pildid
        #youWin = pygame.image.load("img/youwin.png")
        #youWin = pygame.transform.scale(youWin, [300, 120])
        #screen.blit(youWin,[180,100])

                
    # Uuenda ekraan
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
