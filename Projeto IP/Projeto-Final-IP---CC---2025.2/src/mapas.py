import pygame

class Mapas:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

        self.mapa1 = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_1.png')
        self.mapa2 = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_2.png')

        self.mapa1 = pygame.transform.scale(self.mapa1, (largura, altura))
        self.mapa2 = pygame.transform.scale(self.mapa2, (largura, altura))

        # mapa atual
        self.mapa_atual = 1

    def desenhar(self, tela):
        if self.mapa_atual == 1:
            tela.blit(self.mapa1, (0, 0))
            recta = pygame.draw.rect(self.mapa1, (255, 0, 0), (1*32, 4*32, 32, 32))
        elif self.mapa_atual == 2:
            tela.blit(self.mapa2, (0, 0))

    def trocar_mapa(self, pos_y_jogador):
        # trocar do mapa 1 para 2
        if pos_y_jogador > self.altura:
            self.mapa_atual = 2
            return 0

        # trocar do mapa 2 para 1
        if pos_y_jogador < -60:
            self.mapa_atual = 1
            return self.altura

        return pos_y_jogador
