#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED
from code.entity import Entity

class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # Move para a esquerda (subtrai no X)
        self.rect.centerx -= ENTITY_SPEED[self.name]