import pygame
import random


WIDTH = 600
RADIUS = WIDTH // 2
FONT_SIZE = 16


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)


def main():
    # Setup screen and font
    screen, statsFont = setup()

    ptsInsideCircle = 0
    totalPts = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the circle
        pygame.draw.circle(screen, Colors.WHITE, (RADIUS, RADIUS), RADIUS, 1)

        # Increase total pts every frame
        totalPts += 1

        # Draw a new point and check if it is inside the circle
        ptsInsideCircle += addNewPoint(screen)

        # Draw total pts, pts inisde circle and estimated value of PI
        drawStats(screen, statsFont, totalPts, ptsInsideCircle)

        # Flip the screen
        pygame.display.flip()


def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Monte Carlo Simulation for Pi")

    pygame.font.init()
    statsFont = pygame.font.SysFont('Roboto', FONT_SIZE)

    return screen, statsFont


def addNewPoint(screen):
    posX = random.randint(0, WIDTH)
    posY = random.randint(0, WIDTH)

    color = Colors.RED
    isPointInside = 0
    if isPointInsideCircle(posX, posY):
        color = Colors.GREEN
        isPointInside = 1

    screen.set_at((posX, posY), color)
    return isPointInside


def isPointInsideCircle(x, y):
    return ((y - RADIUS) ** 2 + (x - RADIUS) ** 2) < RADIUS ** 2


def drawStats(screen, statsFont, totalPts, ptsInsideCircle):
    totalPtsText = createTextSurface(f"Total Points : {totalPts}", statsFont)
    ptsInsideCircleText = createTextSurface(
        f"Points Inside Circle : {ptsInsideCircle}", statsFont)
    piText = createTextSurface(
        f"Pi : {round(4 * ptsInsideCircle / totalPts, 4)}", statsFont)

    screen.blit(ptsInsideCircleText, (0, 0))
    screen.blit(totalPtsText, (0, FONT_SIZE))
    screen.blit(piText, (0, 2 * FONT_SIZE))


def createTextSurface(text, statsFont):
    return statsFont.render(text, True, Colors.BLACK, Colors.WHITE)


if __name__ == "__main__":
    main()
