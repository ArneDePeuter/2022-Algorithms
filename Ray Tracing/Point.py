import pygame
import math
from Ray import Ray

class Point:
    def __init__(self, start, stop, mapwidth, mapheight):
        self.x = mapwidth/2
        self.y = mapheight/2
        self.start = start
        self.stop = stop
        self.get_rays()

    def show(self,win):
        for ray in self.rays:
            ray.show(win)
        pygame.draw.circle(win, (255,0,0), (self.x, self.y), 4)

    def get_rays(self):
        self.rays = []
        for angle in range(self.start,self.stop):
            x = math.cos(math.radians(angle))
            y = math.sin(math.radians(angle))
            ray = Ray(150, 500, x, y)
            if ray not in self.rays:
                self.rays.append(ray)

    def get_shortest(self, x1, y1, points):
        lengths = []
        for point in points:
            if point != None:
                lengths.append(((x1 - point[0]) ** 2 + (y1 - point[1]) ** 2) ** 0.5)
            else:
                lengths.append(math.inf)
        return points[lengths.index(min(lengths))], min(lengths)

    def update(self, walls, prev_scene, mapwidht, mapheight):
        if not(0<pygame.mouse.get_pos()[0]<mapwidht and 0<pygame.mouse.get_pos()[1]<mapheight): #if mouse outside of range
            return prev_scene

        scene = []
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        for ray in self.rays:
            ray.x1 = self.x
            ray.y1 = self.y
            points = []
            for wall in walls:
                points.append(ray.cast(wall))
            point, dist = self.get_shortest(ray.x1, ray.y1, points)
            if point != None:
                ray.x2 = point[0]
                ray.y2 = point[1]
                scene.append(dist)
        return scene