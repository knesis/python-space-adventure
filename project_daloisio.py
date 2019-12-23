import random
import sys
import time
import pygame
import pickle
from pygame.locals import *

# Stephen Daloisio - Simon Memory Game - Venus

name = profile_main['name']               # Player Name
score1 = profile_main['score1']           # Score for Asteroid Minigame
score2 = profile_main['score2']           # Score for Simon Minigame
score3 = profile_main['score3']           # Score for Multiple Choice Minigame
score4 = profile_main['score4']           # Score for Minesweeper Minigame
score5 = profile_main['score5']           # Score for Shooting Minigame

frames = 30
width = 720
height = 480
flash_time = 500
flash_pause = 200
button_size = 200
button_spacing = 20
pause_length = 4

# Colors
green = (0, 100, 0)
red = (100, 0, 0)
yellow = (100, 100, 0)
blue = (0, 0, 100)

# Flashing Colors
flash_green = (0, 255, 0)
flash_red = (255, 0, 0)
flash_yellow = (255, 255, 0)
flash_blue = (0, 0, 255)

# Text / Background Colors
white = (255, 255, 255)
black = (0, 0, 0)
background_color = black

# Set Margin Sizes for Formatting
x_margin = int((width - (2 * button_size) - button_spacing) / 2)
y_margin = int((height - (2 * button_size) - button_spacing) / 2)

# Create "Rect's" with Pygame to serve as buttons
green_button = pygame.Rect(x_margin, y_margin, button_size, button_size)
red_button = pygame.Rect(x_margin + button_size + button_spacing, y_margin, button_size, button_size)
yellow_button = pygame.Rect(x_margin, y_margin + button_size + button_spacing, button_size, button_size)
blue_button = pygame.Rect(x_margin + button_size + button_spacing, y_margin + button_size + button_spacing, button_size, button_size)
# Mainloop
def mainloop():
    global framecounter, displaysurface, font_type
    global green_button, red_button, yellow_button, blue_button
    global frames, width, height, flash_time, flash_pause, button_size, button_spacing, pause_length
    global green, red, yellow, blue
    global flash_green, flash_red, flash_yellow, flash_blue
    global white, black, background_color
    global placebuttons, buttonflash, getuserclick, gquit, end_game
    global profile_main, name, score1, score2, score3, score4, score5
    # Set Margin Sizes for Formatting
    x_margin = int((width - (2 * button_size) - button_spacing) / 2)
    y_margin = int((height - (2 * button_size) - button_spacing) / 2)
    import pygame
    import random
    import time
    import pickle
    # Set title, directions, and display
    pygame.init()
    pygame.display.set_caption('Space Command!')
    framecounter = pygame.time.Clock()
    displaysurface = pygame.display.set_mode((width, height))
    font_type = pygame.font.SysFont('monospace.ttf', 18)
    help_surface = font_type.render("Repeat the spaceship's commands by clicking the buttons in order to blast off! You must have a score of atleast 5 to win!", 1, white)
    instr_box = help_surface.get_rect()
    instr_box.topleft = (5, height - 20)
    # Set a blank pattern, level, and score
    pattern = []
    level = 0
    user_input = 0
    score = 0
    no_input = False

    while True:
        button_press = None
        displaysurface.fill(background_color)

        placebuttons()

        score_surface = font_type.render('Score: ' + str(score), 1, white)
        score_box = score_surface.get_rect()
        score_box.topleft = (width - 100, 10)

        displaysurface.blit(score_surface, score_box)
        displaysurface.blit(help_surface, instr_box)

        gquit()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                button_press = getuserclick(mouse_x, mouse_y)

        if not no_input:
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((green, red, yellow, blue)))
            for button in pattern:
                buttonflash(button)
                pygame.time.wait(flash_pause)
            no_input = True
        else:
            try:
                if button_press and (button_press == pattern[level]):
                    buttonflash(button_press)
                    level += 1
                    user_input = time.time()

                    if level == len(pattern):
                        score += 1
                        no_input = False
                        level = 0

                elif (button_press and button_press != pattern[level]) or (level != 0 and time.time() - pause_length > user_input):
                    if score > 5:
                        print("Congrats! You win!")
                        score2 = max(score, score2)
                        nprofile = {'name': name, 'score1': score1, 'score2': score2, 'score3': score3, 'score4': score4,
                                'score5': score5}
                        spath = 'profiles\\' + name + '.p'
                        pickle.dump(nprofile, open(spath, 'wb'))
                        profile_main = nprofile
                        end_game()
                        return
                    else:
                        no_input = False
                        score = 0
                        pattern = []
            except IndexError as e:
                print "Cosmic Error. Please restart."
                end_game()
                return
        pygame.display.update()
        framecounter.tick(frames)


#Functions
def placebuttons():
    import pygame
    global green_button, red_button, yellow_button, blue_button
    global green, red, yellow, blue
    global flash_green, flash_red, flash_yellow, flash_blue
    global white, black, background_color
    pygame.draw.rect(displaysurface, green, green_button)
    pygame.draw.rect(displaysurface, red, red_button)
    pygame.draw.rect(displaysurface, yellow, yellow_button)
    pygame.draw.rect(displaysurface, blue, blue_button)


def getuserclick(x, y):
    global green_button, red_button, yellow_button, blue_button
    global green, red, yellow, blue
    if green_button.collidepoint( (x, y) ):
        return green
    elif red_button.collidepoint( (x, y) ):
        return red
    elif yellow_button.collidepoint( (x, y) ):
        return yellow
    elif blue_button.collidepoint( (x, y) ):
        return blue

    return None


def buttonflash(color, flash_speed=75):
    global green_button, red_button, yellow_button, blue_button
    global green, red, yellow, blue
    import random
    import pygame
    if color == green:
        color_flash = flash_green
        rectangle = green_button
    elif color == red:
        color_flash = flash_red
        rectangle = red_button
    elif color == yellow:
        color_flash = flash_yellow
        rectangle = yellow_button
    elif color == blue:
        color_flash = flash_blue
        rectangle = blue_button

    original_flash_color = displaysurface.copy()
    surface_flash = pygame.Surface((button_size, button_size))
    surface_flash = surface_flash.convert_alpha()
    r, g, b = color_flash
    for start, end, step in ((0, 255, 1), (255, 0, -1)):
        for alpha in range(start, end, flash_speed * step):
            gquit()
            displaysurface.blit(original_flash_color, (0, 0))
            surface_flash.fill((r, g, b, alpha))
            displaysurface.blit(surface_flash, rectangle.topleft)
            pygame.display.update()
            framecounter.tick(frames)
    displaysurface.blit(original_flash_color, (0, 0))


def gquit():
    import pygame

    for event in pygame.event.get(pygame.QUIT):
        end_game()
    for event in pygame.event.get(pygame.KEYUP):
        if event.key == pygame.K_ESCAPE:
            end_game()
    #pygame.event.post(event)


def end_game():
    import pygame
    pygame.display.quit()
    #pygame.quit()

mainloop()

