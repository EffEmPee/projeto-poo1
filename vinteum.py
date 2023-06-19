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
    self.tela.blit(convCarta(self.jogador.imagens[1]), (370, 450))
  
  def checarResultado(self):
    print(self.jogador.soma)
    if self.jogador.soma > 21:
      # self.tela.fill(red)
      print('estourou')
    elif self.banca.soma > 21:
      # self.tela.fill(green)
      print('ganhou')
    elif self.banca.soma == self.jogador.soma:
      # self.tela.fill(white)
      print('empate')
    elif self.jogador.soma > self.banca.soma:
      # self.tela.fill(green)
      print('ganhou 2')
    else:
      print('banca')
      # BANCA ganhou
      # self.tela.fill(green) 

  def comprar(self):
    if not self.segurou:
      self.jogador.adicionar(self.baralho.comprar())

      i = len(self.jogador.cartas)-1

      self.tela.blit(convCarta(self.jogador.imagens[i]), (300 + i*70 ,450))
      
      self.jogador.calcularMao()

    if self.jogador.soma > 21:
      self.checarResultado()

  def segurar(self):
    i = 2

    self.tela.blit(convCarta(self.banca.imagens[1]), (370 ,100))
    pygame.display.flip()
    self.banca.calcularMao()
    pygame.time.wait(2000)

    while self.jogador.soma > self.banca.soma < 17:
      self.segurou = True
      self.banca.adicionar(self.baralho.comprar())

      self.tela.blit(convCarta(self.banca.imagens[i]), (300 + i*70 ,100))
      pygame.display.flip()
    
      self.banca.calcularMao()
      print('soma banca:', self.banca.soma)

      pygame.time.wait(1500)
      i += 1

    self.checarResultado()