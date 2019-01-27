import pygame
import time
import random
from colors import *
from scrollLog import *

pygame.init()

display_width = 1024
display_height = 576

gameDisplay: pygame.Surface = pygame.display.set_mode(
    (display_width, display_height))
pygame.display.set_caption('Text RPG')
clock = pygame.time.Clock()

pause = False

default_font_color = white

multi_Line_surface: pygame.Surface = pygame.Surface((990, 260))
logAreaRect = pygame.Rect(10, 120, 1004, 270)
multi_Line_surface_rect = pygame.Rect(20, 130, 985, 256)

log = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5", "Line 6", "Line 7", "Line 8", "Line 9", "Line 10", "Line 11", "Line 12", "Line 13", "Line 14", "Line 15",
       "Line 16", "Line 17", "Line 18", "Line 19", "Line 20", "Line 21", "Line 22", "Line 23", "Line 24", "Line 25", "Line 26", "Line 27", "Line 28", "Line 29", "Line 30"]


scroll_position = 0
max_line_display = 15
log_display_frame = []


def text_objects(text, font, font_color):
    textSurface = font.render(text, True, font_color)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText, default_font_color)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def display_text(msg, color, rect: pygame.Rect):
    smallText: pygame.font.Font = pygame.font.SysFont("comicsansms", 10)
    textSurf, textRect = text_objects(msg, smallText, color)
    textRect.center = ((rect.left+(rect.width/2)), (rect.top+(rect.height/2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False


def paused():

    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText, default_font_color)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects(
            "Text RPG", largeText, default_font_color)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 774, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    global scroll_position
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    gameExit = False

    while not gameExit:
        gameDisplay.fill(black)
        draw_player_area()
        draw_enemy_area()
        draw_log_area()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_ESCAPE:
            #         pause = True
            #         paused()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 5:
                    print("Scrolled down")
                    if(scroll_position + max_line_display < len(log)):
                        scroll_position += 1
                if event.button == 4:
                    print("Scrolled up")
                    if(scroll_position > 0):
                        scroll_position -= 1

        pygame.display.update()
        clock.tick(60)


def draw_enemy_area():
    pygame.draw.rect(gameDisplay, bright_red,
                     pygame.Rect(10, 10, 1004, 100), 3)


def draw_player_area():
    # Background
    pygame.draw.rect(gameDisplay, blue_bg, pygame.Rect(10, 400, 1004, 166), 0)
    # Borders
    pygame.draw.rect(gameDisplay, white, pygame.Rect(10, 400, 502, 166), 3)
    pygame.draw.rect(gameDisplay, white, pygame.Rect(512, 400, 502, 166), 3)


def draw_log_area():
    global multi_Line_surface
    logRect: pygame.Rect = pygame.draw.rect(
        gameDisplay, white, logAreaRect, 3)
    # display_text("Over the break\nNew Line", default_font_color, logRect)
    smallText: pygame.font.Font = pygame.font.SysFont("Consolas", 16)

    # text: str = "Over the break\nN\nN\nN\nN\nN\nN\nN\nN\nN\nN\nN"
    text = scroll_text(log, scroll_position, max_line_display)
    multi_Line_surface = multiLineSurface(
        text, smallText, multi_Line_surface_rect, white, blue_bg)
    gameDisplay.blit(multi_Line_surface, multi_Line_surface_rect)

# def draw_log_scrollbar():
#     if (len(log) > max_line_display):


class TextRectException:
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message


def multiLineSurface(string, font, rect, fontColour, BGColour, justification=0) -> pygame.Surface:
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Parameters
    ----------
    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rect style giving the size of the surface requested.
    fontColour - a three-byte tuple of the rgb value of the
             text color. ex (0, 0, 0) = BLACK
    BGColour - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                1 horizontally centered
                2 right-justified

    Returns
    -------
    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """

    finalLines = []
    requestedLines = string.splitlines()
    # Create a series of lines that will fit on the provided
    # rectangle.
    for requestedLine in requestedLines:
        if font.size(requestedLine)[0] > rect.width:
            words = requestedLine.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException(
                        "The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulatedLine = ""
            for word in words:
                testLine = accumulatedLine + word + " "
                # Build the line while the words fit.
                if font.size(testLine)[0] < rect.width:
                    accumulatedLine = testLine
                else:
                    finalLines.append(accumulatedLine)
                    accumulatedLine = word + " "
            finalLines.append(accumulatedLine)
        else:
            finalLines.append(requestedLine)

    # Let's try to write the text out on the surface.
    surface = pygame.Surface(rect.size)
    surface.fill(BGColour)
    accumulatedHeight = 0
    for line in finalLines:
        if accumulatedHeight + font.size(line)[1] >= rect.height:
            raise TextRectException(
                "Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            tempSurface = font.render(line, 1, fontColour)
        if justification == 0:
            surface.blit(tempSurface, (0, accumulatedHeight))
        elif justification == 1:
            surface.blit(
                tempSurface, ((rect.width - tempSurface.get_width()) / 2, accumulatedHeight))
        elif justification == 2:
            surface.blit(tempSurface, (rect.width -
                                       tempSurface.get_width(), accumulatedHeight))
        else:
            raise TextRectException(
                "Invalid justification argument: " + str(justification))
        accumulatedHeight += font.size(line)[1]
    return surface


game_intro()
game_loop()
pygame.quit()
quit()
