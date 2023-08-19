import pygame
import sys
import asyncio

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
iconRect.center = (width / 2, height / 2)

# sounds
clickSound = pygame.mixer.Sound("assets/sounds/click.wav")

# random shapes
buyTextContainer = pygame.Rect(((width / 5, height / 5), (300, 100)))
buyTextContainer.center = (width / 5, height / 5)

# text
font = pygame.font.Font(None, 36)
smallFont = pygame.font.Font(None, 18)

buyText = font.render("Buy Chumbud - 10 (+1/s)", True, (120, 120, 120))

# other game variables
count = 0
chumbuds = 0
clock = pygame.time.Clock()
running = True

# functions
def resize(object, newWidth, newHeight, center):
    object.width = newWidth
    object.height = newHeight
    object.center = center

# events
INCREMENT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(INCREMENT_EVENT, 1000)

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == INCREMENT_EVENT:
            count += chumbuds

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if iconRect.collidepoint(position):
                count += 1
                icon = pygame.transform.scale(icon, (250, 250))
                iconRect = icon.get_rect()
                iconRect.center = (width / 2, height / 2)
                pygame.mixer.Sound.play(clickSound)

            if buyTextContainer.collidepoint(position) and count >= 10:
                chumbuds += 1
                count -= 10
                resize(buyTextContainer, 200, 50, (width / 5, height / 5))
                buyText = smallFont.render("Buy Chumbud - 10 (+1/s)", True, (120, 120, 120))

        elif event.type == pygame.MOUSEBUTTONUP:
            icon = pygame.transform.scale(icon, (500, 500))
            iconRect = icon.get_rect()
            iconRect.center = (width / 2, height / 2)
            resize(buyTextContainer, 300, 100, (width / 5, height / 5))
            buyText = font.render("Buy Chumbud - 10 (+1/s)", True, (120, 120, 120))

    screen.fill((0, 0, 0))

    screen.blit(icon, iconRect)

    text = font.render(f"Click Count: {count}", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (width / 2, height / 5)
    screen.blit(text, textRect)

    pygame.draw.rect(screen, (255, 255, 255), buyTextContainer)

    buyTextRect = buyText.get_rect()
    buyTextRect.center = buyTextContainer.center
    screen.blit(buyText, buyTextRect)

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()