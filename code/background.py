#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        speed = ENTITY_SPEED.get(self.name, 0)
        self.rect.centerx -= speed

        # Lógica de loop infinito (reposiciona o fundo)
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
