import pygame

ORDEM = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
NAIPES = ['H', 'S', 'D', 'C']

altura_tela = 700
largura_tela = 900

DIMENSAO_CARTA = (100, 150)

plano_de_fundo = (34,139,34)
grey = (220,220,220)
black = (0,0,0)
green = (0, 200, 0)
red = (255,0,0)
light_slat = (119,136,153)
dark_slat = (47, 79, 79)
dark_red = (255, 0, 0)
white = (255, 255, 255)

pygame.init()
font = pygame.font.SysFont("Arial", 36)
legenda = pygame.font.SysFont("Arial", 24)
textfont = pygame.font.SysFont('Comic Sans MS', 35)
game_end = pygame.font.SysFont('dejavusans', 100)
blackjack = pygame.font.SysFont('roboto', 70)
