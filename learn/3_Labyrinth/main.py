import pygame
import asyncio
import logging

from functions import kollision

logger = logging.getLogger("pygame")

pygame.init()
window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()


async def main():
    """
    Pygame Tutorial 2: Bewegung mit Tasten
    """

    run = True

    # Bewegbares Objekt aus einem Bild
    obj = pygame.image.load("images/pacman.png")
    # Größe verändern
    obj = pygame.transform.scale(obj, (50, 50))
    # Position des Objekts
    position = obj.get_rect(center=(190, 145))
    # Rotierte Version des Objekts (anfangs unverändert)
    obj_rotiert = obj
    # obj.get_rect center=window.get_rect().center
    # Wand
    wand1 = pygame.Rect(155, 110, 70, 10)
    wand2 = pygame.Rect(155, 110, 10, 110)
    wand3 = pygame.Rect(215, 110, 10, 60)
    wand4 = pygame.Rect(155, 270, 70, 10)
    wand5 = pygame.Rect(215, 170, 70, 10)

    wände = [wand1, wand2, wand3, wand4, wand5]

    # Keine Taste gedrückt
    taste = ""

    # Ist ein Tasten-Event erfolgt
    tastenwechsel = False

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                # Get the name of the pressed key
                taste = pygame.key.name(event.key)
                tastenwechsel = True
                logger.info(f"Taste: {taste}")

        # Blauer Hintergrund
        window.fill((20, 20, 100))

        # Aufgabe 1:
        # Abfragen, ob Tasten gedrückt sind
        # "left", "right", "up", "down"
        # Logik wenn Taste "right" ist, erhöhe position.x um 1

        if taste == "right":
            position.x = position.x + 1

        if taste == "left":
            position.x = position.x - 1

        if taste == "up":
            position.y = position.y - 1

        if taste == "down":
            position.y = position.y + 1

        # Aufgabe 2:
        # Zeichne die Wand als rotes Rechteck
        for w in wände:
            pygame.draw.rect(window, (200, 0, 0), w)
        # Prüfe mit der Funktion kollision, ob obj die Wand berührt
        # Nutze dafür die Funktion kollisition(object1, object2) <- oben auskommentiert
        eine_kollision = False
        for w in wände:
            if kollision(position, w):
                eine_kollision = True
        if eine_kollision:

            if taste == "right":
                position.x = position.x - 1

            if taste == "left":
                position.x = position.x + 1

            if taste == "up":
                position.y = position.y + 1

            if taste == "down":
                position.y = position.y - 1

        # Wenn eine Kollision erkannt wird, bewege das obj zurück und stoppe die
        # Bewegung

        # Aufgabe 2:
        # Je nach Richtung soll das Objekt gedreht werden
        # wenn ein Tastenwechsel erfolgt ist
        # Nutze dazu obj_rotiert und tastenwechsel (auskommentierte Befehle)

        if tastenwechsel:

            if taste == "right":
                obj_rotiert = pygame.transform.rotate(obj, 0)

            if taste == "left":
                obj_rotiert = pygame.transform.rotate(obj, 180)

            if taste == "up":
                obj_rotiert = pygame.transform.rotate(obj, 90)

            if taste == "down":
                obj_rotiert = pygame.transform.rotate(obj, 270)

        # Zeige obj an der aktuellen Position
        window.blit(obj_rotiert, position)

        tastenwechsel = False

        pygame.display.flip()
        await asyncio.sleep(0)  # required for pygbag

    pygame.quit()
    exit()


# This is the program entry point:
asyncio.run(main())
