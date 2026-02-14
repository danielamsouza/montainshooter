import pygame.image
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from const import WIN_WIDTH, ORANGE_COLOR, MENU_OPTION, WHITE_COLOR


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') #carrega a imagem
        self.rect = self.surf.get_rect() #padrão left=0, top=0 / cria e insere a imagem em um retangulo
    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')  # carrega a musica
        pygame.mixer_music.play(-1)  # da play / -1 fica em loop

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenha a imagem
            self.menu_text(50,'Mountain',ORANGE_COLOR,((WIN_WIDTH/2), 70))
            self.menu_text(50, 'Shooter', ORANGE_COLOR, ((WIN_WIDTH / 2), 120))
            for i in range (len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], WHITE_COLOR, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip() #recarrega a janela
            # verifica os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha a janela
                    quit()  # fecha o pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect) #fonte utilizada no jogo (imagem)