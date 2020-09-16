import pygame
import math

#  !configure window
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HangMan")
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
hangman_status = 0
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
letters = []

for i in range(26):
    letters.append([chr(65+i), True])
# !guessing word
WORD = "DEVELOPING"
guessed = []
FONT_GUESS = pygame.font.SysFont("comicsans", 60)
guessX = 350
guessY = 250
FONT_RESULT = pygame.font.SysFont('comicsans', 100)
guessed_length = 1

for i in range(1, len(WORD)-1):
    for j in range(0, i-1):
        if WORD[i] != WORD[j]:
            guessed_length += 1

# !draw function called inside the game loop


def draw():
    global mouse_Y, mouse_X, letters, hangman_status, running
    screen.fill(WHITE)
    screen.blit(hangman[hangman_status], (100, 140))

    for i in range(26):
        cirX = initialX + (2*RADIUS+GAP)*(i % 13)
        cirY = initialY + (2*RADIUS+GAP)*(i//13)
        ltr, visible = letters[i]

        if visible:
            pygame.draw.circle(screen, BLACK, (cirX, cirY), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            screen.blit(text, (cirX-9, cirY-12))

            distance = math.sqrt(math.pow((cirX-mouse_X), 2) +
                                 math.pow((cirY - mouse_Y), 2))
            if distance < RADIUS:
                letters[i][1] = False

                if ltr in WORD:
                    guessed.append(ltr)
                else:
                    hangman_status += 1

                if hangman_status == 6:
                    text_lose = FONT_RESULT.render('You Lose', 1, (200, 0, 0))
                    screen.blit(text_lose, (300, 200))
                    running = False


# !game loop
while running:
    clock.tick(FPS)

    draw()

    for letter in WORD:

        if letter in guessed:
            text_guess = FONT_GUESS.render(letter, 1, BLACK)
            screen.blit(text_guess, (guessX+15, guessY))

        else:
            text_guess = FONT_GUESS.render("_", 1, BLACK)
            screen.blit(text_guess, (guessX+20, guessY))
        guessX += 40

    guessX = 350

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # mouse clicked coordinates
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_X, mouse_Y = pygame.mouse.get_pos()

    pygame.display.update()
pygame.quit()
#
