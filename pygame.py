import pygame as pygame
pygame.init()

altura_tela = 600
largura_tela = 800

tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption("Blackjack")
gameDisplay.fill(plano_de_fundo)

jogo_rodar = True

while jogo_rodar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_rodar = False
    pygame.display.flip()
pygame.quit()

