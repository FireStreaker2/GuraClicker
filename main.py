import pygame
import sys

pygame.init()

dimensions = pygame.display.Info()
width = dimensions.current_w
height = dimensions.current_h

clock= pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GuraClicker")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()