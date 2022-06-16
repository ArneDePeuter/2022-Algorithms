import pygame
from math import dist, atan, cos, sin,pi, radians
import time
import time
pygame.init()

# screen setup
screen_width = 1000
screen_height = 1000

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.dist = dist(self.p1, self.p2)
        self.middle = (self.p1[0]+self.p2[0])/2,(self.p1[1]+self.p2[1])/2

def add_line(lines):
    newlines = []
    for line in lines:
        oorsprong = line.p1
        uiterste = line.p2

        if line.p1[0]>line.p2[0]:
            oorsprong = line.p2
            uiterste = line.p1
        if line.p1[1]==line.p2[1]:
            lo = oorsprong[0] + line.dist/3, oorsprong[1]
            lb = lo[0], lo[1]- line.dist/3
            rb = lb[0]+line.dist/3, lb[1]
            ro = rb[0], rb[1]+line.dist/3
        elif line.p1[1]<line.p2[1]: #BO
            lo = oorsprong[0], oorsprong[1] + line.dist / 3
            lb = lo[0]+line.dist/3, lo[1]
            rb = lb[0], lb[1]+line.dist/3
            ro = rb[0]-line.dist/3,rb[1]
        elif line.p1[1]>line.p2[1]: #OB
            lo = oorsprong[0], oorsprong[1] - line.dist / 3
            lb = lo[0]-line.dist/3, lo[1]
            rb = lb[0], lb[1]-line.dist/3
            ro = rb[0]+line.dist/3,rb[1]

        newlines.append(Line(oorsprong, lo))
        newlines.append(Line(lo, lb))
        newlines.append(Line(lb, rb))
        newlines.append(Line(rb, ro))
        newlines.append(Line(ro, uiterste))
    return newlines

def draw_function(win, lines):
    win.fill((0, 0, 0))
    for line in lines:
        pygame.draw.line(win, (255,255,255), line.p1, line.p2)
    pygame.display.update()

def main(win):
    run = True

    firstline = Line((0, screen_height -100 ), (screen_width, screen_height-100))
    lines = [firstline]

    while run:
        draw_function(win, lines)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if pygame.K_SPACE:
                    lines = add_line(lines)

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('iteration')
main(win)