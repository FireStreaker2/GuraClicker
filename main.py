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

# colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (120, 120, 120)

# images
icon = pygame.image.load("assets/images/icon.png")
pygame.display.set_icon(icon)

iconRect = icon.get_rect()
iconRect.center = (width / 2, height / 2)

chumbud = pygame.image.load("assets/images/chumbud.png")
chumbudRect = chumbud.get_rect()
chumbud = pygame.transform.scale(chumbud, (100, 100))

atlantis = pygame.image.load("assets/images/atlantis.png")
atlantisRect = atlantis.get_rect()
atlantis = pygame.transform.scale(atlantis, (200, 200))

# sounds
clickSound = pygame.mixer.Sound("assets/sounds/click.wav")

# random shapes
buyTextContainer = pygame.Rect(((width / 5, height / 5), (500, 100)))
buyTextContainer.center = (width / 5, height / 5)

rebuildContainer = pygame.Rect(((1592, 200), (400, 300)))

# text
font = pygame.font.Font(None, 36)
mediumFont = pygame.font.Font(None, 27)
smallFont = pygame.font.Font(None, 18)

buyText = font.render("Buy Chumbud - 10 (+1/s)", True, gray)
rebuildText = font.render("Rebuild Atlantis! - 1,000,000", True, gray)

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
    # event loop
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
                resize(buyTextContainer, 250, 50, (width / 5, height / 5))
                buyText = smallFont.render("Buy Chumbud - 10 (+1/s)", True, gray)
                chumbud = pygame.transform.scale(chumbud, (50, 50))

            if rebuildContainer.collidepoint(position):# and count >= 1000000:
                resize(rebuildContainer, 200, 200, (width / 5 * 4, height / 4))
                rebuildText = smallFont.render("Rebuild Atlantis! - 1,000,000", True, gray)
                atlantis = pygame.transform.scale(atlantis, (100, 100))
                atlantisRect = atlantis.get_rect()
                atlantisRect.center = (rebuildContainer.center[0] + 10, rebuildContainer.center[1] - 20)

                running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            icon = pygame.transform.scale(icon, (500, 500))
            chumbud = pygame.transform.scale(chumbud, (100, 100))
            iconRect = icon.get_rect()
            iconRect.center = (width / 2, height / 2)
            resize(buyTextContainer, 500, 100, (width / 5, height / 5))
            buyText = font.render("Buy Chumbud - 10 (+1/s)", True, gray)
            resize(rebuildContainer, 400, 300, (width / 5 * 4, height / 4))
            rebuildText = font.render("Rebuild Atlantis! - 1,000,000", True, gray)
            atlantis = pygame.transform.scale(atlantis, (200, 200))
            atlantisRect = atlantis.get_rect()
            atlantisRect.center = (rebuildContainer.center[0] + 10, rebuildContainer.center[1] - 20)

    screen.fill(black)

    # icon
    screen.blit(icon, iconRect)

    # click text
    text = font.render(f"Click Count: {count}", True, white)
    textRect = text.get_rect()
    textRect.center = (width / 2, height / 5)
    screen.blit(text, textRect)

    # chumbuds
    pygame.draw.rect(screen, white, buyTextContainer)

    buyTextRect = buyText.get_rect()
    buyTextRect.center = (buyTextContainer.center[0] + 50, buyTextContainer.center[1])
    screen.blit(buyText, buyTextRect)

    chumbudRect.center = (buyTextContainer.x + 150, buyTextContainer.y + 110)
    screen.blit(chumbud, chumbudRect)

    buyTextInfo = mediumFont.render(f"Chumbud Count: {chumbuds} (+{chumbuds}/s)", True, gray)
    buyTextInfoRect = buyTextInfo.get_rect()
    buyTextInfoRect.center = (textRect.center[0], textRect.center[1] + 30)
    screen.blit(buyTextInfo, buyTextInfoRect)

    # rebuild atlantis!!!
    pygame.draw.rect(screen, white, rebuildContainer)
    atlantisRect.center = (rebuildContainer.center[0] + 10, rebuildContainer.center[1] - 20)
    screen.blit(atlantis, atlantisRect)

    rebuildTextRect = rebuildText.get_rect()
    rebuildTextRect.center = (rebuildContainer.center[0] + 10, rebuildContainer.center[1] + 70)
    screen.blit(rebuildText, rebuildTextRect)

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()