from constants import *
import pygame

class Texts:
    def __init__(self,game):
        self.game=game
        self.path="sprites/ka1.ttf"
        self.font=pygame.font.Font(self.path,60)
        self.text_record=f"record: {self.game.record}"
        self.points=-1
        self.text_points=f"{self.points-1}"

    def render_points(self):
        self.text_points=f"{self.points}"
        if self.game.playing or self.game.losing:
            if self.points < 0:
                text=self.font.render("0",True,"white")
            else:        
                text=self.font.render(self.text_points,True,"white")
            self.game.screen.blit(text,(WIDTH/2-30,100))
    
    def update_text(self):
        self.render_points()
    
    def render_record(self,y=200):
        text=self.font.render(self.text_record,True,"white")
        self.game.screen.blit(text,(WIDTH/4-60,y))



