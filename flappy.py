from constants import *
import pygame

class Flappy:
    def __init__(self,game):
        self.game=game
        self.downflap=pygame.image.load("sprites/yellowbird-downflap.png")
        self.midflap=pygame.image.load("sprites/yellowbird-midflap.png")
        self.upflap=pygame.image.load("sprites/yellowbird-upflap.png")
        self.downflap=pygame.transform.scale(self.downflap,(70,50))
        self.midflap=pygame.transform.scale(self.midflap,(70,50))
        self.upflap=pygame.transform.scale(self.upflap,(70,50))
        self.images_list=[self.downflap,self.midflap,self.upflap]
        self.index=0
        self.flappy=self.images_list[self.index]
        self._unedited_flappy_rect=self.flappy.get_rect()
        self.flappy_rect=pygame.Rect(self._unedited_flappy_rect.x+5,self._unedited_flappy_rect.y+5,
                                     self._unedited_flappy_rect.width-10,self._unedited_flappy_rect.height-10)
        self.jump_progress=0
        self.jumping=False
        self.y=600
        self.animation_speed=0.1
        self.gravity_speed=0.5
        self.can_fall=True

    def fly_input(self):
        if self.game.playing and not self.game.losing:
            self.jumping=True
            self.jump_progress=JUMP_SPEED
            self.game.audio.play_jump()

    def fly(self):
        if self.jumping and self.game.playing and not self.game.losing:
            self.y-=self.jump_progress
            self.jump_progress*=JUMP_FACTOR

            if self.jump_progress<0.1:
                self.jumping=False

    
    def gravity(self):
        if self.game.playing and not self.game.losing:
            if not self.jumping and self.can_fall:# self.y>500 and not
                self.gravity_speed=GRAVITY*self.gravity_speed
                self.y+=self.gravity_speed
            else:
                self.gravity_speed=0.5

    def update_rect(self):
        self.flappy_rect.topleft=(200,self.y)
        

    def render(self):
        self.flappy_rect.topleft=(200,self.y)
        if self.game.playing or self.game.losing:
            self.index+=self.animation_speed
            if self.index>len(self.images_list):
                self.index=0
            self.game.screen.blit(self.images_list[int(self.index)],(250,self.y))
        elif self.game.losing and not self.game.playing:
            self.game.screen.blit(self.images_list[int(self.index)],(250,self.y))

    def update(self):

   
        self.gravity()
        self.fly()
        self.update_rect()
        self.collision()
        self.render()

    def collision(self):
        if self.y>750:
            self.can_fall=False
        else:
            self.can_fall=True
        if self.game.playing and not self.game.losing:
            for tubes in self.game.world.tubes.list_tubes:
                if self.flappy_rect.colliderect(tubes.rect_down) or self.flappy_rect.colliderect(tubes.rect_up):
                    self.game.playing=False
                    self.game.losing=True




            