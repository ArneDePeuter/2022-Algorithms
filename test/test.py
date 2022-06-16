import pygame
from math import dist, atan, cos, sin,pi, radians
import time
import time
pygame.init()

# screen setup
screen_width = 1920
screen_height = 600

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.dist = dist(self.p1, self.p2)
        self.middle = (self.p1[0]+self.p2[0])/2,(self.p1[1]+self.p2[1])/2

def add_line(lines):
    newlines = []
    for line in lines:
        oorsprong = line.p1[0], line.p1[1]
        uiterste = line.p2[0], line.p2[1]

        #angle = -atan((line.p2[1]-line.p1[1])/(line.p2[0]-line.p1[0]))
        #lo = oorsprong[0]+(line.dist/3)*cos(angle), oorsprong[1]-(line.dist/3)*sin(angle)
        #ro = uiterste[0]-(line.dist/3)*cos(angle), uiterste[1]+(line.dist/3)*sin(angle)
        #toppunt = line.middle[0]-(line.dist/3)*sin(angle), line.middle[1]-(line.dist/3)*cos(angle)

        angle1 = 60
        angle2 = 60
        angle3 = 60
        angle4 = 60
        lo = oorsprong[0]+(uiterste[0]-oorsprong[0])/3,  oorsprong[1]+(uiterste[1]-oorsprong[1])/3
        ro = oorsprong[0]+2*(uiterste[0]-oorsprong[0])/3,  oorsprong[1]+2*(uiterste[1]-oorsprong[1])/3
        tro = ro[0]-lo[0], ro[1]-lo[1]
        rotatiero = tro[0]*cos(radians(angle1))-tro[1]*sin(radians(angle2)), tro[0]*sin(radians(angle3)) + tro[1]*cos(radians(angle4))
        toppunt = rotatiero[0]+lo[0], rotatiero[1]+lo[1]

        newlines.append(Line(oorsprong, lo))
        newlines.append(Line(lo, toppunt))
        newlines.append(Line(toppunt, ro))
        newlines.append(Line(ro, uiterste))
    return newlines

def draw_function(win, lines):
    win.fill((0, 0, 0))
    for line in lines:
        pygame.draw.line(win, (255,255,255), line.p1, line.p2)
    pygame.display.update()

def main(win):
    run = True

    firstline = Line((0, screen_height / 2), (screen_width, screen_height / 2))
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