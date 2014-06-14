#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame,sys,os,random
from pygame.locals import *
#some constant
#direction
GO_UP = 1
GO_RIGHT = 2
GO_DOWN = 3
GO_LEFT = 4
#how many point at per axis
X_POINT_COUNT = 60
Y_POINT_COUNT = 60
#resolution 
X_RESOLUTION = 600
Y_RESOLUTION = 600
#point resolution
X_POINT_RESOLUTION = X_RESOLUTION / X_POINT_COUNT
Y_POINT_RESOLUTION = Y_RESOLUTION / Y_POINT_COUNT
#title of window
CAPTION = "Lazy Snake"
#max frame per second
FPS = 60
#speed of snake move
SPEED = 50
TIME_EVENTID = 30
LOSE_EVENTID = 29
GAINPOINT_EVENTID = 28
#image
SNAKE_POINT_PATH = os.path.join(sys.path[0],"Snake_Point.png")
SNAKE_SURFACE = pygame.image.load(SNAKE_POINT_PATH)
#ALLOW_SCANCODE
UP_ARROW = 72 #200
RIGHT_ARROW = 77 #205
DOWN_ARROW = 80 #208
LEFT_ARROW = 75 #203
#Score you got
Score = 0
class Point:
    _direction = None
    _x = 0
    _y = 0
    _rect = None
    _snake_surf = SNAKE_SURFACE
    def __init__(self,surf,x = 30,y = 30):
        self._x = x
        self._y = y
        self._rect = pygame.Rect((self._x*X_POINT_RESOLUTION,self._y*Y_POINT_RESOLUTION),(10,10))
        
        self._direction = GO_RIGHT
    def render(self):
        return self._rect,self._snake_surf
    #calculate next position by direction
    def move(self):
        new_x,new_y = self.get_nextxy()
        self._x = new_x % X_POINT_COUNT
        self._y = new_y % Y_POINT_COUNT
        self._rect.left = self._x * X_POINT_RESOLUTION
        self._rect.top = self._y * Y_POINT_RESOLUTION                
    def turn(self,direction):
        if (abs(self._direction - direction) != 2):
            self._direction = direction
    def set_direction(self,direction):
        self._direction = direction
    def get_direction(self):
        return self._direction
    def get_xy(self):
        return self._x,self._y
    def get_nextxy(self):
        ret_y,ret_x = self._y,self._x
        if self._direction == GO_UP:
            ret_y = self._y - 1
        elif self._direction == GO_LEFT:
            ret_x = self._x - 1
        elif self._direction == GO_DOWN:
            ret_y = self._y + 1
        elif self._direction == GO_RIGHT:
            ret_x = self._x + 1
        return (ret_x,ret_y)

class Snake:
    def __init__(self):
        self._points = []
        self._randpoint = None
        self._turned = False#a flag snake turned,it's important
        self._moving = True
        self.newrand()
        self._points.insert(len(self._points),Point(SNAKE_SURFACE))
        self._points.insert(len(self._points),Point(SNAKE_SURFACE,31,30))
        self._points.insert(len(self._points),Point(SNAKE_SURFACE,32,30))
        self._points.insert(len(self._points),Point(SNAKE_SURFACE,33,30))
    def newrand(self):
        no_repeat = False
        while not no_repeat:
            no_repeat = True
            rand_x = random.randint(0,X_POINT_COUNT - 1)
            rand_y = random.randint(0,Y_POINT_COUNT - 1)
            for point in self._points:
                point_x,point_y = point.get_xy()
                if (point_x,point_y) == (rand_x,rand_y):
                    no_repeat = False
                    break
        self._randpoint = Point(SNAKE_SURFACE,rand_x,rand_y)
    def render(self):
        surf = pygame.Surface((X_RESOLUTION,Y_RESOLUTION))
        for point in self._points:
            point_rect,point_surf = point.render()
            surf.blit(point_surf,point_rect)
        #rend random point
        point_rect,point_surf = self._randpoint.render()
        surf.blit(point_surf,point_rect)
        
        return surf.get_rect(),surf
    def addPoint(self,point):
        point.set_direction(self._points[-1].get_direction()) #change new point direction
        self._points.insert(len(self._points),point)
    def move(self):
        if self._moving:
            len_points = len(self._points)
            head = self._points[-1]
            next_xy = head.get_nextxy()
            rand_xy = self._randpoint.get_xy()
            #detect lose
            for point in self._points:
                if (next_xy == point.get_xy()):#lose                
                    pygame.event.post(pygame.event.Event(LOSE_EVENTID))#raise lose event
                    self._moving = False#stop moving
                    return 
            #detect rand_point
            if (next_xy == rand_xy):#gain a point
                self.addPoint(self._randpoint)
                self.newrand()
                pygame.event.post(pygame.event.Event(GAINPOINT_EVENTID))#raise gain point event
            else:#do not gain a point,continue move
                for i in range(0,len_points):
                    self._points[i].move()
                    if (i != len_points - 1):#follow the next point direction
                        self._points[i].set_direction(self._points[i + 1].get_direction())
            self._turned = False
    def turn(self,direction):
        #由于蛇的移动是由计时器触发的（计时器的间隔最文件开头SPEED定义），如果在SPEED的间隔内
        #蛇头转动了两次的话，会导致蛇头脱离,因此定义这个flag
        if not self._turned:
            self._points[-1].turn(direction)
            self._turned = True
    
def main():
    running = 1
    display_flags = DOUBLEBUF
    pygame.init()
    global Score
    clock = pygame.time.Clock()
    if pygame.display.mode_ok((X_RESOLUTION,Y_RESOLUTION),display_flags):
        screen = pygame.display.set_mode((X_RESOLUTION,Y_RESOLUTION),display_flags)
    pygame.display.set_caption("%s - Score:%i" % (CAPTION,Score))
    pygame.time.set_timer(TIME_EVENTID,SPEED)
    
    #testcode
    snake = Snake()
    
    #background surface
    background = pygame.Surface((X_RESOLUTION,Y_RESOLUTION))
    background.fill((0,0,0))
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0
            elif event.type == TIME_EVENTID:
                snake.move()
            elif event.type == KEYDOWN:
                #change direction
                if event.scancode == UP_ARROW:
                    snake.turn(GO_UP)
                elif event.scancode == RIGHT_ARROW:
                    snake.turn(GO_RIGHT)
                elif event.scancode == DOWN_ARROW:
                    snake.turn(GO_DOWN)
                elif event.scancode == LEFT_ARROW:
                    snake.turn(GO_LEFT)
            elif event.type == GAINPOINT_EVENTID:
                Score += 10
                pygame.display.set_caption("%s - Score:%i" % (CAPTION,Score))
            elif event.type == LOSE_EVENTID:
                print "Game Lose"
            else:
                pass
        #test code
        rect,surf = snake.render()
        screen.blit(background,(0,0))
        screen.blit(surf,rect)
        pygame.display.update()
        clock.tick(FPS)#set max fps
if __name__ == "__main__":
    main()