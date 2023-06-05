import pygame as pygame
from utils import *

pygame.init()


tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption("21 do Caneta Azul")

def menu_de_jogo():
    tela.fill(green)

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()

        texto = font.render("Vinte e Um", True, white)
        texto_posicao = texto.get_rect(center=(largura_tela//2, altura_tela// 3 - 50))
        tela.blit(texto, texto_posicao)

        texto2 = legenda.render("Pressione ESPAÇO para jogar", True, white)
        texto2_posicao = texto.get_rect(center=(largura_tela//2, altura_tela//3))
        tela.blit(texto2, texto2_posicao)


def jogo():
    tela.fill(plano_de_fundo)
    pygame.draw.rect(tela, grey, pygame.Rect(0, 0, 250, 700))

    jogo_rodar = True

    while jogo_rodar:
        for event in pygame.event.get():
            


            if event.type == pygame.QUIT:
                jogo_rodar = False
                pygame.quit()
                quit()
        pygame.display.flip()


menu_de_jogo()
jogo()
pygame.quit()
quit()