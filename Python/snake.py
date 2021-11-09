# Snake Game
# Alden Dent
# 10/7/21

import pygame
import random

PER_ROW, PER_COLUMN = 12, 10 #int(input("Squares per row: ")), int(input("Squares per column: "))
SQUARE_SIZE = 50
WIDTH, HEIGHT = SQUARE_SIZE*PER_ROW, SQUARE_SIZE*PER_COLUMN
SNAKE_SIZE_OFFSET = 1.5
SNAKE_SIZE = SQUARE_SIZE - 2*SNAKE_SIZE_OFFSET
FOOD_SIZE_OFFSET = SNAKE_SIZE_OFFSET
FOOD_SIZE = SQUARE_SIZE - 2*FOOD_SIZE_OFFSET

WHITE = (255, 255, 255)
FOOD_COLOR = (76, 196, 63)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
TEXT_COLOR = (46, 127, 255)
DEATH_SCREEN_COLOR = BLACK

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)
snake = [(0, PER_COLUMN//2), (1, PER_COLUMN//2), (2, PER_COLUMN//2)]
food = (PER_ROW//2, PER_COLUMN//2)
highScore = 0
X, Y = 0, 1  # Indices for the x and y values in snake a direction
direction = RIGHT
alive = True

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")  # Titles windon "Snake Game"
pygame.font.init()  # Initializes pygame font module
MYFONT = pygame.font.SysFont('Microsoftsansserif', 40)  # Creates font object
clock = pygame.time.Clock()  # Starts a clock
FRAME_LENGTH = 90


def canMove(snake, dir):
    if -1 < snake[-1][X] + direction[X] < PER_ROW and -1 < snake[-1][Y] + direction[Y] < PER_COLUMN:
        if (snake[-1][X] + dir[X], snake[-1][Y] + dir[Y]) not in snake[1:]:
            return True
    return False


def addFood():
    global food, FRAME_LENGTH
    openSquares = [(x, y) for x in range(PER_ROW) for y in range(PER_COLUMN) if (x, y) not in snake]
    if len(snake) < PER_ROW*PER_COLUMN:
        food = openSquares[random.randrange(len(openSquares))]
    #FRAME_LENGTH = FRAME_LENGTH - 5


def drawWin():
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, FOOD_COLOR, pygame.Rect(food[X]*SQUARE_SIZE + FOOD_SIZE_OFFSET, food[Y]*SQUARE_SIZE + FOOD_SIZE_OFFSET, FOOD_SIZE, FOOD_SIZE))
    for index in range(len(snake)):
            brightness = 255 - (255/len(snake))*(index+1)
            color = (255, brightness, brightness)
            pygame.draw.rect(WIN, color, pygame.Rect(snake[index][X]*SQUARE_SIZE + SNAKE_SIZE_OFFSET, snake[index][Y]*SQUARE_SIZE + SNAKE_SIZE_OFFSET, SNAKE_SIZE, SNAKE_SIZE))
    pygame.display.update()


def deathScreen(score):
    WIN.fill(DEATH_SCREEN_COLOR)
    scoreText = MYFONT.render(f"You died with a score of {score}", 1, TEXT_COLOR)
    highScoreText = MYFONT.render(f"Your high-score is {highScore}", 1, TEXT_COLOR)
    instructionsText = MYFONT.render("Press ENTER to play again", 1, TEXT_COLOR)
    WIN.blit(scoreText, (.5*WIDTH - .5*scoreText.get_width(), .3*HEIGHT - .5*scoreText.get_height()))
    WIN.blit(highScoreText, (.5*WIDTH - .5*highScoreText.get_width(), .5*HEIGHT - .5*highScoreText.get_height()))
    WIN.blit(instructionsText, (.5*WIDTH - .5*instructionsText.get_width(), .7*HEIGHT - .5*instructionsText.get_height()))
    pygame.display.update()


def handleMovement():
    if canMove(snake, direction):
            tail = snake[0]
            for index in range(len(snake)):
                    if index < len(snake)-1:
                            snake[index] = snake[index+1]
                    if index == len(snake)-1:
                            snake[index] = (snake[index][X] + direction[X], snake[index][Y] + direction[Y])
            if snake[-1] == food:
                    snake.insert(0, tail)
                    addFood()
    else:
            global alive
            alive = False


def gameLoop():
    global alive, direction
    alive = True
    startGame = False
    while alive:
            nextFrameTime = pygame.time.get_ticks() + FRAME_LENGTH
            oldDirection = direction
            while pygame.time.get_ticks() < nextFrameTime:
                    keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
                    if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
                            pygame.quit()
                            exit()
                    for event in pygame.event.get():  # Quits if window is closed
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()
                    if keys_pressed[pygame.K_LEFT] and not (snake[-1][X]-snake[-2][X], snake[-1][Y]-snake[-2][Y]) == RIGHT and not direction == RIGHT:
                            direction = LEFT
                    if keys_pressed[pygame.K_RIGHT] and not (snake[-1][X]-snake[-2][X], snake[-1][Y]-snake[-2][Y]) == LEFT and not direction == LEFT:
                            direction = RIGHT
                    if keys_pressed[pygame.K_UP] and not (snake[-1][X]-snake[-2][X], snake[-1][Y]-snake[-2][Y]) == DOWN and not direction == DOWN:
                            direction = UP
                    if keys_pressed[pygame.K_DOWN] and not (snake[-1][X]-snake[-2][X], snake[-1][Y]-snake[-2][Y]) == UP and not direction == UP:
                            direction = DOWN
            handleMovement()
            drawWin()

WIN.fill(BLACK)
titleText = MYFONT.render("Snake Game", 1, TEXT_COLOR)
creditText = MYFONT.render("By Alden Dent", 1, TEXT_COLOR)
instructionsText = MYFONT.render("Press ENTER to play", 1, TEXT_COLOR)
WIN.blit(titleText, (.5*WIDTH - .5*titleText.get_width(), .3*HEIGHT - .5*titleText.get_height()))
WIN.blit(creditText, (.5*WIDTH - .5*creditText.get_width(), .5*HEIGHT - .5*creditText.get_height()))
WIN.blit(instructionsText, (.5*WIDTH - .5*instructionsText.get_width(), .7*HEIGHT - .5*instructionsText.get_height()))
pygame.display.update()

while True:
    snake = [(0, PER_COLUMN//2), (1, PER_COLUMN//2), (2, PER_COLUMN//2), (3, PER_COLUMN//2)]
    startingSnakeLen = len(snake)
    direction = RIGHT
    playAgain = False
    while not playAgain:
            keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
            if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
                    pygame.quit()
                    exit()
            for event in pygame.event.get():  # Quits if window is closed
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
            if keys_pressed[pygame.K_RETURN]:
                    playAgain = True
    gameLoop()
    score = len(snake)-startingSnakeLen
    if score > highScore:
        highScore = score
    deathScreen(score)
