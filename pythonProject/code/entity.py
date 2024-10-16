#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

import pygame.image


class Entity(ABC):  #CLASSE ABSTRACT
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asstes' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
    def move(self, ):
        pass
