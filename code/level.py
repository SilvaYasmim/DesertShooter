#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random

from code.EntityMediator import EntityMediator
from code.const import WIN_HEIGHT, WIN_WIDTH
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.level_timer = 2000
        self.spawn_timer = 0
        self.clock = pygame.time.Clock()
        self.shot_cooldown = 0

        # Adiciona o Player dependendo do modo de jogo
        if self.game_mode == 'NEW GAME 1P':
            self.entity_list.append(EntityFactory.get_entity('Player1'))



    def run(self):
        while True:
            self.clock.tick(60)
            self.window.fill((135, 206, 235))

            self.level_timer -= 1
            if self.level_timer <= 0:
                return True

            if self.shot_cooldown > 0:
                self.shot_cooldown -= 1

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                move_return = ent.move()

                if move_return == 'Player1Shot' and self.shot_cooldown == 0:
                    canhao_cima_y = ent.rect.centery - 25
                    canhao_baixo_y = ent.rect.centery + 12

                    tiro_cima = EntityFactory.get_entity('Player1Shot', (ent.rect.right, canhao_cima_y))
                    tiro_baixo = EntityFactory.get_entity('Player1Shot', (ent.rect.right, canhao_baixo_y))

                    self.entity_list.append(tiro_cima)
                    self.entity_list.append(tiro_baixo)
                    self.shot_cooldown = 20

            EntityMediator.verify_collision(self.entity_list)

            # Lógica de Spawn de Inimigos
            self.spawn_timer += 1
            if self.spawn_timer >= 150:
                new_y = random.randint(50, WIN_HEIGHT - 50)
                can_spawn = True  # Inicializa como True a cada tentativa

                for ent in self.entity_list:
                    if isinstance(ent, Enemy):
                        # Se houver inimigo muito próximo da borda de spawn, cancela
                        if ent.rect.right > WIN_WIDTH - 100:
                            if abs(ent.rect.centery - new_y) < 60:
                                can_spawn = False
                                break

                if can_spawn:
                    new_enemy = EntityFactory.get_entity('Enemy1', (WIN_WIDTH, new_y))
                    self.entity_list.append(new_enemy)
                    self.spawn_timer = 0  # Reseta o timer

            # Limpeza de memória: remove inimigos que saíram totalmente da tela à esquerda
            for ent in self.entity_list:
                if ent.rect.right < 0:
                    self.entity_list.remove(ent)

            # Atualiza a tela
            pygame.display.flip()

            # Captura eventos do sistema
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()