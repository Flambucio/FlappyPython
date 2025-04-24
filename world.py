import pygame
import filemanagement as filem
from constants import *
import random

class World():
    def __init__(self,game):
        self.game=game
        self.background=pygame.image.load("sprites/background.png")
        self.background=pygame.transform.scale(self.background,(WIDTH,HEIGHT))
        self.ground=pygame.image.load('sprites/base.png')
        self.ground=pygame.transform.scale(self.ground,(800,400))
        self.ground_x=-50
        self.ground_speed=200
        self.tubes=Tubes(game)
        
    def render_ground(self):
        self.game.screen.blit(self.ground,(self.ground_x,800))

    def world_update(self):
        self.game.screen.blit(self.background,(0,0))
        if self.game.playing:
            self.tubes.update()
            self.ground_movement()
            self.render_ground()
    def ground_movement(self):
        self.ground_x-=self.ground_speed*self.game.deltatime
        if self.ground_x< -200:
            self.ground_x=-27
        
class Tubes():
    def __init__(self,game):
        self.game=game
        self.ground_speed=200
        self.tubex=600
        self.tubey=500+random.randint(-200,100)
        self.tubedown=pygame.image.load("sprites/pipe-green.png")
        self.tubedown=pygame.transform.scale(self.tubedown,(100,600))
        self.tubeup=pygame.transform.rotate(self.tubedown,180)
        self.tubeup=pygame.transform.scale(self.tubeup,(100,600))
        self.spawn_interval=2000
        self.main_spawn_time=pygame.time.get_ticks()
        self.current_time=None
        self.list_tubes=[]
        self.rect_down=self.tubedown.get_rect()
        self.rect_up=self.tubeup.get_rect()
        self.offset_down=100
        self.offset_up=-800
        self.diff=self.difficulty()

    def render_tubes(self):
        self.game.screen.blit(self.tubedown,(self.tubex,self.tubey+self.offset_down))
        self.game.screen.blit(self.tubeup,(self.tubex,self.tubey+self.offset_up))
    def update_collision(self):
        self.rect_down.topleft=(self.tubex,self.tubey+self.offset_down)
        self.rect_up.topleft=(self.tubex,self.tubey+self.offset_up)
    def tube_movement(self):
        self.tubex-=self.ground_speed*self.game.deltatime

    def spawn(self):
        self.current_time=pygame.time.get_ticks()
        if self.current_time-self.main_spawn_time>self.spawn_interval:
            self.game.texts.points+=1
            if self.game.texts.points>0:
                self.game.audio.play_point()
            self.main_spawn_time=self.current_time
            new_tube=Tubes(self.game)
            self.list_tubes.append(new_tube)

    def difficulty(self):
        if self.game.texts.points>10 and self.game.texts.points<50:
            self.offset_down+=random.randint(-30,30)
            self.offset_up+=random.randint(-30,30)
        if self.game.texts.points>50:
            self.offset_down+=random.randint(-50,50)
            self.offset_up+=random.randint(-50,50)
        for i in range(self.game.texts.points):
            if self.ground_speed<500:
                self.ground_speed+=5
            if self.spawn_interval>1000:
                self.spawn_interval-=10
        self.new_offset=int(self.game.texts.points/5)
        self.offset_down-=self.new_offset
        self.offset_up+=self.new_offset
        





    def update(self):
        self.spawn()
        for tubes in self.list_tubes:
            tubes.tube_movement()
            tubes.update_collision()
            tubes.render_tubes()

            if tubes.tubex<-200:
                self.list_tubes.remove(tubes)





    



