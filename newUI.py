import pygame
import time
import random

pygame.init()

display_width = 1024
display_height = 576

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0, 255, 0)

blue_bg = (7,6,196)

block_color = (53,115,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Text RPG')
clock = pygame.time.Clock()

pause = False

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Text RPG", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",774,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        draw_player_area()
        draw_enemy_area()
        draw_log_area()
        pygame.display.update()
        clock.tick(60)


def draw_enemy_area():
    pygame.draw.rect(gameDisplay, bright_red, pygame.Rect(10, 10, 1004, 100), 3)

def draw_player_area():
    #Background
    pygame.draw.rect(gameDisplay, blue_bg, pygame.Rect(10, 400, 1004, 166), 0)
    #Borders
    pygame.draw.rect(gameDisplay, white, pygame.Rect(10, 400, 502, 166), 3)
    pygame.draw.rect(gameDisplay, white, pygame.Rect(512, 400, 502, 166), 3)

def draw_log_area():
    pygame.draw.rect(gameDisplay, white, pygame.Rect(10, 120, 1004, 270), 3)

game_intro()
game_loop()
pygame.quit()
quit()