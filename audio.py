import pygame

class Audio:
    def __init__(self,game):
        self.game=game
        self.mixer=pygame.mixer.init()
        self.losing_audio=pygame.mixer.Sound("audio/hit.ogg")
        self.playing_audio=pygame.mixer.Sound("audio/swoosh.ogg")
        self.point_audio=pygame.mixer.Sound("audio/point.ogg")
        self.jump_audio=pygame.mixer.Sound("audio/wing.ogg")

    def play_losing(self):
        self.losing_audio.play()
    
    def play_playing(self):
        self.playing_audio.play()

    def play_point(self):
        self.point_audio.play()

    def  play_jump(self):
        self.jump_audio.play()