import pygame
import sys

pygame.init()

# window config
dimensions = pygame.display.Info()
width = dimensions.current_w
height = dimensions.current_h
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GuraClicker")

# images
icon = pygame.image.load("assets/images/icon.png")
pygame.display.set_icon(icon)

iconRect = icon.get_rect()
iconIdleSize = iconRect.size
iconClickedSize = (iconIdleSize[0] / 2, iconIdleSize[1] / 2)
iconSize = iconIdleSize

# sounds
clickSound = pygame.mixer.Sound("assets/sounds/click.wav")

# other game variables
count = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if iconRect.collidepoint(position):
                count += 1
                iconSize = iconClickedSize
                pygame.mixer.Sound.play(clickSound)

        elif event.type == pygame.MOUSEBUTTONUP:
            iconSize = iconIdleSize
    
    screen.fill((0, 0, 0))

    iconRect.size = iconSize
    iconRect.center = (width / 2, height / 2)
    screen.blit(pygame.transform.scale(icon, iconSize), iconRect)

    text = font.render(f"Click Count: {count}", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (width / 2, height / 5)
    screen.blit(text, textRect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()