#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
from code.EntityMediator import EntityMediator
from code.const import WIN_HEIGHT, WIN_WIDTH
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player
from code.background import Background

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.score = 0
        self.level_timer = 2000
        self.spawn_timer = 0
        self.clock = pygame.time.Clock()
        self.shot_cooldown = 0
        self.font = pygame.font.SysFont('Consolas', 24)

        if name == 'Level1':
            self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        else:
            self.entity_list.extend(EntityFactory.get_entity('Level2Bg'))


        if self.game_mode == 'NEW GAME 1P':
            self.entity_list.append(EntityFactory.get_entity('Player1'))

    def draw_hud(self):
        hp = 0
        for ent in self.entity_list:
            if isinstance(ent, Player):
                hp = ent.health
        display_hp = hp if hp > 0 else 0
        score_surf = self.font.render(f'SCORE: {self.score}', True, (255, 255, 255))
        hp_surf = self.font.render(f'LIVES: {display_hp}', True, (255, 255, 255))
        self.window.blit(score_surf, (20, 20))
        self.window.blit(hp_surf, (WIN_WIDTH - 150, 20))

    def run(self):
        while True:
            self.clock.tick(60)
            self.window.fill((0, 0, 0))

            self.level_timer -= 1
            if self.level_timer <= 0:
                return True

            if self.shot_cooldown > 0:
                self.shot_cooldown -= 1

            # --- DESENHO POR CAMADAS ---
            # Camada 1: Fundos
            for ent in self.entity_list:
                if isinstance(ent, Background):
                    self.window.blit(ent.surf, ent.rect)
                    ent.move()

            # Camada 2: Inimigos e Tiros
            for ent in self.entity_list:
                if not isinstance(ent, (Background, Player)):
                    self.window.blit(ent.surf, ent.rect)
                    move_return = ent.move()
                    if move_return in ['Enemy1Shot', 'Enemy2Shot']:
                        shot_name = 'Enemy1Shot' if self.name == 'Level1' else 'Enemy2Shot'
                        self.entity_list.append(EntityFactory.get_entity(shot_name, ent.rect.midleft))

            # Camada 3: Player
            player_found = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    player_found = True
                    if ent.visible:
                        self.window.blit(ent.surf, ent.rect)
                    move_return = ent.move()
                    if move_return == 'Player1Shot' and self.shot_cooldown == 0:
                        c_cima = ent.rect.centery - 25
                        c_baixo = ent.rect.centery + 12
                        self.entity_list.append(EntityFactory.get_entity('Player1Shot', (ent.rect.right, c_cima)))
                        self.entity_list.append(EntityFactory.get_entity('Player1Shot', (ent.rect.right, c_baixo)))
                        self.shot_cooldown = 20
                    if ent.health <= 0:
                        self.show_game_over()
                        return False

            if not player_found:
                self.show_game_over()
                return False

            # --- LOGICA DE SPAWN ---
            self.spawn_timer += 1
            if self.spawn_timer >= 120:
                new_y = random.randint(50, WIN_HEIGHT - 50)
                e_name = 'Enemy1' if self.name == 'Level1' else 'Enemy2'
                self.entity_list.append(EntityFactory.get_entity(e_name, (WIN_WIDTH, new_y)))
                self.spawn_timer = 0

            # --- COLISÕES E LIMPEZA ---
            EntityMediator.verify_collision(self.entity_list, self)
            for ent in self.entity_list:
                if not isinstance(ent, Player):
                    if ent.rect.right < -100 or ent.rect.left > WIN_WIDTH + 100:
                        self.entity_list.remove(ent)

            self.draw_hud()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def show_game_over(self):
        self.window.fill((0, 0, 0))
        go_surf = self.font.render('GAME OVER', True, (255, 0, 0))
        sc_surf = self.font.render(f'FINAL SCORE: {self.score}', True, (255, 255, 255))
        inst_surf = self.font.render('ESPAÇO para Menu', True, (200, 200, 200))
        self.window.blit(go_surf, go_surf.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 - 40)))
        self.window.blit(sc_surf, sc_surf.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 + 10)))
        self.window.blit(inst_surf, inst_surf.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 + 60)))
        pygame.display.flip()
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: wait = False
                if event.type == pygame.QUIT: exit()