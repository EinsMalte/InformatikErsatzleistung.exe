# Ist es eine Primzahl?
# Aufgabe 1 der Klausurersatzleistung mit Herrn Grünke

# Importe
import math
import pygame
from pygame import mixer

w, h = 800, 600  # Fenstergröße


# isPrime Funktion
def isPrime(n, verbose=False):
    # returns True or False
    # Wenn n = 2 wird True ausgegeben
    if n == 2:
        return True  # Funktion hier beendet

    # Wenn n kleiner 2 oder teilbar durch 2 ist, wird False ausgegeben
    if n < 2 or n % 2 == 0:
        return False  # Beendet die Funktion

    # Prüfe alle Zahlen zwischen 3 und r
    i = 3
    r = math.sqrt(n)  # Wurzel ausrechnen

    # Wenn die Wurzel durch 1 restlos teilbar ist dann ist keine Primzahl
    if r % 1 == 0:
        return False

    while True:  # Bis return
        if i > r:
            return True

        if n % i == 0:
            if verbose:
                print(f"{n} ist teilbar durch {i}")
            return False
        i += 2


# Code für pygame als GUI
entry_text = ""
entryPrime = False
running = True

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Number Input")

background_neutral = pygame.image.load("MathemannNEUTRAL.png")
background_neutral = pygame.transform.scale(background_neutral, (w, h))

background_happy = pygame.image.load("MathemannHAPPY.png")
background_happy = pygame.transform.scale(background_happy, (w, h))

background_sad = pygame.image.load("MathemannSAD.png")
background_sad = pygame.transform.scale(background_sad, (w, h))

entry = pygame.Rect(0, 0, w - 100, 80)
entry.center = (w // 2, h - 100)

clock = pygame.time.Clock()

mixer.init()
mixer.music.load("music.mp3")
mixer.music.play(-1)
mixer.music.set_volume(.2)

def onBackspace():
    global entry_text, entryPrime
    if len(entry_text) > 0:
        entry_text = entry_text[:-1]
        if len(entry_text) == 0:
            entryPrime = False
        else:
            entryPrime = isPrime(int(entry_text))


def drawCall():
    global running, entry_text, entryPrime, entry, background_neutral, background_happy, background_sad, clock, screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                onBackspace()
            else:
                # Check if the key is a number
                if event.unicode.isnumeric():
                    entry_text += event.unicode
                    entryPrime = isPrime(int(entry_text))

    if len(entry_text) == 0:
        screen.blit(background_neutral, (0, 0))  # Neutral
    elif entryPrime:
        screen.blit(background_happy, (0, 0))  # Happy
    else:
        screen.blit(background_sad, (0, 0))  # Sad
    pygame.draw.rect(screen, (255, 255, 255), entry)  # Draw the entry box

    if entryPrime:
        pygame.draw.rect(screen, (0, 255, 0), entry, 5)  # Draw the border of the entry box
    elif len(entry_text) > 0:
        pygame.draw.rect(screen, (255, 0, 0), entry, 5)  # Draw the border of the entry box
    else:
        pygame.draw.rect(screen, (0, 0, 0), entry, 5)
    font = pygame.font.Font(None, 110)
    text_surface = font.render(entry_text, True, (0, 0, 0))
    screen.blit(text_surface, (w // 2 - text_surface.get_size()[0] // 2, entry.y + 5))

    # Titel in Rainbow Farben
    font = pygame.font.Font(None, 90)
    # Rainbow Farben
    rainbowColor: tuple[int, int, int] = (
        int(math.sin(pygame.time.get_ticks() / 1000 + 0) * 127 + 128),
        int(math.sin(pygame.time.get_ticks() / 1000 + 2) * 127 + 128),
        int(math.sin(pygame.time.get_ticks() / 1000 + 4) * 127 + 128))
    text_surface = font.render("Ist es eine Primzahl?", True, rainbowColor)
    screen.blit(text_surface, (w // 2 - text_surface.get_size()[0] // 2, h-200))

    pygame.display.flip()
    clock.tick(60)


# Main Loop
while running:
    drawCall()
pygame.quit()
