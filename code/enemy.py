#!/usr/bin/python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED
from code.entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_cooldown = 80

    def move(self):
        # O inimigo sempre se move para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]

        self.shot_cooldown -= 1
        if self.shot_cooldown <= 0:
            self.shot_cooldown = 80  # Reseta o tempo
            return 'Enemy1Shot'  # Manda o comando para o Level
        return None