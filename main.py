import pygame
from pygame.locals import *

#criando a classe das cartas
class cartas():
    def __init__(self,V,N,S,P):
        self.valor = V
        self.nome = N
        self.imagem = P
        self.naipe = S 

#criando o deck de cartas
