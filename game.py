import pygame as pg
from const import WIN_WIDTH
from const import WIN_HEIGHT
from menu import Menu

class Game:
    def __init__(self):
        pg.init() #inicia o pygame
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) #cria um display

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
