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

originalW = 990
originalH = 720
scaleX = fenster_breite / originalW
scaleY = fenster_höhe / originalH

hintergrund = pygame.image.load("parts/without.png")  # Lade das Bild
hintergrund = pygame.transform.scale(hintergrund, (fenster_breite, fenster_höhe))  # Skaliere das Bild

eyebrowL = pygame.image.load("parts/left.png")  # Lade das Bild
eyebrowL = pygame.transform.scale(eyebrowL, (eyebrowL.get_width() * scaleX, eyebrowL.get_height() * scaleY))  # Skaliere das Bild um den gleichen Faktor wie das Hintergrundbild
eyebrowL_position = {
    "neutral": (.5, .16, 0),
    "sad": (.5, .18, -5),
    "happy": (.5, .16, 20),
    "current": (0, 0, 0)
}
eyebrowL_position["current"] = eyebrowL_position["neutral"]

eyebrowR = pygame.image.load("parts/right.png")  # Lade das Bild
eyebrowR = pygame.transform.scale(eyebrowR, (eyebrowR.get_width() * scaleX, eyebrowR.get_height() * scaleY))  # Skaliere das Bild um den gleichen Faktor wie das Hintergrundbild
eyebrowR_position = {
    "neutral": (.58, .17, 0),
    "sad": (.58, .15, -15),
    "happy": (.58, .17, -40),
    "current": (0, 0, 0)
}
eyebrowR_position["current"] = eyebrowR_position["neutral"]

mouth = pygame.image.load("parts/mouth.png")  # Lade das Bild
mouth = pygame.transform.scale(mouth, (mouth.get_width() * scaleX, mouth.get_height() * scaleY))  # Skaliere das Bild um den gleichen Faktor wie das Hintergrundbild
mouth_position = {
    "neutral": (.54, .335, 0),
    "sad": (.54, .34, 180),
    "happy": (.55, .34, 0),
    "current": (0, 0, 0)
}
mouth_position["current"] = mouth_position["neutral"]

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
    global programm_läuft, nutzereingabe, eingabe_ist_primzahl, eingabefeld, hintergrund, clock, screen  # Globale Variablen
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

    screen.blit(hintergrund, (0, 0))  # Neutral
    
    pygame.draw.rect(screen, (255, 255, 255), eingabefeld)  # Darstellung des Eingabefeldes

    if eingabe_ist_primzahl:  # Wenn die Eingabe eine Primzahl ist
        pygame.draw.rect(screen, (0, 255, 0), eingabefeld, 5)  # Box grün umranden
    elif len(nutzereingabe) > 0:  # Wenn die Eingabe nicht leer ist
        pygame.draw.rect(screen, (255, 0, 0), eingabefeld, 5)  # Box rot umranden
    else:  # Wenn die Eingabe leer ist
        pygame.draw.rect(screen, (0, 0, 0), eingabefeld, 5) # Box schwarz umranden

    # Augenbrauen anzeigen (mit easing)
    state: str = "neutral" # 0 = neutral, 1 = Primzahl, 2 = Keine Primzahl
    if eingabe_ist_primzahl:
        state = "happy"
    elif len(nutzereingabe) > 0:
        state = "sad"
    # state wird später geändert aktuell statisch
    # Links
    eyebrowL_position["current"] = (eyebrowL_position["current"][0] + (eyebrowL_position[state][0] - eyebrowL_position["current"][0]) * 0.1, # X
                                    eyebrowL_position["current"][1] + (eyebrowL_position[state][1] - eyebrowL_position["current"][1]) * 0.1, # Y
                                    eyebrowL_position["current"][2] + (eyebrowL_position[state][2] - eyebrowL_position["current"][2]) * 0.1) # Rotation
    
    rotatedL = pygame.transform.rotate(eyebrowL, eyebrowL_position["current"][2]) # Rotiere das Bild
    screen.blit(rotatedL, (eyebrowL_position["current"][0] * fenster_breite, eyebrowL_position["current"][1] * fenster_höhe))

    # Rechts
    eyebrowR_position["current"] = (eyebrowR_position["current"][0] + (eyebrowR_position[state][0] - eyebrowR_position["current"][0]) * 0.1, # X
                                    eyebrowR_position["current"][1] + (eyebrowR_position[state][1] - eyebrowR_position["current"][1]) * 0.1, # Y
                                    eyebrowR_position["current"][2] + (eyebrowR_position[state][2] - eyebrowR_position["current"][2]) * 0.1) # Rotation
    
    rotatedR = pygame.transform.rotate(eyebrowR, eyebrowR_position["current"][2]) # Rotiere das Bild
    screen.blit(rotatedR, (eyebrowR_position["current"][0] * fenster_breite, eyebrowR_position["current"][1] * fenster_höhe))

    # Mund anzeigen (mit easing)
    mouth_position["current"] = (mouth_position["current"][0] + (mouth_position[state][0] - mouth_position["current"][0]) * 0.1, # X
                                 mouth_position["current"][1] + (mouth_position[state][1] - mouth_position["current"][1]) * 0.1, # Y
                                 mouth_position["current"][2] + (mouth_position[state][2] - mouth_position["current"][2]) * 0.1) # Rotation
    rotatedM = pygame.transform.rotate(mouth, mouth_position["current"][2]) # Rotiere das Bild
    screen.blit(rotatedM, (mouth_position["current"][0] * fenster_breite, mouth_position["current"][1] * fenster_höhe))

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
