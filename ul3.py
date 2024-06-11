import pygame # Impordib pygame'i mooduli
import random # Impordib random mooduli
pygame.init() # Initsialiseerib pygame'i

# Seadista akna suurus
screen = pygame.display.set_mode([640, 480])

# Ekraani pealkiri
pygame.display.set_caption("ÜL3 - kristjan kangur")

# Jooksuta kuni kasutaja sulgeb aken
running = True
while running:

    # Kui kasutaja vajutab sulgemisnuppu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Taust heleroheliseks
    screen.fill([204, 255, 204])

    # Joonista ekraan grid (ruudustik) täis
    def draw_grid(color, width, height, cell_size):
        for x in range(0, width, cell_size):
            pygame.draw.line(screen, color, [x, 0], [x, height])
        for y in range(0, height, cell_size):
            pygame.draw.line(screen, color, [0, y], [width, y])

    draw_grid([255, 0, 255], 640, 480, 20)    
       
    # Uuenda ekraan
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
