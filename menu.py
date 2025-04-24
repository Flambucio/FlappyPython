import pygame
from constants import *
import time

class Menu:
    def __init__(self,game):
        self.game=game
        self.play=pygame.image.load("sprites/message.png")
        self.play=pygame.transform.scale(self.play,(WIDTH,HEIGHT))
        self.over=pygame.image.load("sprites/gameover.png")
        self.over=pygame.transform.scale(self.over,(WIDTH/2,HEIGHT/12)) 
    def menu_update(self):
        if not self.game.losing and not self.game.playing:
            self.game.screen.blit(self.play,(0,0))
            self.game.texts.render_record()
        self.check_game_over()
    def play_event(self):
        if not self.game.losing and not self.game.playing:
            self.game.playing=True
            self.game.audio.play_playing()
    
    def game_over(self):
        self.game.audio.play_losing()
        self.game.flappy.render()
        for tubes in self.game.world.tubes.list_tubes:
            tubes.render_tubes()
        self.game.world.render_ground()
        self.game.texts.render_points()
        self.game.texts.render_record(700)
        self.game.screen.blit(self.over,(WIDTH/4,400))
        if self.game.texts.points>self.game.record:
            self.game.record=self.game.texts.points
            self.game.files.write()
        pygame.display.flip()
        time.sleep(2)
        self.game.main()

    def check_game_over(self):
        if self.game.losing and not self.game.playing:
            self.game_over()


        
