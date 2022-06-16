import pygame

class Ray:
    def __init__(self, x, y, dir_x, dir_y):
        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y
        self.dir_x = dir_x
        self.dir_y = dir_y

    def show(self, win):
        pygame.draw.line(win, (255,255,255), (self.x1, self.y1), (self.x2, self.y2))

    def cast(self, wall):
        #https://en.wikipedia.org/wiki/Line–line_intersection
        x1 = wall.ax
        y1 = wall.ay
        x2 = wall.bx
        y2 = wall.by
        x3 = self.x1
        y3 = self.y1
        x4 = self.x1 + self.dir_x
        y4 = self.y1 + self.dir_y

        den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        if den == 0:
            return
        t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den
        u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den
        if t>0 and t<1 and u>0:
            x = x1+t*(x2-x1)
            y = y1+t*(y2-y1)
            return [x,y]
        else:
            return