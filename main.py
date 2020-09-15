import pygame
import math

#  !configure window
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("hangMan")
running = True
FPS = 60
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
mouse_X = 0
mouse_Y = 0
#

# !hangmanImg load
hangman = []
hangman_status = 6
for i in range(7):
    img = pygame.image.load('images/hangman'+str(i) + '.png')
    hangman.append(img)

# !all about circle and the letters
cirX = 40
cirY = 400
initialX = 40
initialY = 400
RADIUS = 20
GAP = 20
LETTER_FONT = pygame.font.SysFont('comicsans', 40)

# !draw function called inside the game loop


def draw():
    global mouse_Y, mouse_X
    screen.fill(WHITE)
    screen.blit(hangman[hangman_status], (100, 140))

    for i in range(26):
        cirX = initialX + (2*RADIUS+GAP)*(i % 13)
        cirY = initialY + (2*RADIUS+GAP)*(i//13)
        pygame.draw.circle(screen, BLACK, (cirX, cirY), RADIUS, 3)

        ltr = chr(65 + i)
        text = LETTER_FONT.render(ltr, 1, BLACK)
        screen.blit(text, (cirX-9, cirY-12))

        distance = math.sqrt(math.pow((cirX-mouse_X), 2) +
                             math.pow((cirY - mouse_Y), 2))
        if distance < RADIUS:
            print(ltr)
            pygame.draw.circle(screen, WHITE, (cirX, cirY), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, WHITE)
            screen.blit(text, (cirX-9, cirY-12))


# !game loop
while running:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # mouse clicked coordinates
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_X, mouse_Y = pygame.mouse.get_pos()

    pygame.display.update()
pygame.quit()
#
