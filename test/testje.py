import pygame
import random
pygame.init()

# screen setup
screen_width = 1000
screen_height = 1000

#vars
smallfont = pygame.font.SysFont('comicsans', 20, bold=True)
beginpoint_BL = (10, screen_height-10)
beginpoint_BR = (screen_width-10, screen_height-10)
beginpoint_TR = (screen_height-10, 10)
beginpoint_TL = (10, 10)
firstpoint = (900,910)

corners = [beginpoint_TL, beginpoint_TR, beginpoint_BL, beginpoint_BR]
dots = [beginpoint_BR, beginpoint_TR, beginpoint_TL, beginpoint_BL, firstpoint]
radius = 1

def new_point(cornerpoint, firstpoint):
    cornerx, cornery = cornerpoint
    pointx, pointy = firstpoint
    return (cornerx+pointx)/2, (cornery+pointy)/2

def draw_function(win, dots, percentage):
    win.fill((0, 0, 0))
    percent = smallfont.render('Percentage: {}%'.format(round(percentage)), 1, (255,255,255))
    win.blit(percent, (0,0))

    for dotx, doty in dots:
        pygame.draw.circle(win, (255,255,255), (dotx, doty), radius)
    pygame.display.update()

def main(win, firstpoint):
    uitgevoerd = 0
    iterations = 100000

    run = True
    while run:
        percentage = (uitgevoerd/iterations)*100
        draw_function(win, dots, percentage)

        if uitgevoerd <= iterations:
            firstpoint = new_point(random.choice(corners), firstpoint)
            if firstpoint not in dots:
                dots.append(firstpoint)
            uitgevoerd += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('iteration')
main(win, firstpoint)
