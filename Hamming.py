import pygame
import sys
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN)

pygame.init()

# basic setup
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

# main menu


def main_menu():
    running = True
    arialFont = pygame.font.SysFont('arial', 25)
    printButton = pygame.Rect(550, 100, 170, 100)  # draw red button
    eraseButton = pygame.Rect(550, 400, 170, 100)  # draw blue button
    printHelloWorld = False

    while running:

        # Flags
        click = False

        # Events
        for event in pygame.event.get():  # check events here
            # leave application
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:  # check for left mouse click
                click = True

        mx, my = pygame.mouse.get_pos()

        if printButton.collidepoint((mx, my)) and click:
            printHelloWorld = True
        elif eraseButton.collidepoint((mx, my)) and click:
            printHelloWorld = False

        # Drawing and updating
        screen.fill((255, 255, 255))  # white background
        pygame.draw.rect(screen, (255, 50, 50), printButton)  # red button
        draw_text("Print", arialFont, (0, 0, 0), screen, 600, 110)
        pygame.draw.rect(screen, (50, 50, 255), eraseButton)  # blue button
        draw_text("Erase", arialFont, (0, 0, 0), screen, 600, 410)

        if printHelloWorld:
            draw_text("Hello World!", arialFont, (0, 0, 0), screen, 580, 310)

        pygame.display.flip()
        clock.tick(14)

# basic function to draw text


def draw_text(text, font, color, surface, x, y):

    if text == "":
        return
    text = font.render(text, 1, color)
    surface.blit(text, (x, y))


main_menu()
