# Ist es eine Primzahl?
# Aufgabe 1 der Klausurersatzleistung mit Herrn Grünke

# Bitte pygame und mixer installieren

# Importe
import math  # Mathematische Funktionen wie z.B. Wurzel
import pygame  # Pygame für die GUI
from pygame import mixer  # Pygame für die Musik

breite, höhe = 800, 600  # Fenstergröße


# isPrime Funktion
def ist_es_eine_primzahl(n, konsolenausgabe=False):
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
            if konsolenausgabe:
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

hintergrund_neutral = pygame.image.load("MathemannNEUTRAL.png")
hintergrund_neutral = pygame.transform.scale(hintergrund_neutral, (breite, höhe))

hintergrund_happy = pygame.image.load("MathemannHAPPY.png")
hintergrund_happy = pygame.transform.scale(hintergrund_happy, (breite, höhe))

hintergrund_sad = pygame.image.load("MathemannSAD.png")
hintergrund_sad = pygame.transform.scale(hintergrund_sad, (breite, höhe))

eingabefeld = pygame.Rect(0, 0, breite - 100, 80)
eingabefeld.center = (breite // 2, höhe - 100)

clock = pygame.time.Clock()

# Musik usw.
mixer.init()
mixer.music.load("music.mp3")
mixer.music.play(-1)
mixer.music.set_volume(.1)


def rücktaste_gedrückt():
    global nutzereingabe, eingabe_ist_primzahl
    # Lösche das letzte Zeichen der Eingabe, wenn die Eingabe nicht leer ist (Länge > 0)
    if len(nutzereingabe) > 0:
        nutzereingabe = nutzereingabe[:-1]
        if len(nutzereingabe) == 0:
            eingabe_ist_primzahl = False
        else:
            eingabe_ist_primzahl = ist_es_eine_primzahl(int(nutzereingabe))


def bildschirm_zeichnen():
    global programm_läuft, nutzereingabe, eingabe_ist_primzahl, eingabefeld, hintergrund_neutral, hintergrund_happy, hintergrund_sad, clock, screen
    # Zeichne den Inhalt des Bildschirms neu

    # Events abfragen und verarbeiten (z.B. Tastendrücke)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programm_läuft = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                rücktaste_gedrückt()
            elif event.key == pygame.K_ESCAPE:
                programm_läuft = False
            else:
                # Check if the key is a number
                if event.unicode.isnumeric():
                    nutzereingabe += event.unicode
                    eingabe_ist_primzahl = ist_es_eine_primzahl(int(nutzereingabe))

    if len(nutzereingabe) == 0:
        mixer.music.set_volume(.1) # Leiser wenn nichts eingegeben ist
        screen.blit(hintergrund_neutral, (0, 0))  # Neutral
    elif eingabe_ist_primzahl:
        mixer.music.set_volume(.1) # Leiser wenn richtig ist
        screen.blit(hintergrund_happy, (0, 0))  # Happy
    else:
        mixer.music.set_volume(1) # Lauter wenn falsch ist
        screen.blit(hintergrund_sad, (0, 0))  # Sad
    pygame.draw.rect(screen, (255, 255, 255), eingabefeld)  # Draw the entry box

    if eingabe_ist_primzahl:
        pygame.draw.rect(screen, (0, 255, 0), eingabefeld, 5)  # Draw the border of the entry box
    elif len(nutzereingabe) > 0:
        pygame.draw.rect(screen, (255, 0, 0), eingabefeld, 5)  # Draw the border of the entry box
    else:
        pygame.draw.rect(screen, (0, 0, 0), eingabefeld, 5)
    font = pygame.font.Font(None, 110)
    text_surface = font.render(nutzereingabe, True, (0, 0, 0))
    screen.blit(text_surface, (breite // 2 - text_surface.get_size()[0] // 2, eingabefeld.y + 5))

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
    bildschirm_zeichnen()

pygame.quit()
