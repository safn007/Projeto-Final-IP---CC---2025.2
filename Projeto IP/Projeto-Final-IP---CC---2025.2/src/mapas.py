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

    def trocar_mapa(self, retangulo):

        if self.mapa_atual == 1:
            if retangulo.top > self.altura:
                self.mapa_atual = 2
                retangulo.y = 0

        elif self.mapa_atual == 2:
            if retangulo.bottom < 0:
                self.mapa_atual = 1
                retangulo.y = self.altura

            elif retangulo.left > self.largura:
                self.mapa_atual = 3
                retangulo.x = -60

        elif self.mapa_atual == 3:
            if retangulo.right < 0:
                self.mapa_atual = 2
                retangulo.x = self.largura - 100

        return retangulo
