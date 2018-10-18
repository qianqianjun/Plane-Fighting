import pygame
from random import *
class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.bomb=pygame.image.load("images/ufo.png")
        self.mask=pygame.mask.from_surface(self.bomb)
        self.rect=self.bomb.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.set_position()
        self.speed=1
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.survival=False

    def set_position(self):
        self.survival=True
        self.rect.left=randint(0,self.width-self.rect.width)
        self.rect.bottom=-100