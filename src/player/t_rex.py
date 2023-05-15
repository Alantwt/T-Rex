import pygame
from pygame.sprite import Group, Sprite
import time


class T_Rex(Sprite):
    def __init__(self, *groups: Group, x: int=0, y: int=0) -> None:
        super().__init__(*groups)

        # Configuracion de la imagen y dimensiones del personaje
        self.imgs = ['src/img/t-rex/t-rex.png','src/img/t-rex/t-rex_right_leg_running.png','src/img/t-rex/t-rex_left_leg_running.png','src/img/t-rex/t-rex_right_leg_down_running.png','src/img/t-rex/t-rex_left_leg_down_running.png']
        self.img = pygame.image.load(self.imgs[0],'pygame')
        # self.img = pygame.transform.scale(self.img, (90, 100))
        self._rect = self.img.get_rect()

        # Configuracion de la posicion del t-rex
        self.x = int(x)
        self.y = int(y)
        self._rect.x = x
        self._rect.y = y
        
        # 0 derecha, 1 izquierda
        self.running = 0
        self.down_running = 0
        self.time_runing = time.time()

        


    def jump(self):
        pass

    def bend_down(self):
        pass

    def run(self):
        delay = time.time()
        if self._rect.y != self.y:
            self._rect.y = self.y

        if self.running == 0 and abs(self.time_runing - delay) > 0.1 :
            self.img = pygame.image.load(self.imgs[1],'pygame')
            self.running = 1
            self.time_runing = delay
        elif self.running == 1 and abs(self.time_runing - delay) > 0.1: 
            self.img = pygame.image.load(self.imgs[2],'pygame')
            self.running = 0
            self.time_runing = delay

        
    
    def stop(self):
        if self._rect.y != self.y:
            self._rect.y = self.y

        self.img = pygame.image.load(self.imgs[0],'pygame')

    def down_run(self):
        delay = time.time()
        self._rect.y = self.y + 35
        if self._rect.y == self.y:
            print(self.img.get_size())
            # self._rect.y = self.y + 35
            pass

        if self.down_running == 0 and abs(self.time_runing - delay) > 0.1:
            self.img = pygame.image.load(self.imgs[3],'pygame')
            self.down_running = 1
            self.time_runing = delay
        elif self.down_running == 1 and abs(self.time_runing - delay) > 0.1: 
            self.img = pygame.image.load(self.imgs[4],'pygame')
            self.down_running = 0
            self.time_runing = delay

    def set_position(self,x,y):
        self._rect.x = x
        self._rect.y = y

    


