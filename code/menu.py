#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_BROWN, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            # 1. Primeiro desenha o fundo
            self.window.blit(source=self.surf, dest=self.rect)

            # 2. Desenha o título (Mudei para Desert Shooter para combinar com seu tema)
            self.menu_text(70, "Desert", COLOR_BROWN, ((WIN_WIDTH / 2), 70))
            self.menu_text(70, "Shooter", COLOR_BROWN, ((WIN_WIDTH / 2), 120))

            # 3. Desenha as opções do menu
            for i in range(len(MENU_OPTION)):
                pos_y = 170 + 25 * i
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), pos_y))
                else:
                    self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), pos_y))

            # 4. Desenha os controles UMA ÚNICA VEZ
            self.menu_text(15, "Controles: Setas para Mover | Espaço para Atirar", COLOR_WHITE,
                           ((WIN_WIDTH / 2), WIN_HEIGHT - 20))

            # 5. ATUALIZA A TELA
            pygame.display.flip()

            # 6. Verifica eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)