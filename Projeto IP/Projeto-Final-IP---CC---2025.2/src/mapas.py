import pygame
from src.coletaveis import Coletavel
from src.inimigo import Inimigo

class Mapas:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

        self.mapa1 = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_1.png')
        self.mapa2 = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_2.png')
        self.mapa3 = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_3.png')
        self.mapa4 = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_4.png')

        self.mapa1_arvores = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_1_arvores.png')
        self.mapa2_arvores = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_2_arvores.png')
        self.mapa3_arvores = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_3_arvores.png')
        self.mapa4_arvores = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/mapa_4_arvores.png')

        self.mapa1 = pygame.transform.scale(self.mapa1, (largura, altura))
        self.mapa2 = pygame.transform.scale(self.mapa2, (largura, altura))
        self.mapa3 = pygame.transform.scale(self.mapa3, (largura, altura))
        self.mapa4 = pygame.transform.scale(self.mapa4, (largura, altura))

        self.mapa1_arvores = pygame.transform.scale(self.mapa1_arvores, (largura, altura))
        self.mapa2_arvores = pygame.transform.scale(self.mapa2_arvores, (largura, altura))
        self.mapa3_arvores = pygame.transform.scale(self.mapa3_arvores, (largura, altura))
        self.mapa4_arvores = pygame.transform.scale(self.mapa4_arvores, (largura, altura))

        # mapa inicial
        self.mapa_atual = 1

    def desenhar(self, tela, coletado, chapeu_coletado, oculos_coletado):
        grupo_coletaveis = pygame.sprite.Group()
        grupo_inimigos = pygame.sprite.Group()

        if self.mapa_atual == 1:
            # posiciona os coletáveis
            if coletado == False and chapeu_coletado == False:
                grupo_coletaveis.add(Coletavel("chapeu", 100, 100))
            
            # adiciona os inimigos
            posicoes_inimigos = [
                (600, 300), 
                (800, 100), 
                (150, 500), 
                (850, 550) 
            ]

            for pos in posicoes_inimigos:
                # Cria um inimigo para cada posição e adiciona ao grupo
                inimigo = Inimigo(pos[0], pos[1])
                grupo_inimigos.add(inimigo)

            # desenha o mapa
            tela.blit(self.mapa1, (0, 0))

        elif self.mapa_atual == 2:
            # posiciona os coletáveis
            if coletado == False and oculos_coletado == False:
                grupo_coletaveis.add(Coletavel("oculos", 150, 100))

            # adiciona os inimigos

            # desenha o mapa
            tela.blit(self.mapa2, (0, 0))
        
        elif self.mapa_atual == 3:
            # posiciona os coletáveis 
            grupo_coletaveis.add(Coletavel("carangueijo", 600, 500))
            
            # adiciona os inimigos

            # desenha o mapa
            tela.blit(self.mapa3, (0, 0))
        
        elif self.mapa_atual == 4:
            # posiciona os coletáveis
            
            # adiciona os inimigos

            # desenha o mapa
            tela.blit(self.mapa4, (0, 0))
        
        # retorna os coletaveis e os inimigos
        return [grupo_coletaveis, grupo_inimigos]

    def desenhar_arvores(self, tela):
        if self.mapa_atual == 1:
            tela.blit(self.mapa1_arvores, (0, 0))
        elif self.mapa_atual == 2:
             tela.blit(self.mapa2_arvores, (0, 0))
        elif self.mapa_atual == 3:
             tela.blit(self.mapa3_arvores, (0, 0))
        elif self.mapa_atual == 4:
             tela.blit(self.mapa4_arvores, (0, 0))

    def trocar_mapa(self, player):
        if self.mapa_atual == 1:
            if player.rect.top > self.altura:
                self.mapa_atual = 2
                player.pos_y = 0.0
                player.rect.y = int(player.pos_y)

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

            elif player.rect.top > self.altura:
                self.mapa_atual = 4
                player.pos_y = 0.0
                player.rect.y = int(player.pos_y)

        elif self.mapa_atual == 4:
            if player.rect.bottom < 0:
                self.mapa_atual = 3
                player.rect.y = self.altura - player.rect.height
                player.pos_y = float(player.rect.y)
