import pygame
import random
import sys

pygame.init()

# ---------------- WINDOW ----------------
WIDTH = 1100
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CYBER//BREACH - Password Hacker Game")

clock = pygame.time.Clock()

# ---------------- COLORS ----------------
BLACK = (5, 8, 15)
DARK = (10, 15, 25)
PANEL = (15, 24, 38)

CYAN = (0, 255, 255)
GREEN = (50, 255, 130)
RED = (255, 70, 90)
YELLOW = (255, 220, 80)
PURPLE = (180, 100, 255)

WHITE = (235, 245, 255)
GREY = (130, 145, 160)

# ---------------- FONTS ----------------
title_font = pygame.font.SysFont("consolas", 48, bold=True)
big_font = pygame.font.SysFont("consolas", 32, bold=True)
font = pygame.font.SysFont("consolas", 22)
small_font = pygame.font.SysFont("consolas", 17)

# ---------------- LEVELS ----------------
levels = [
    {
        "name": "TRAINING SERVER",
        "password": "CYBER7",
        "clue": "I am the field that protects computers and networks.",
        "hint": "Think about your degree."
    },

    {
        "name": "FIREWALL SERVER",
        "password": "FIREWALL",
        "clue": "I protect a network by controlling incoming traffic.",
        "hint": "I act like a security barrier."
    },

    {
        "name": "SHADOW SERVER",
        "password": "SHADOW9",
        "clue": "I follow you but disappear when there is no light.",
        "hint": "Look behind you."
    },

    {
        "name": "QUANTUM SERVER",
        "password": "QUANTUM",
        "clue": "I belong to the strange world of advanced physics.",
        "hint": "Think about quantum computers."
    },

    {
        "name": "FINAL SERVER",
        "password": "ZEROCOOL",
        "clue": "A legendary hacker-inspired name. It starts with ZERO.",
        "hint": "ZERO + COOL."
    }
]

# ---------------- GAME VARIABLES ----------------
game_state = "menu"

level = 0
attempts = 5
score = 0

password_input = ""

hint_used = False

time_limit = 40
start_time = 0

message = ""
message_color = WHITE

# ---------------- BACKGROUND PARTICLES ----------------
particles = []

for i in range(100):
    particles.append([
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.randint(1, 3)
    ])


# ==================================================
# FUNCTIONS
# ==================================================

def draw_text(text, font, color, x, y, center=False):

    image = font.render(text, True, color)

    if center:
        x = x - image.get_width() // 2

    screen.blit(image, (x, y))


def draw_background():

    screen.fill(BLACK)

    # Grid
    for x in range(0, WIDTH, 50):
        pygame.draw.line(
            screen,
            (10, 25, 35),
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, 50):
        pygame.draw.line(
            screen,
            (10, 25, 35),
            (0, y),
            (WIDTH, y)
        )

    # Moving particles
    for particle in particles:

        x, y, speed = particle

        pygame.draw.circle(
            screen,
            (15, 80, 90),
            (x, y),
            2
        )

        particle[1] -= speed

        if particle[1] < 0:
            particle[1] = HEIGHT
            particle[0] = random.randint(0, WIDTH)


def draw_panel(x, y, width, height):

    pygame.draw.rect(
        screen,
        PANEL,
        (x, y, width, height),
        border_radius=12
    )

    pygame.draw.rect(
        screen,
        (30, 80, 100),
        (x, y, width, height),
        2,
        border_radius=12
    )


def start_game():

    global game_state
    global level
    global attempts
    global score
    global password_input
    global hint_used
    global start_time
    global message

    game_state = "game"

    level = 0
    attempts = 5
    score = 0

    password_input = ""

    hint_used = False

    message = ""

    start_time = pygame.time.get_ticks()


# ==================================================
# MENU
# ==================================================

def draw_menu():

    draw_background()

    draw_text(
        "CYBER//BREACH",
        title_font,
        CYAN,
        WIDTH // 2,
        120,
        True
    )

    draw_text(
        "PASSWORD INFILTRATION GAME",
        small_font,
        GREY,
        WIDTH // 2,
        180,
        True
    )

    # Lock icon

    pygame.draw.rect(
        screen,
        CYAN,
        (WIDTH // 2 - 35, 270, 70, 55),
        3,
        border_radius=8
    )

    pygame.draw.arc(
        screen,
        CYAN,
        (WIDTH // 2 - 25, 235, 50, 60),
        3.14,
        6.28,
        4
    )

    # Start button

    pygame.draw.rect(
        screen,
        (10, 35, 40),
        (WIDTH // 2 - 180, 400, 360, 70),
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        GREEN,
        (WIDTH // 2 - 180, 400, 360, 70),
        2,
        border_radius=10
    )

    draw_text(
        "[ ENTER ] START BREACH",
        font,
        GREEN,
        WIDTH // 2,
        422,
        True
    )

    draw_text(
        "Solve clues • Crack passwords • Unlock servers",
        small_font,
        GREY,
        WIDTH // 2,
        530,
        True
    )


# ==================================================
# GAME SCREEN
# ==================================================

def draw_game():

    draw_background()

    current_level = levels[level]

    # Header

    draw_text(
        "CYBER//BREACH",
        big_font,
        CYAN,
        40,
        25
    )

    draw_text(
        f"LEVEL {level + 1}/5",
        font,
        GREEN,
        900,
        35
    )

    # Main panel

    draw_panel(
        50,
        100,
        1000,
        500
    )

    # Server name

    draw_text(
        current_level["name"],
        big_font,
        PURPLE,
        90,
        135
    )

    draw_text(
        "TARGET SECURITY STATUS",
        small_font,
        GREY,
        90,
        195
    )

    # Security bars

    for i in range(5):

        color = GREEN if i <= level else (30, 45, 60)

        pygame.draw.rect(
            screen,
            color,
            (90 + i * 45, 225, 32, 10),
            border_radius=5
        )

    # Clue box

    pygame.draw.rect(
        screen,
        DARK,
        (90, 275, 920, 90),
        border_radius=8
    )

    draw_text(
        "CLUE",
        small_font,
        CYAN,
        110,
        290
    )

    draw_text(
        current_level["clue"],
        small_font,
        WHITE,
        110,
        325
    )

    # Hint

    if hint_used:

        pygame.draw.rect(
            screen,
            (35, 30, 50),
            (90, 380, 920, 55),
            border_radius=8
        )

        draw_text(
            "HINT: " + current_level["hint"],
            small_font,
            YELLOW,
            110,
            397
        )

    # Input label

    draw_text(
        "ENTER ACCESS KEY",
        small_font,
        GREY,
        90,
        455
    )

    # Input box

    pygame.draw.rect(
        screen,
        (3, 7, 12),
        (90, 485, 650, 55),
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        CYAN,
        (90, 485, 650, 55),
        2,
        border_radius=8
    )

    draw_text(
        password_input + "_",
        font,
        WHITE,
        110,
        500
    )

    # Attempts

    draw_text(
        f"ATTEMPTS: {attempts}",
        small_font,
        RED if attempts <= 2 else GREEN,
        780,
        490
    )

    # Score

    draw_text(
        f"SCORE: {score}",
        small_font,
        YELLOW,
        780,
        525
    )

    # Timer

    elapsed = (pygame.time.get_ticks() - start_time) // 1000

    remaining = max(
        0,
        time_limit - elapsed
    )

    draw_text(
        f"TIME: {remaining}s",
        small_font,
        RED if remaining <= 10 else CYAN,
        780,
        560
    )

    # Controls

    draw_text(
        "[ H ] HINT",
        small_font,
        GREY,
        90,
        570
    )

    draw_text(
        "[ ENTER ] SUBMIT",
        small_font,
        GREY,
        250,
        570
    )

    # Message

    if message:

        draw_text(
            message,
            small_font,
            message_color,
            WIDTH // 2,
            635,
            True
        )


# ==================================================
# WIN SCREEN
# ==================================================

def draw_win():

    draw_background()

    draw_text(
        "ACCESS GRANTED",
        title_font,
        GREEN,
        WIDTH // 2,
        180,
        True
    )

    draw_text(
        "ALL SECURITY NODES UNLOCKED",
        big_font,
        CYAN,
        WIDTH // 2,
        260,
        True
    )

    draw_text(
        f"FINAL SCORE: {score}",
        big_font,
        YELLOW,
        WIDTH // 2,
        340,
        True
    )

    pygame.draw.rect(
        screen,
        (10, 35, 40),
        (WIDTH // 2 - 180, 450, 360, 65),
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        GREEN,
        (WIDTH // 2 - 180, 450, 360, 65),
        2,
        border_radius=10
    )

    draw_text(
        "[ ENTER ] PLAY AGAIN",
        font,
        GREEN,
        WIDTH // 2,
        470,
        True
    )


# ==================================================
# GAME OVER
# ==================================================

def draw_game_over():

    draw_background()

    draw_text(
        "ACCESS DENIED",
        title_font,
        RED,
        WIDTH // 2,
        180,
        True
    )

    draw_text(
        "SECURITY SYSTEM LOCKED",
        big_font,
        GREY,
        WIDTH // 2,
        260,
        True
    )

    draw_text(
        f"FINAL SCORE: {score}",
        big_font,
        YELLOW,
        WIDTH // 2,
        340,
        True
    )

    pygame.draw.rect(
        screen,
        (40, 15, 20),
        (WIDTH // 2 - 180, 450, 360, 65),
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        RED,
        (WIDTH // 2 - 180, 450, 360, 65),
        2,
        border_radius=10
    )

    draw_text(
        "[ ENTER ] RETRY",
        font,
        RED,
        WIDTH // 2,
        470,
        True
    )


# ==================================================
# MAIN LOOP
# ==================================================

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        # ---------------- MENU ----------------

        if game_state == "menu":

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    start_game()

        # ---------------- GAME ----------------

        elif game_state == "game":

            if event.type == pygame.KEYDOWN:

                # Backspace
                if event.key == pygame.K_BACKSPACE:

                    password_input = password_input[:-1]

                # Hint
                elif event.key == pygame.K_h:

                    hint_used = True

                # Submit
                elif event.key == pygame.K_RETURN:

                    correct_password = levels[level]["password"]

                    if password_input.upper() == correct_password:

                        score += 100

                        if not hint_used:
                            score += 25

                        level += 1

                        if level >= len(levels):

                            game_state = "win"

                        else:

                            attempts = 5
                            password_input = ""
                            hint_used = False

                            start_time = pygame.time.get_ticks()

                            message = "ACCESS GRANTED!"
                            message_color = GREEN

                    else:

                        attempts -= 1

                        password_input = ""

                        message = "ACCESS DENIED!"
                        message_color = RED

                        if attempts <= 0:

                            game_state = "gameover"

                # Letters / numbers
                elif event.unicode.isalnum():

                    if len(password_input) < 20:

                        password_input += event.unicode

        # ---------------- END SCREENS ----------------

        elif game_state == "win":

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    start_game()

        elif game_state == "gameover":

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    start_game()

    # ---------------- TIMER CHECK ----------------

    if game_state == "game":

        elapsed = (pygame.time.get_ticks() - start_time) // 1000

        if elapsed >= time_limit:

            attempts -= 1

            start_time = pygame.time.get_ticks()

            password_input = ""

            message = "TIME EXPIRED!"
            message_color = RED

            if attempts <= 0:

                game_state = "gameover"

    # ---------------- DRAW ----------------

    if game_state == "menu":

        draw_menu()

    elif game_state == "game":

        draw_game()

    elif game_state == "win":

        draw_win()

    elif game_state == "gameover":

        draw_game_over()

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()