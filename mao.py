class Mao():
  def __init__(self):
    self.cartas = [] 
    self.soma = 0
    self.imagens = []

  def adicionar(self, carta):
    self.cartas.append(carta)
    self.imagens.append("".join(carta[0], carta[1]))
  
  def calcularMao(self):
    ordem_carta = [carta[0] for carta in self.cartas]
    nao_ases = [carta for carta in ordem_carta if carta != 'A']
    ases = [carta for carta in ordem_carta if carta == 'A']

    for carta in nao_ases:
      if carta in 'JQK':
        self.soma += 10
      else:
        self.soma += int(carta)
    
    for carta in ases:
      if self.soma <= 10:
        self.soma += 11
      else:
        self.soma += 1  