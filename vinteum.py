import baralho
import mao

class VinteUm:
  def __init__(self):
    self.baralho = Baralho()
    self.jogador = Mao()
    self.banca = Mao()

    self.baralho.embaralhar()

    for i in range(2):
      self.banca.adicionar(self.baralho.comprar())
      self.jogador.adicionar(self.baralho.comprar())

      self.player_card = 1

      banca_card = pygame.image.load('img/' + self.banca.card_img[0] + '.png').convert()
      banca_card_2 = pygame.image.load('img/back.png').convert()
          
      player_card = pygame.image.load('img/' + self.player.card_img[0] + '.png').convert()
      player_card_2 = pygame.image.load('img/' + self.player.card_img[1] + '.png').convert()

      
      game_texts("Banca:", 500, 150)

      gameDisplay.blit(dealer_card, (400, 200))
      gameDisplay.blit(dealer_card_2, (550, 200))

      game_texts("Sua mão:", 500, 400)
      
      gameDisplay.blit(player_card, (300, 450))
      gameDisplay.blit(player_card_2, (410, 450))
      self.blackjack()
  