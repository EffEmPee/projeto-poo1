import random
from utils import *

class Baralho:
  def __init__(self):
    self.cartas = []
    for n in NAIPES:
      for o in ORDEM:
        self.cartas.append((n, o)) # ['A', 'C']

  def embaralhar(self):
    random.shuffle(self.cartas)

  def comprar(self):
    if len(self.cartas) >= 1: 
      return self.cartas.pop()