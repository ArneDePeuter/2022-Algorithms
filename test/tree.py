import pygame
import random
from math import sin, cos, radians, dist
pygame.init()

# screen setup
screen_width = 1000
screen_height = 1000

#vars
factor = 0.6

smallfont = pygame.font.SysFont('comicsans', 20, bold=True)
percent = smallfont.render('Percentage: {}%', 1, (255, 255, 255))

firstlength = 200
firstline = [(screen_width/2,screen_height),(screen_width/2, screen_height-firstlength)]
lines = [firstline]


def add_line(lines, angle,uitgevoerd):
    point1, point2 = lines[-1]
    point2x, point2y = point2

    distance = dist(point1, point2)*factor

    point2 = point2x+distance*cos(radians(angle-90)), point2y+distance*sin(radians(angle-90))
    point1 = point2x, point2y

    iterations = 5

    if uitgevoerd<iterations:
        lines, angle, uitgevoerd = add_line(lines, angle, uitgevoerd)
        uitgevoerd+=1
    else:
        uitgevoerd = 0
        return lines, angle, uitgevoerd

def draw_function(win, lines):
    win.fill((0, 0, 0))
    for p1, p2 in lines:
        print(p1, p2)
        pygame.draw.line(win, (255,255,255), p1, p2)
    pygame.display.update()

def main(win):
    clock = pygame.time.Clock()
    angle = 60

    uitgevoerd = 0
    getekend = 0
    branches = 1

    run = True
    while run:
        draw_function(win, lines)

        if getekend<branches:
            line, angle, uitgevoerd = add_line(lines, angle, uitgevoerd)
            lines.append(line)
            getekend+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('iteration')
main(win)