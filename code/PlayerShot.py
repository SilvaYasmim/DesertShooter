#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED
from code.entity import Entity

class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # O tiro se move para a direita (X aumenta)
        self.rect.centerx += ENTITY_SPEED[self.name]