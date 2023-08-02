import pygame
from sys import exit

# starts pygame. needs to be before any other pygame code.
# similar to starting the engine of a car
pygame.init()

#display surface
#the game window. anything displayed goes here.
# is unique and must always be visible
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Example Title')
clock = pygame.time.Clock()

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/Ground.png").convert()
text_surface = test_font.render("Hello World!", False, "Black")

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #draw all our elements
    #places surface at position (x,y)
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,50))
    

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    snail_rect.left -= 4
    if snail_rect.left < -100:
        snail_rect.left = 850

    if player_rect.colliderect(snail_rect):
        print("Collide")

    #update everything
    pygame.display.update()
    clock.tick(60)