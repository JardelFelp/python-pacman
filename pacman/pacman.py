import pygame
from character import Pacman
from scenario import Scenario

# Screen dimensions
SCREEN_SIZE = 800

# Colors
BLACK = (0, 0, 0)

# Circle characteristics
RADIUS = 30

# Move
COLUMNS_AMOUNT = 20

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pacman = Pacman(screen, COLUMNS_AMOUNT)
scenario = Scenario(screen, COLUMNS_AMOUNT)

while True:
    # Calculate rules
    pacman.calculate()

    # Paint PACKMAN
    screen.fill(BLACK)
    scenario.generate_maze()
    pacman.paint()
    pygame.display.update()
    pygame.time.delay(10)

    # Check Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman.turn_up()
            elif event.key == pygame.K_DOWN:
                pacman.turn_down()
            elif event.key == pygame.K_LEFT:
                pacman.turn_left()
            elif event.key == pygame.K_RIGHT:
                pacman.turn_right()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pacman.stop_vertical()
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pacman.stop_horizontal()
