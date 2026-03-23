#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.enemy import Enemy
from code.player import Player
from code.PlayerShot import PlayerShot
from code.EnemyShot import EnemyShot

class EntityMediator:

    @staticmethod
    def verify_collision(entity_list, level):
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
                        level.score += 100

                    # Caso B: Player vs Inimigo (Dano na nave)
                    elif (isinstance(ent1, Player) and (isinstance(ent2, Enemy) or isinstance(ent2, EnemyShot))) or \
                            (isinstance(ent2, Player) and (isinstance(ent1, Enemy) or isinstance(ent1, EnemyShot))):

                        player = ent1 if isinstance(ent1, Player) else ent2
                        perigo = ent2 if isinstance(ent1, Player) else ent1

                        if player.rect.colliderect(perigo.rect):
                            # Só toma dano se NÃO estiver invulnerável
                            if player.invincible_timer <= 0:
                                player.health -= 1
                                player.invincible_timer = 100
                                print(f"VIDAS: {player.health}")

                                if player.health <= 0:
                                    print("GAME OVER")


                            # Remove o tiro ou o inimigo que bateu no player
                            if not isinstance(perigo, Enemy):  # Se for tiro, remove sempre
                                to_remove.append(perigo)
                            return

                if (isinstance(ent1, EnemyShot) and isinstance(ent2, Player)) or \
                        (isinstance(ent2, EnemyShot) and isinstance(ent1, Player)):
                    if ent1.rect.colliderect(ent2.rect):
                        # Aqui o player morre ou perde vida
                        if isinstance(ent1, EnemyShot): to_remove.append(ent1)
                        if isinstance(ent2, EnemyShot): to_remove.append(ent2)
                        print("PLAYER FOI ATINGIDO!")


        for entity in to_remove:
            if entity in entity_list:
                entity_list.remove(entity)