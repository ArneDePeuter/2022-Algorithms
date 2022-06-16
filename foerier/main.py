import pygame
from math import cos, sin, radians

# screen setup
screen_width = 1000
screen_height = 1000

class Circle:
    def __init__(self, x, y, radius, v, angle):
        self.x = x
        self.y = y
        self.radius = radius
        self.v = v
        self.angle = angle

def move_circles(circles, angles):
    for index, angle in enumerate(angles):
        circle = circles[index]
        angles[index] += circle.v
        if index == len(circles)-1:
            break
    return angles

def draw_function(win,circles,dots, graph):
    if not(graph):
        win.fill((0, 0, 0))
        for i, circle in enumerate(circles):
            pygame.draw.circle(win, (255,255,255), (circle.x, circle.y), circle.radius, width=1)
            if i == len(circles)-1:
                pygame.draw.circle(win, (255,255,0), (circle.x+circle.radius*cos(radians(circle.angle)), circle.y+circle.radius*sin(radians(circle.angle))), 5)
                dots.append((circle.x+circle.radius*cos(radians(circle.angle)), circle.y+circle.radius*sin(radians(circle.angle))))
                if len(dots)>500:
                    dots.remove(dots[0])

        for dotx, doty in dots:
            pygame.draw.circle(win, (255,0,0), (dotx,doty), 1)
    else:
        win.fill((255,255,255))
        for i, dot in enumerate(dots):
            dotx,doty = dot
            pygame.draw.circle(win, (0,0,0), (i, doty), 3)
        pygame.display.update()

    pygame.display.update()
    return dots

def main(win):
    clock = pygame.time.Clock()

    #setup
    innercircle_angle = 0
    circle1_angle = 0
    circle2_angle = 0
    circle3_angle = 0
    circle4_angle = 0
    circle5_angle = 0
    circle6_angle = 0
    circle7_angle = 0
    circle8_angle = 0
    circle9_angle = 0
    angles = [innercircle_angle, circle1_angle, circle2_angle, circle3_angle, circle4_angle, circle5_angle, circle6_angle, circle7_angle, circle8_angle, circle9_angle]

    dots = list()
    run = True
    graph = False
    while run:
        clock.tick(60)

        #setup                                                                                                                                                  radius  velocity
        innercircle = Circle(screen_width/2, screen_height/2,                                                                                                   10,     1,      angles[0])
        circle1 = Circle(innercircle.x+innercircle.radius*cos(radians(innercircle.angle)), innercircle.y+innercircle.radius*sin(radians(innercircle.angle)),    20,      6,      angles[1])
        circle2 = Circle(circle1.x + circle1.radius*cos(radians(circle1.angle)), circle1.y + circle1.radius*sin(radians(circle1.angle)),                        40,      -4,      angles[2])
        circle3 = Circle(circle2.x + circle2.radius*cos(radians(circle2.angle)), circle2.y + circle2.radius*sin(radians(circle2.angle)),                        20,      -8,      angles[3])
        circle4 = Circle(circle3.x + circle3.radius*cos(radians(circle3.angle)), circle3.y + circle3.radius*sin(radians(circle3.angle)),                        40,     -4,     angles[4])
        circle5 = Circle(circle4.x + circle4.radius*cos(radians(circle4.angle)), circle4.y + circle4.radius*sin(radians(circle4.angle)),                        60,      4,      angles[5])
        circle6 = Circle(circle5.x + circle5.radius*cos(radians(circle5.angle)), circle5.y + circle5.radius*sin(radians(circle5.angle)),                        40,      -5,      angles[6])
        circle7 = Circle(circle6.x + circle6.radius*cos(radians(circle6.angle)), circle6.y + circle6.radius*sin(radians(circle6.angle)),                        30,      4,      angles[7])
        circle8 = Circle(circle7.x + circle7.radius*cos(radians(circle7.angle)), circle7.y + circle7.radius*sin(radians(circle7.angle)),                        40,      6,      angles[8])
        circle9 = Circle(circle8.x + circle8.radius*cos(radians(circle8.angle)), circle8.y + circle8.radius*sin(radians(circle8.angle)),                        40,      5,      angles[9])

        circles = [innercircle, circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9]

        #move and draw
        if not graph:
            angles = move_circles(circles, angles)
        dots = draw_function(win,circles,dots, graph)

        #quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    graph = True
                elif event.key == pygame.K_RIGHT:
                    graph = False

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('foerier')
main(win)
