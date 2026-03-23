#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.menu import Menu
from code.level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.SysFont('Consolas', 36)

    def show_text_screen(self, text):
        self.window.fill((0, 0, 0))
        surf = self.font.render(text, True, (255, 255, 255))
        self.window.blit(surf, surf.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2)))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.event.pump()

    def show_winner_screen(self, score):
        self.window.fill((0, 50, 0)) # Fundo verde de vitória
        t1 = self.font.render("MISSÃO CUMPRIDA!", True, (0, 255, 0))
        t2 = self.font.render(f"PONTUAÇÃO: {score}", True, (255, 255, 255))
        t3 = self.font.render("ESPAÇO para Menu", True, (200, 200, 200))
        self.window.blit(t1, t1.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 - 50)))
        self.window.blit(t2, t2.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 + 10)))
        self.window.blit(t3, t3.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 + 70)))
        pygame.display.flip()
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: wait = False
                if event.type == pygame.QUIT: sys.exit()

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in MENU_OPTION[:3]:
                # LEVEL 1
                self.show_text_screen("LEVEL 1: DESERTO")
                l1 = Level(self.window, 'Level1', menu_return)
                if l1.run():
                    # LEVEL 2
                    self.show_text_screen("LEVEL 2: MONTANHAS")
                    l2 = Level(self.window, 'Level2', menu_return)
                    l2.score = l1.score
                    if l2.run():
                        self.show_winner_screen(l2.score)
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                sys.exit()