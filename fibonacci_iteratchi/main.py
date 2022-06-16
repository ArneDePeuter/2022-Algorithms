import copy
import pygame as pygame
import time
pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)

#screen
screenwidht = 500
screenheight = 500
win = pygame.display.set_mode((screenwidht,screenheight))

resize = 0.001

class Line:
    def __init__(self, size, start, dir):
        self.size = size
        self.start = start
        self.dir = dir
        self.next_dir = 'unknown'
        self.end = ('none', 'none')
        self.get_end()

    def draw(self):
        pygame.draw.line(win, red, self.start, self.end)

    def get_end(self):
        if self.dir == 'TL-BR':
            self.next_dir = 'BL-TR'
            self.end = self.start[0]+self.size*resize, self.start[1]+self.size*resize
        elif self.dir == 'BL-TR':
            self.next_dir = 'BR-TL'
            self.end = self.start[0]+self.size*resize, self.start[1]-self.size*resize
        elif self.dir == 'BR-TL':
            self.next_dir = 'TR-BL'
            self.end = self.start[0]-self.size*resize, self.start[1]-self.size*resize
        elif self.dir == 'TR-BL':
            self.next_dir = 'TL-BR'
            self.end = self.start[0]-self.size*resize, self.start[1]+self.size*resize

def init_list(start):
    lines = [Line(0,start,'TR-BL')]
    lines.append(Line(1, lines[0].end, lines[0].next_dir))
    return lines

def add_fibonacci(lines):
    newsize = lines[-1].size + lines[-2].size
    lines.append(Line(newsize, lines[-1].end, lines[-1].next_dir))
    return lines

def draw_screen(lines):
    win.fill(black)
    for line in lines:
        line.draw()
    pygame.display.update()

def get_input():
    run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    return run

def main():
    pygame.display.set_caption("Pygame Default")
    run = True

    lines = init_list((screenwidht/2,screenheight/2))

    while run:

        lines = add_fibonacci(lines)
        draw_screen(lines)
        run = get_input()

    quit()

if __name__ == '__main__':
    main()