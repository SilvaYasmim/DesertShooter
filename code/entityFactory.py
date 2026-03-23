#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (80, WIN_HEIGHT / 2))

            case 'Enemy1':
                return Enemy('Enemy1', position)

            case 'Enemy2':
                return Enemy('Enemy2', position)

            case 'Player1Shot':
                return PlayerShot('Player1Shot', position)

            case 'Enemy1Shot':
                return EnemyShot('Enemy1Shot', position)

            case 'Enemy2Shot':
                return EnemyShot('Enemy2Shot', position)