#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import const
from code.Score import Score
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_RED, C_GREEN, NEXT_LEVEL_POS
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
    def mostrar_inicio_level2(self):

        self.window.blit(pygame.image.load("./asset/Level2Bg0.png"), (0, 0))
        self.next_level_text(74, "Level 2", C_RED, NEXT_LEVEL_POS)
        pygame.display.flip()
        pygame.time.delay(2000)  # Aguarda 2 segundos antes de sair ou reiniciar
    def mostrar_inicio_level3(self):
            self.window.blit(pygame.image.load("./asset/Level3Bg2.png"), (0, 0))
            self.next_level_text(74, "Level 3", C_RED, NEXT_LEVEL_POS)
            pygame.display.flip()
            pygame.time.delay(2000)  # Aguarda 2 segundos antes de sair ou reiniciar

    def run(self):
        while True:
            score= Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [player1, player2]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    self.mostrar_inicio_level2()
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        self.mostrar_inicio_level3()
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                           score.save(menu_return, player_score)
            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # close window
                quit()  # end game
            else:
                pygame.quit()
                sys.exit()

    def next_level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)