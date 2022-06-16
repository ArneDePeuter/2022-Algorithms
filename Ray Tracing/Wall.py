import pygame

class Wall:
    def __init__(self, a, b):
        self.ax = a[0]
        self.ay = a[1]
        self.bx = b[0]
        self.by = b[1]

    def show(self,win):
        pygame.draw.line(win, (255,255,255), (self.ax, self.ay), (self.bx, self.by))