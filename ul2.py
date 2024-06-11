import pygame # Impordib pygame'i mooduli
pygame.init() # Initsialiseerib pygame'i

# Seadista akna suurus
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ülesanne 2 - Kangur")

# Jooksuta kuni kasutaja sulgeb aken
running = True
while running:

    # Kui kasutaja vajutab sulgemisnuppu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pane taust valgeks
        screen.fill([204, 255, 255])

        # Taustapilt
        bg = pygame.image.load("img/bg_shop.webp")
        screen.blit(bg, [0,0])

        # Tegelase pilt 
        char = pygame.image.load("img/seller.webp")
        char = pygame.transform.scale(char, [200, 250])
        screen.blit(char, [100,200])

        # Tekstiakna pilt
        text = pygame.image.load("img/chat.webp")
        text = pygame.transform.scale(text, [200, 150])
        screen.blit(text, [200, 150])


        # Tekst tekstiaknasse "Tere, olen Kristjan Kangur"
        font = pygame.font.Font(None, 20)
        text = font.render("Tere, olen Kristjan Kangur", True, [255, 255, 255])
        screen.blit(text, [215, 200])

        ### Lisaülesanne 2

        # Vasakusse nurka VIKK logo
        vikk = pygame.image.load("img/vikk.png")
        vikk = pygame.transform.scale(vikk, [200, 50])
        screen.blit(vikk, [0,0])

        # Logo kõrvale kaarega tekst "TULEVIK 2050"
        font = pygame.font.Font(None, 30)
        text = font.render("TULEVIK 2050", True, [255, 255, 255])
        screen.blit(text, [210, 25])

        # TULEVIK 2050 peal olev kaar
        pygame.draw.arc(screen, [255, 255, 255], [200, 5, 160, 50], 0, 3.14, 2)

        # Laua peale tordipilt
        cake = pygame.image.load("img/tort.png")
        cake = pygame.transform.scale(cake, [100, 100])
        screen.blit(cake, [400, 200])

        # Seina peale mõõgapilt
        sword = pygame.image.load("img/sword.png")
        sword = pygame.transform.scale(sword, [100, 100])
        screen.blit(sword, [540, 150])
                
    # Uuenda ekraan
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
