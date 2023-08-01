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

sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/Ground.png")
text_surface = test_font.render("Hello World!", False, "Black")

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

    #update everything
    pygame.display.update()
    clock.tick(60)