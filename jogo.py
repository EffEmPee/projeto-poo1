import pygame as pygame
from utils import *
from vinteum import *

pygame.init()

tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption("21 do Caneta Azul")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def texto(text, x, y):
    TextSurf, TextRect = text_objects(text, textfont)
    TextRect.center = (x, y)
    tela.blit(TextSurf, TextRect)

    pygame.display.update()

def menu_de_jogo():
    tela.fill(green)

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogar()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()

        texto = font.render("Vinte e Um do Blue Pen", True, white)
        texto_posicao = texto.get_rect(center=(largura_tela//2, altura_tela// 3 - 50))
        tela.blit(texto, texto_posicao)

        texto2 = legenda.render("Pressione ESPAÇO para jogar", True, white)
        texto2_posicao = texto.get_rect(center=(largura_tela//2, altura_tela//3))
        tela.blit(texto2, texto2_posicao)


def jogar():
    tela.fill(plano_de_fundo)
    pygame.draw.rect(tela, grey, pygame.Rect(0, 0, 250, 700))

    jogo = VinteUm(tela)
    
    texto("Banca:", 500, 50)
    texto("Sua mãe:", 500, 400)
    
    jogo.distribuir()

    while True:
        for event in pygame.event.get():
            texto(f"soma: {jogo.banca.soma}", 700, 50)
            texto(f"soma: {jogo.jogador.soma}", 700, 400)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    jogo.comprar()
                elif event.key == pygame.K_v:
                    jogo.segurar()
                elif event.key == pygame.K_q:
                    menu_de_jogo()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()

menu_de_jogo()