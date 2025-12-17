import pygame

class Mapas:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

        self.mapa1 = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_1.png')
        self.mapa2 = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_2.png')
        self.mapa3 = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_3.png')

        self.mapa1 = pygame.transform.scale(self.mapa1, (largura, altura))
        self.mapa2 = pygame.transform.scale(self.mapa2, (largura, altura))
        self.mapa3 = pygame.transform.scale(self.mapa3, (largura, altura))

        # mapa atual
        self.mapa_atual = 1

    def desenhar(self, tela):
        if self.mapa_atual == 1:
            tela.blit(self.mapa1, (0, 0))
        elif self.mapa_atual == 2:
            tela.blit(self.mapa2, (0, 0))
        elif self.mapa_atual == 3:
            tela.blit(self.mapa3, (0, 0))

    def trocar_mapa(self, player):

        if self.mapa_atual == 1:
            if player.rect.top > self.altura:
                self.mapa_atual = 2
                player.rect.y = 0
                player.pos_y = 0.0

        elif self.mapa_atual == 2:
            if player.rect.bottom < 0:
                self.mapa_atual = 1
                player.rect.y = self.altura - player.rect.height
                player.pos_y = float(player.rect.y)

            elif player.rect.left > self.largura:
                self.mapa_atual = 3
                player.rect.x = 0
                player.pos_x = 0.0

        elif self.mapa_atual == 3:
            if player.rect.right < 0:
                self.mapa_atual = 2
                player.rect.x = self.largura - player.rect.width
                player.pos_x = float(player.rect.x)

