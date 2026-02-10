import pygame as pg

pg.init()
window = pg.display.set_mode(size=(600, 480))

while True:
    #chek for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() #Close Window
            quit() #end pygame


