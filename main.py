# Ist es eine Primzahl?
# Aufgabe 1 der Klausurersatzleistung mit Herrn Grünke

# Importe
import math  # Mathematische Funktionen wie z.B. Wurzel
import pygame  # Pygame für die GUI
from pygame import mixer  # Pygame für die Musik

breite, höhe = 800, 600  # Fenstergröße


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
nutzereingabe = ""  # Text in der Eingabe
eingabe_ist_primzahl = False  # Ist die Eingabe eine Primzahl?
programm_läuft = True  # Läuft das Programm?

pygame.init()
screen = pygame.display.set_mode((breite, höhe))
pygame.display.set_caption("Ist es eine Primzahl.png")

background_neutral = pygame.image.load("MathemannNEUTRAL.png")
background_neutral = pygame.transform.scale(background_neutral, (breite, höhe))

background_happy = pygame.image.load("MathemannHAPPY.png")
background_happy = pygame.transform.scale(background_happy, (breite, höhe))

background_sad = pygame.image.load("MathemannSAD.png")
background_sad = pygame.transform.scale(background_sad, (breite, höhe))

entry = pygame.Rect(0, 0, breite - 100, 80)
entry.center = (breite // 2, höhe - 100)

clock = pygame.time.Clock()

mixer.init()
mixer.music.load("music.mp3")
mixer.music.play(-1)
mixer.music.set_volume(.2)

def onBackspace():
    global nutzereingabe, eingabe_ist_primzahl
    if len(nutzereingabe) > 0:
        nutzereingabe = nutzereingabe[:-1]
        if len(nutzereingabe) == 0:
            eingabe_ist_primzahl = False
        else:
            eingabe_ist_primzahl = isPrime(int(nutzereingabe))


def drawCall():
    global programm_läuft, nutzereingabe, eingabe_ist_primzahl, entry, background_neutral, background_happy, background_sad, clock, screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programm_läuft = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                onBackspace()
            else:
                # Check if the key is a number
                if event.unicode.isnumeric():
                    nutzereingabe += event.unicode
                    eingabe_ist_primzahl = isPrime(int(nutzereingabe))

    if len(nutzereingabe) == 0:
        mixer.music.set_volume(.2) # Leiser wenn nichts eingegeben ist
        screen.blit(background_neutral, (0, 0))  # Neutral
    elif eingabe_ist_primzahl:
        mixer.music.set_volume(.2) # Leiser wenn richtig ist
        screen.blit(background_happy, (0, 0))  # Happy
    else:
        mixer.music.set_volume(1) # Lauter wenn falsch ist
        screen.blit(background_sad, (0, 0))  # Sad
    pygame.draw.rect(screen, (255, 255, 255), entry)  # Draw the entry box

    if eingabe_ist_primzahl:
        pygame.draw.rect(screen, (0, 255, 0), entry, 5)  # Draw the border of the entry box
    elif len(nutzereingabe) > 0:
        pygame.draw.rect(screen, (255, 0, 0), entry, 5)  # Draw the border of the entry box
    else:
        pygame.draw.rect(screen, (0, 0, 0), entry, 5)
    font = pygame.font.Font(None, 110)
    text_surface = font.render(nutzereingabe, True, (0, 0, 0))
    screen.blit(text_surface, (breite // 2 - text_surface.get_size()[0] // 2, entry.y + 5))

    # Titel in Rainbow Farben
    font = pygame.font.Font(None, 90)
    # Rainbow Farben
    rainbowColor: tuple[int, int, int] = (
        int(math.sin(pygame.time.get_ticks() / 1000 + 0) * 127 + 128),
        int(math.sin(pygame.time.get_ticks() / 1000 + 2) * 127 + 128),
        int(math.sin(pygame.time.get_ticks() / 1000 + 4) * 127 + 128))
    text_surface = font.render("Ist es eine Primzahl?", True, rainbowColor)
    screen.blit(text_surface, (breite // 2 - text_surface.get_size()[0] // 2, höhe-200))

    pygame.display.flip()
    clock.tick(60)


# Main Loop
while programm_läuft:
    drawCall()
pygame.quit()
