from pygame import *
from baralho import *
from mao import *
import time

def convCarta(carta="back"):
  image = pygame.image.load('images/' + carta + '.png').convert()

  return pygame.transform.scale(image, (DIMENSAO_CARTA))

class VinteUm:
  def __init__(self, tela):
    self.baralho = Baralho()
    self.jogador = Mao()
    self.banca = Mao()
    self.tela = tela
    self.segurou = False

    self.baralho.embaralhar()

  def distribuir(self):
    for i in range(2):
      self.banca.adicionar(self.baralho.comprar())
      self.jogador.adicionar(self.baralho.comprar())

    self.jogador.calcularMao()

    self.tela.blit(convCarta(self.banca.imagens[0]), (300, 100))
    self.tela.blit(convCarta(), (370, 100))
    
    self.tela.blit(convCarta(self.jogador.imagens[0]), (300, 450))
    self.tela.blit(convCarta(self.banca.imagens[1]), (370, 450))
    # self.blackjack()
  
  # def checarResultado(self):
  #   if self.jogador.soma > 21:
  #     # JOGADOR estourou
  #   elif self.banca.soma > 21:
  #     # JOGADOR ganhou
  #   elif self.banca.soma == self.jogador.soma == 21:
  #     # EMPATE
  #   elif self.jogador.soma > self.banca.soma:
  #     # JOGADOR ganhou
  #   else:
  #     # BANCA ganhou      

  def comprar(self):
    if not self.segurou:
      self.jogador.adicionar(self.baralho.comprar())

      i = len(self.jogador.cartas)-1

      self.tela.blit(convCarta(self.jogador.imagens[i]), (300 + i*70 ,450))
      
      self.jogador.calcularMao()

    # if self.jogador.soma > 21:
    #   checarResultado()

  def segurar(self):
    i = 1

    while self.jogador.soma > self.banca.soma < 17:
      self.segurou = True
      self.banca.adicionar(self.baralho.comprar())

      self.tela.blit(convCarta(self.banca.imagens[i]), (300 + i*70 ,100))
    
      self.banca.calcularMao()
      time.sleep(0.5)
      i += 1

    # checarResultado()


  