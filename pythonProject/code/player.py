#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        pass

    def update(self, ):
        pass

    def move(self, ):
        pass
