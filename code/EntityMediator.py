#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.enemy import Enemy
from code.player import Player
from code.PlayerShot import PlayerShot

class EntityMediator:

    @staticmethod
    def verify_collision(entity_list):
        to_remove = [] # Lista de quem vai "morrer"

        for i in range(len(entity_list)):
            ent1 = entity_list[i]
            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]

                # Se algum deles já foi marcado para remover, ignora
                if ent1 in to_remove or ent2 in to_remove:
                    continue

                # Checa colisão física
                if ent1.rect.colliderect(ent2.rect):
                    # Caso A: Tiro do Player vs Inimigo
                    if (isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy)) or \
                       (isinstance(ent2, PlayerShot) and isinstance(ent1, Enemy)):
                        to_remove.append(ent1)
                        to_remove.append(ent2)

                    # Caso B: Player vs Inimigo (Dano na nave)
                    elif (isinstance(ent1, Player) and isinstance(ent2, Enemy)) or \
                         (isinstance(ent2, Player) and isinstance(ent1, Enemy)):
                        # Marca apenas o inimigo para sumir
                        if isinstance(ent1, Enemy): to_remove.append(ent1)
                        if isinstance(ent2, Enemy): to_remove.append(ent2)
                        print("PLAYER BATEU NO INIMIGO!")

        # Agora removemos de verdade da lista principal sem bugar o loop
        for entity in to_remove:
            if entity in entity_list:
                entity_list.remove(entity)