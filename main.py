import pygame
from constants import *
from world import *
from menu import *
from flappy import *
from texts import *
import filemanagement
from audio import *
pygame.display.set_caption("Flappy Bird Remake")
pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
class Main():
    def __init__(self):
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        self.playing=False
        self.losing=False
        self.keys=pygame.key.get_pressed()
        self.main_time=pygame.time.get_ticks()
        self.new_time=None
        self.deltatime=self.deltaTime()
        self.record=0

    def deltaTime(self):
        self.new_time=pygame.time.get_ticks()
        deltatime=(self.new_time-self.main_time)/1000
        self.main_time=self.new_time
        return deltatime


    def main(self):
        self.files=filemanagement.Points(self)
        self.record=self.files.read()
        self.playing=False
        self.losing=False
        self.audio=Audio(self)
        self.texts=Texts(self)
        self.world=World(self)
        self.menu=Menu(self)
        self.flappy=Flappy(self)
        self.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                self.menu.play_event()
                self.flappy.fly_input()




    def update(self):
        while True:
            self.deltatime=self.deltaTime()
            self.check_events()
            self.world.world_update()
            self.menu.menu_update()
            self.flappy.update()
            self.texts.update_text()
#            clock.tick(FPS)


            # Update the display
            pygame.display.flip()  # Update the full display Surface to the screen


if __name__=='__main__':
    main_game=Main()
    main_game.main()
