import pygame
from pygame.locals import *
class Plane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.plane1 = pygame.image.load("images/plane1.png").convert_alpha()
        self.plane2 = pygame.image.load("images/plane2.png").convert_alpha()
        self.plane = self.plane1
        self.mask = pygame.mask.from_surface(self.plane)
        self.death_spirits = list()
        self.spirit1 = pygame.image.load("images/plane_blowup_n1.png").convert_alpha()
        self.spirit2 = pygame.image.load("images/plane_blowup_n2.png").convert_alpha()
        self.spirit3 = pygame.image.load("images/plane_blowup_n3.png").convert_alpha()
        self.death_spirits.extend([self.spirit1, self.spirit2, self.spirit3])
        self.spirits_index = 0
        self.swich = True
        self.count = 3
        self.scaler = self.count
        self.rect = self.plane1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 10
        self.set_position()
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0
    def moveDown(self):
        if self.rect.bottom < self.height - 50:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom =self.height - 50
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width
    def move(self):
        self.key_pressed = pygame.key.get_pressed()
        if self.key_pressed[K_w] or self.key_pressed[K_UP]:
            self.moveUp()
        if self.key_pressed[K_s] or self.key_pressed[K_DOWN]:
            self.moveDown()
        if self.key_pressed[K_a] or self.key_pressed[K_LEFT]:
            self.moveLeft()
        if self.key_pressed[K_d] or self.key_pressed[K_RIGHT]:
            self.moveRight()
        # 控制图片切换
        if self.swich:
            self.plane = self.plane1
        else:
            self.plane = self.plane2
        if self.scaler == 0:
            self.swich = not self.swich
            self.scaler = self.count
        self.scaler -= 1
    def set_position(self):
        self.survival = True
        self.spirits_index = 0
        self.rect.left = (self.width - self.rect.width) / 2
        self.rect.top = self.height - self.rect.height - 50
