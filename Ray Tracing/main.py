from Wall import Wall
from Point import Point
import math, pygame, numpy, random,time
pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)

#screens setup
screenwidth = 1000
screenheigth = 1000

mapwidht = 400
mapheight = 400

field_width = screenwidth-mapwidht
field_height = screenheigth

win = pygame.display.set_mode((screenwidth,screenheigth))

def get_walls(amount):
    walls = []
    #extra walls
    for x in range(amount):
        walls.append(Wall([random.randint(0,mapwidht),random.randint(0,mapheight)], [random.randint(0,mapwidht),random.randint(0,mapheight)]))

    #border
    walls.append(Wall([0,0], [mapwidht,0]))
    walls.append(Wall([0,0], [0,mapheight]))
    walls.append(Wall([mapwidht,0], [mapwidht,mapheight]))
    walls.append(Wall([0,mapheight], [mapwidht,mapheight]))
    return walls

def draw_screen(walls, point, scene):
    win.fill(black)
    for wall in walls:
        wall.show(win)
    point.show(win)

    w = field_width/len(scene)
    maxdist = round((field_width**2+mapheight**2)**0.5)
    maxdist = 500
    for i,dist in enumerate(scene):
        rgb = (dist/maxdist)*255
        inv_rgb = abs(rgb-255)
        height = abs(dist-mapheight)
        pygame.draw.rect(win, (inv_rgb, inv_rgb, inv_rgb), (mapwidht+i*w,field_height/2-height/2, w+1, height))
    pygame.display.update()

def get_input(point):
    run = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        point.start -= 1
        point.stop -= 1
        changed = True
        point.get_rays()
    elif keys[pygame.K_RIGHT]:
        point.start += 1
        point.stop += 1
        changed = True
        point.get_rays()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    return run, point

def main():
    pygame.display.set_caption("Ray casting")

    walls = get_walls(4)
    point = Point(0,60, mapwidht, mapheight)

    scene = []

    win.fill(black)
    pygame.draw.rect(win, (255,0,0), (0,0,mapwidht, mapheight),1)
    pygame.display.update()

    time.sleep(4)

    run = True
    while run:
        scene = point.update(walls, scene, mapwidht, mapheight)
        draw_screen(walls, point, scene)
        run,point = get_input(point)
    quit()

if __name__ == '__main__':
    main()