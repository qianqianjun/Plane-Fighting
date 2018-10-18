import pygame
from random import *
#pygame.sprite.Sprite是pygame的一个游戏对象的基类,继承可以很方便的操游戏对象。
class MiniEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        #必须调用sprite的构造函数来进行初始化操作：
        pygame.sprite.Sprite.__init__(self)
        #加载图片素材：
        self.enemy1=pygame.image.load("images/enemy1.png").convert_alpha()
        self.enemy=self.enemy1
        #获取敌机的区域位置：
        self.mask=pygame.mask.from_surface(self.enemy)
        #设置精灵：
        self.death_spirit=list()
        #加载精灵素材：
        self.spirit1 = pygame.image.load("images/enemy1_down1.png").convert_alpha()
        self.spirit2 = pygame.image.load("images/enemy1_down2.png").convert_alpha()
        self.spirit3 = pygame.image.load("images/enemy1_down3.png").convert_alpha()
        self.spirit4 = pygame.image.load("images/enemy1_down4.png").convert_alpha()
        #加到精灵列表中：
        self.death_spirit.extend([self.spirit1,self.spirit2,self.spirit3,self.spirit4])
        #设置精灵列表播放下标
        self.spirit_index=0
        #敌机尺寸
        self.rect=self.enemy1.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        #敌机速度：
        self.speed=2
        #初始化位置：
        self.set_position()
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.set_position()
    #设置敌机的初始位置：
    def set_position(self):
        self.survival=True
        self.spirit_index=0
        self.rect.left=randint(0,self.width-self.rect.width)
        self.rect.top=randint(-3*self.height,0)

#中型敌机类：
class MediumEnemy(pygame.sprite.Sprite):
    hp=5
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        #加载素材
        self.enemy2=pygame.image.load("images/enemy2.png").convert_alpha()
        self.enemy=self.enemy2
        #加载击中的素材
        self.enemy_hit=pygame.image.load("images/enemy2_hit.png").convert_alpha()
        #设置是否被击中的参数
        self.hit=False
        #获取敌机的实际位置
        self.mask=pygame.mask.from_surface(self.enemy)
        #设置精灵：
        self.death_spirits=list()
        self.spirit1=pygame.image.load("images/enemy2_down1.png").convert_alpha()
        self.spirit2=pygame.image.load("images/enemy2_down2.png").convert_alpha()
        self.spirit3=pygame.image.load("images/enemy2_down3.png").convert_alpha()
        self.spirit4=pygame.image.load("images/enemy2_down4.png").convert_alpha()
        self.death_spirits.extend([self.spirit1,self.spirit2,self.spirit3,self.spirit4])
        self.spirits_index=0
        self.rect=self.enemy2.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.speed=1.5
        self.set_position()
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.set_position()
    def set_position(self):
        self.survival=True
        self.hp=MediumEnemy.hp
        self.spirits_index=0
        self.rect.left=randint(0,self.width-self.rect.width)
        self.rect.top=randint(-5*self.height,-self.height)

# 大型敌机类
class LargeEnemy(pygame.sprite.Sprite):
    hp = 15
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.enemy3_n1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.enemy3_n2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.enemy = self.enemy3_n1
        self.enemy_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()
        self.hit = False
        self.mask = pygame.mask.from_surface(self.enemy)
        self.death_spirits = list()
        self.spirit1 = pygame.image.load("images/enemy3_down1.png").convert_alpha()
        self.spirit2 = pygame.image.load("images/enemy3_down2.png").convert_alpha()
        self.spirit3 = pygame.image.load("images/enemy3_down3.png").convert_alpha()
        self.spirit4 = pygame.image.load("images/enemy3_down4.png").convert_alpha()
        self.spirit5 = pygame.image.load("images/enemy3_down5.png").convert_alpha()
        self.spirit6 = pygame.image.load("images/enemy3_down6.png").convert_alpha()
        self.death_spirits.extend([self.spirit1, self.spirit2, self.spirit3, self.spirit4, self.spirit5, self.spirit6])
        self.spirits_index = 0
        self.switch = True
        self.count = 5
        self.scaler = self.count
        self.rect = self.enemy3_n1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.set_position()
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.set_position()
        if self.switch:
            self.enemy = self.enemy3_n1
        else:
            self.enemy = self.enemy3_n2
        # 计数器判定
        if self.scaler == 0:
            self.switch = not self.switch
            self.scaler = self.count
        # 计数器计数
        self.scaler -= 1

    def set_position(self):
        self.survival = True
        self.hp = LargeEnemy.hp
        self.spirits_index = 0
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-6 * self.height, -3 * self.height)

def add_enemies(size,bg_size,group1,group2,num):
    for i in range(num):
        enemy=MediumEnemy(bg_size)
        if size=='mimi':
            enemy=MiniEnemy(bg_size)
        if size=='medium':
            enemy=MediumEnemy(bg_size)
        if size=='large':
            enemy=LargeEnemy(bg_size)
        group1.add(enemy)
        group2.add(enemy)

#提示敌机速度
def up_speed(group,index):
    for each in group:
        each.speed+=index

def get_level(num):
    result=0
    if num>=4092:
        num2=1
        while num2<num:
            num2*=2
            result+=1
        result-=12
    return result