import pygame as pg

from Level import Level
from const import WIN_WIDTH, MENU_OPTION
from const import WIN_HEIGHT
from menu import Menu

class Game:
    def __init__(self):
        pg.init() #inicia o pygame
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) #cria um display

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pg.quit()
                quit()
            else:
                pass
