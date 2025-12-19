import pygame
import os
imagens_path = os.path.join('Assets', 'Imagens')

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, tipo, x, y):
        super().__init__()
        self.tipo = tipo
        
        # Define a imagem/cor baseada no tipo
        if self.tipo == "chapeu":
            self.image = pygame.image.load(os.path.join(imagens_path, 'Chapeu-Chico-Science.png'))
        elif self.tipo == "oculos":
            self.image = pygame.image.load(os.path.join(imagens_path, 'Oculos-Chico-Science.png'))
        elif self.tipo == "carangueijo1":
            self.image = pygame.image.load(os.path.join(imagens_path, 'Pata-Carangueijo.png'))
        elif self.tipo == "carangueijo2":
            self.image = pygame.image.load(os.path.join(imagens_path, 'Pata-Carangueijo.png'))
        elif self.tipo == "carangueijo3":
            self.image = pygame.image.load(os.path.join(imagens_path, 'Pata-Carangueijo.png'))
        elif self.tipo == "coracao1":
            self.image = pygame.image.load(os.path.join(imagens_path, 'vida-jogador.png'))
        elif self.tipo == "coracao2":
            self.image = pygame.image.load(os.path.join(imagens_path, 'vida-jogador.png'))     
        
        # O rect define a posição e a área de colisão
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)