import pygame
from random import randint
from spritesheet import Spritesheet

class Player():
    def __init__(self, loc, constantx, posx, posy, health=100, atk=20) -> None:
        self.loc = loc
        self.constantx = constantx
        self.posx = posx
        self.posy = posy 
        self.health = health
        self.atk = atk
        self.status = 'idle'
        self.update_time = pygame.time.get_ticks()
        self.animhold = []
        self.frame_count = 28
        self.frame_index = 0
        base = pygame.image.load(f'code\\liam\\python\\minicapstone\\sprites\\{self.loc}\\hero.png')
        self.sheet = Spritesheet(base)
        for x in range(self.frame_count):
            self.animhold.append(self.sheet.get_sprite(x, 32, 32, 2))
        self.sprite = self.animhold[self.frame_index]
        
    def update(self):
        frame_duration = 200
        self.sprite = self.animhold[self.frame_index]
        if self.status == 'idle':
            idle_duration = 5
            if pygame.time.get_ticks() - self.update_time > frame_duration:
                self.update_time = pygame.time.get_ticks()
                self.frame_index+=1
                if self.frame_index > idle_duration:
                    self.frame_index = 0
        if self.status == 'attack':
            atk_duration = 11
            self.posx+=20
            if self.posx >= 320:
                self.posx = 320
            if pygame.time.get_ticks() - self.update_time > frame_duration:
                self.update_time = pygame.time.get_ticks()
                self.frame_index+=1
                if self.frame_index > atk_duration:
                    self.frame_index = 0
                    self.posx = self.constantx
                    self.status = 'idle'
        if self.status == 'heal':
            heal_duration = 17
            if pygame.time.get_ticks() - self.update_time > frame_duration:
                self.update_time = pygame.time.get_ticks()
                self.frame_index+=1
                if self.frame_index > heal_duration:
                    self.frame_index = 0
                    self.status = 'idle'
        if self.status == 'hurt':
            hurt_duration = 21
            if pygame.time.get_ticks() - self.update_time > frame_duration:
                self.update_time = pygame.time.get_ticks()
                self.frame_index+=1
                if self.frame_index > hurt_duration:
                    self.frame_index = 0
                    self.status = 'idle'
        if self.status == 'magic':
            magic_duration = 27
            if pygame.time.get_ticks() - self.update_time > frame_duration:
                self.update_time = pygame.time.get_ticks()
                self.frame_index+=1
                if self.frame_index > magic_duration:
                    self.frame_index = 0
                    self.status = 'idle'
   
    def display(self, screen):
        posy = self.posy
        screen.blit(self.sprite, (self.posx, posy))

    def attack(self, target):
        damage = randint(self.atk-5, self.atk+5)
        target.health -= damage
        if target.health < 0:
            target.health = 0
        return damage

    def magic(self, target):
        damage = randint(1,40)
        target.health -= damage
        if target.health < 0:
            target.health = 0
        return damage

    def heal(self):
        self.health += randint(5, 25)
        if self.health >= 100:
            self.health = 100
        return self.health
    
    #death checks
    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        

class Enemy():
    def __init__(self, loc, constantx, posx, posy, health, atk) -> None:
        self.loc = loc
        self.constantx = constantx
        self.posx = posx 
        self.posy = posy 
        self.health = health
        self.atk = atk
        self.status = 'idle'
        self.update_time = pygame.time.get_ticks()
        self.animhold = []
        self.frame_count = 16
        self.frame_index = 0
        base = pygame.image.load(f'code\\liam\\python\\minicapstone\\sprites\\{self.loc}\\{self.loc}.png')
        self.sheet = Spritesheet(base)
        for x in range(self.frame_count):
            self.animhold.append(self.sheet.get_sprite(x, 32, 32, 2))
        self.sprite = self.animhold[self.frame_index]

    def update(self):
        frame_duration = 200
        self.sprite = self.animhold[self.frame_index]
        if self.status == 'idle':
            idle_duration = 5
            if pygame.time.get_ticks() - self.update_time > frame_duration:
                self.update_time = pygame.time.get_ticks()
                self.frame_index+=1
                if self.frame_index > idle_duration:
                    self.frame_index = 0
        if self.status == 'attack':
            atk_duration = 11
            self.posx-=20
            if self.posx <= 110:
                self.posx = 110
            if pygame.time.get_ticks() - self.update_time > frame_duration:
                self.update_time = pygame.time.get_ticks()
                self.frame_index+=1
                if self.frame_index > atk_duration:
                    self.frame_index = 0
                    self.posx = self.constantx
                    self.status = 'idle'
        if self.status == 'hurt':
            hurt_duration = 15
            if pygame.time.get_ticks() - self.update_time > frame_duration:
                self.update_time = pygame.time.get_ticks()
                self.frame_index+=1
                if self.frame_index > hurt_duration:
                    self.frame_index = 0
                    self.status = 'idle'

    def display(self, screen): #was only screen before testing
        posy = self.posy
        screen.blit(self.sprite, (self.posx, posy))

    def attack(self, target):
        damage = randint(self.atk-5, self.atk+5)
        target.health -= damage
        if target.health < 0:
            target.health = 0
        return damage
      
        #death checks
    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
