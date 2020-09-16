import pygame
import math


# ?The length of the guessed is hardcorded need to fix it , other is all good

#  !configure window and some variables
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
    # ! True determines the showing of the letter on the screen
    letters.append([chr(65+i), True])

# !guessing word
# ! if you want to change the word , you also need to change the hardcoded wining condition
WORD = "DEVELOPING"
guessed = []
FONT_GUESS = pygame.font.SysFont("comicsans", 60)
guessX = 350
guessY = 250
FONT_RESULT = pygame.font.SysFont('comicsans', 100)
FONT_HEADER = pygame.font.SysFont('comicsans', 50)
FONT_FOOTER = pygame.font.SysFont('comicsans', 20)
# set = {}

# for i in range(len(WORD)-1):
#     set.put(WORD[i])


# !draw function called inside the game loop


def draw():
    global mouse_Y, mouse_X, letters, hangman_status, running
    screen.fill(WHITE)
# !putting header and footer and hangman image on the screen
    text_header = FONT_HEADER.render("Guess The Word", 1, (33, 88, 33))
    screen.blit(text_header, (250, 40))

    text_footer = FONT_FOOTER.render("developer: Amrit kaphle", 1, (0, 0, 29))
    screen.blit(text_footer, (310, 540))

    screen.blit(hangman[hangman_status], (100, 140))
#!
#! displaying visible letters on the screen
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
#!
#! inserting the correct clicked word into the guessed array else changing the hangman image
                if ltr in WORD:
                    guessed.append(ltr)
                else:
                    hangman_status += 1
#!
#! showing the losing message
                if hangman_status == 6:
                    screen.blit(hangman[hangman_status], (100, 140))
                    text_lose = FONT_RESULT.render('You Lose', 1, (200, 0, 0))
                    screen.blit(text_lose, (300, 200))
                    running = False


# !game loop
while running:
    clock.tick(FPS)

    draw()

    # !check if all letter are guessed, wining condition
    if len(guessed) == 9:
        text_win = FONT_RESULT.render("You Win", 1, (0, 200, 0))
        screen.blit(text_win, (300, 200))
        running = False
#!
#! if clicked letter is correct, rendering the letters else rendering _ .
    for letter in WORD:
        if letter in guessed:
            text_guess = FONT_GUESS.render(letter, 1, BLACK)
            screen.blit(text_guess, (guessX+15, guessY))

        else:
            text_guess = FONT_GUESS.render("_", 1, BLACK)
            screen.blit(text_guess, (guessX+20, guessY))
        guessX += 40

    guessX = 350
#!

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #! mouse clicked coordinates
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_X, mouse_Y = pygame.mouse.get_pos()

    pygame.display.update()
pygame.quit()
#
