### Informatik Klausurersatzleistung
#   Fachlehrer: Herr Grünke
#   Code von: Arasp, Nick, Tobias und Malte
#   Datum: 18.12.2023
#   Dependencies: pygame, math
### Aufgabe 1 (Primzahlenerkennung)

# Importe
import math
import pygame
from pygame import mixer

# Konfiguration
fenster_breite, fenster_höhe = 800, 600
fps = 60

### Funktionen
# Primzahlenerkennung
def ist_es_eine_primzahl(n, konsolenausgabe=False):
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
nutzereingabe: str = ""             # Text in der Eingabe
eingabe_ist_primzahl: bool = False  # Ist die Eingabe eine Primzahl?
programm_läuft: bool = True         # Läuft das Programm?

pygame.init()  # Initialisiere pygame
screen = pygame.display.set_mode((fenster_breite, fenster_höhe))  # Erstelle das Fenster
pygame.display.set_caption("Ist es eine Primzahl.png")  # Setze den Titel des Fensters

hintergrund_neutral = pygame.image.load("MathemannNEUTRAL.png")  # Lade das Bild
hintergrund_neutral = pygame.transform.scale(hintergrund_neutral, (fenster_breite, fenster_höhe))  # Skaliere das Bild

hintergrund_happy = pygame.image.load("MathemannHAPPY.png")  # Lade das Bild
hintergrund_happy = pygame.transform.scale(hintergrund_happy, (fenster_breite, fenster_höhe))  # Skaliere das Bild

hintergrund_sad = pygame.image.load("MathemannSAD.png")  # Lade das Bild
hintergrund_sad = pygame.transform.scale(hintergrund_sad, (fenster_breite, fenster_höhe))  # Skaliere das Bild

eingabefeld = pygame.Rect(0, 0, fenster_breite - 100, 80)  # Erstelle das Eingabefeld
eingabefeld.center = (fenster_breite // 2, fenster_höhe - 100)  # Zentriere das Eingabefeld

clock = pygame.time.Clock()  # Erstelle die Uhr für die Framerate

# Musik usw.
mixer.init()  # Initialisiere pygame.mixer
mixer.music.load("music.mp3")  # Lade die Musik
mixer.music.play(-1)  # Spiele die Musik ab (-1 = Endlosschleife)
mixer.music.set_volume(.1)  # Setze die Lautstärke


# Funktion für die Rücktaste
def rücktaste_gedrückt():
    global nutzereingabe, eingabe_ist_primzahl
    # Lösche das letzte Zeichen der Eingabe, wenn die Eingabe nicht leer ist (Länge > 0)
    if len(nutzereingabe) > 0:  # Wenn die Eingabe nicht leer ist
        nutzereingabe = nutzereingabe[:-1]  # Lösche das letzte Zeichen
        if len(nutzereingabe) == 0:  # Wenn die Eingabe jetzt leer ist
            eingabe_ist_primzahl = False  # Setze die Eingabe auf False
        else:  # Wenn die Eingabe nicht leer ist
            eingabe_ist_primzahl = ist_es_eine_primzahl(int(nutzereingabe))  # Prüfe ob die Eingabe eine Primzahl ist


# Funktion für das Zeichnen des Bildschirms
def bildschirm_zeichnen():
    global programm_läuft, nutzereingabe, eingabe_ist_primzahl, eingabefeld, hintergrund_neutral, hintergrund_happy, hintergrund_sad, clock, screen  # Globale Variablen
    # Zeichne den Inhalt des Bildschirms neu

    # Events abfragen und verarbeiten (z.B. Tastendrücke)
    for event in pygame.event.get():  # Alle Events abfragen
        if event.type == pygame.QUIT:  # Wenn das Fenster geschlossen wird
            programm_läuft = False  # Beende das Programm
        elif event.type == pygame.KEYDOWN:  # Wenn eine Taste gedrückt wird
            if event.key == pygame.K_BACKSPACE:  # Wenn die Rücktaste gedrückt wird
                rücktaste_gedrückt()  # Funktion für die Rücktaste
            elif event.key == pygame.K_ESCAPE:  # Wenn die Escape Taste gedrückt wird
                programm_läuft = False  # Beende das Programm
            else:  # Wenn eine andere Taste gedrückt wird
                # Check if the key is a number
                if event.unicode.isnumeric():  # Wenn die Taste eine Zahl ist
                    nutzereingabe += event.unicode  # Füge die Zahl der Eingabe hinzu
                    eingabe_ist_primzahl = ist_es_eine_primzahl(int(nutzereingabe))  # Prüfe ob die Eingabe eine Primzahl ist

    if len(nutzereingabe) == 0:  # Wenn die Eingabe leer ist
        mixer.music.set_volume(.1) # Leiser wenn nichts eingegeben ist
        screen.blit(hintergrund_neutral, (0, 0))  # Neutral
    elif eingabe_ist_primzahl:  # Wenn die Eingabe eine Primzahl ist
        mixer.music.set_volume(.1) # Leiser wenn richtig ist
        screen.blit(hintergrund_happy, (0, 0))  # Happy
    else:  # Wenn die Eingabe keine Primzahl ist
        mixer.music.set_volume(.3) # Lauter wenn falsch ist
        screen.blit(hintergrund_sad, (0, 0))  # Sad
    
    pygame.draw.rect(screen, (255, 255, 255), eingabefeld)  # Darstellung des Eingabefeldes

    if eingabe_ist_primzahl:  # Wenn die Eingabe eine Primzahl ist
        pygame.draw.rect(screen, (0, 255, 0), eingabefeld, 5)  # Box grün umranden
    elif len(nutzereingabe) > 0:  # Wenn die Eingabe nicht leer ist
        pygame.draw.rect(screen, (255, 0, 0), eingabefeld, 5)  # Box rot umranden
    else:  # Wenn die Eingabe leer ist
        pygame.draw.rect(screen, (0, 0, 0), eingabefeld, 5) # Box schwarz umranden

    # Text in der Mitte des Eingabefeldes
    font = pygame.font.Font(None, 110)
    text_surface = font.render(nutzereingabe, True, (0, 0, 0))  # Text rendern
    screen.blit(text_surface, (fenster_breite // 2 - text_surface.get_size()[0] // 2, eingabefeld.y + 5))  # Text zeichnen

    # Titel in Rainbow Farben
    font = pygame.font.Font(None, 90)  # Schriftart und Schriftgröße
    # Rainbow Farben
    rainbowColor: tuple[int, int, int] = (
        int(math.sin(pygame.time.get_ticks() / 1000 + 0) * 127 + 128),  # Rainbow Farben (R - Rot)
        int(math.sin(pygame.time.get_ticks() / 1000 + 2) * 127 + 128),  # Rainbow Farben (G - Grün)
        int(math.sin(pygame.time.get_ticks() / 1000 + 4) * 127 + 128))  # Rainbow Farben (B - Blau)
    text_surface = font.render("Ist es eine Primzahl?", True, rainbowColor)  # Text rendern
    screen.blit(text_surface, (fenster_breite // 2 - text_surface.get_size()[0] // 2, fenster_höhe-200))  # Text zeichnen

    pygame.display.flip()  # Zeige den Inhalt des Bildschirms an
    clock.tick(fps)  # Warte bis die Zeit für einen Frame abgelaufen ist


# Main Loop
while programm_läuft:
    bildschirm_zeichnen()  # Zeichne den Bildschirm neu

pygame.quit()  # Beende pygame
