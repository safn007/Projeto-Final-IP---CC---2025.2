import pygame
import os
from src.coletaveis import Coletavel
from src.inimigo import Inimigo
imagens_path = os.path.join ('Assets', 'Imagens')

class Mapas:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

        # carrega os mapas
        self.mapa1 = pygame.image.load(os.path.join(imagens_path, 'mapa_1.png')).convert()
        self.mapa2 = pygame.image.load(os.path.join(imagens_path, 'mapa_2.png')).convert()
        self.mapa3 = pygame.image.load(os.path.join(imagens_path, 'mapa_3.png')).convert()
        self.mapa4 = pygame.image.load(os.path.join(imagens_path, 'mapa_4.png')).convert()
        self.mapa5 = pygame.image.load(os.path.join(imagens_path, 'mapa_5.png')).convert()
        self.mapa6 = pygame.image.load(os.path.join(imagens_path, 'mapa_6.png')).convert()

        self.mapa1_arvores = pygame.image.load(os.path.join(imagens_path, 'mapa_1_arvores.png')).convert_alpha()
        self.mapa2_arvores = pygame.image.load(os.path.join(imagens_path, 'mapa_2_arvores.png')).convert_alpha()
        self.mapa3_arvores = pygame.image.load(os.path.join(imagens_path, 'mapa_3_arvores.png')).convert_alpha()
        self.mapa4_arvores = pygame.image.load(os.path.join(imagens_path, 'mapa_4_arvores.png')).convert_alpha()
        self.mapa5_arvores = pygame.image.load(os.path.join(imagens_path, 'mapa_5_arvores.png')).convert_alpha()
        self.mapa6_arvores = pygame.image.load(os.path.join(imagens_path, 'mapa_6_arvores.png')).convert_alpha()

        self.mapa_4_cerca = pygame.image.load(os.path.join(imagens_path, 'mapa_4_cerca.png')).convert_alpha()

        self.mapa1 = pygame.transform.scale(self.mapa1, (largura, altura))
        self.mapa2 = pygame.transform.scale(self.mapa2, (largura, altura))
        self.mapa3 = pygame.transform.scale(self.mapa3, (largura, altura))
        self.mapa4 = pygame.transform.scale(self.mapa4, (largura, altura))
        self.mapa5 = pygame.transform.scale(self.mapa5, (largura, altura))
        self.mapa6 = pygame.transform.scale(self.mapa6, (largura, altura))

        self.mapa1_arvores = pygame.transform.scale(self.mapa1_arvores, (largura, altura))
        self.mapa2_arvores = pygame.transform.scale(self.mapa2_arvores, (largura, altura))
        self.mapa3_arvores = pygame.transform.scale(self.mapa3_arvores, (largura, altura))
        self.mapa4_arvores = pygame.transform.scale(self.mapa4_arvores, (largura, altura))
        self.mapa5_arvores = pygame.transform.scale(self.mapa5_arvores, (largura, altura))    
        self.mapa6_arvores = pygame.transform.scale(self.mapa6_arvores, (largura, altura))

        self.mapa_4_cerca = pygame.transform.scale(self.mapa_4_cerca, (largura, altura)) 

        # mapa inicial
        self.mapa_atual = 1

    # define a posição dos inimigos dependendo do mapa
    def get_inimigos(self):
        if self.mapa_atual == 1:
            pos_inimigos = []

        elif self.mapa_atual == 2:
            pos_inimigos = [
                (200, 200),
                (500, 500),
                (550, 200)
            ]
            
        elif self.mapa_atual == 3:
            pos_inimigos = [
                (300, 200),
                (625, 500)
            ]

        elif self.mapa_atual == 4:
            pos_inimigos = [
                (100, 100),
                (300, 250),
                (620, 250)
            ]

        elif self.mapa_atual == 5:
            pos_inimigos = [
                (135, 135),
                (350, 300),
                (630, 250)
            ]
            
        elif self.mapa_atual == 6:
            pos_inimigos = []

        return pos_inimigos

    # retorna a posição dos itens e dos objetos
    def desenhar(self, tela, chapeu_coletado, oculos_coletado, coracao1_coletado, coracao2_coletado, c1_coletado, c2_coletado, c3_coletado):
        grupo_coletaveis = pygame.sprite.Group()

        if self.mapa_atual == 1:
            # posiciona os coletáveis
            if c3_coletado == False:
                grupo_coletaveis.add(Coletavel("carangueijo3", 350, 200))

            # desenha o mapa
            tela.blit(self.mapa1, (0, 0))

        elif self.mapa_atual == 2:
            # posiciona os coletáveis
            if chapeu_coletado == False:
                grupo_coletaveis.add(Coletavel("chapeu", 335, 495))

            if coracao1_coletado == False:
                grupo_coletaveis.add(Coletavel("coracao1", 820, 230))
            
            # desenha o mapa
            tela.blit(self.mapa2, (0, 0))
        
        elif self.mapa_atual == 3:
            # posiciona os coletáveis 
            if c1_coletado == False:
                grupo_coletaveis.add(Coletavel("carangueijo1", 400, 200))

            if coracao2_coletado == False:
                grupo_coletaveis.add(Coletavel("coracao2", 220, 530))

            # desenha o mapa
            tela.blit(self.mapa3, (0, 0))
        
        elif self.mapa_atual == 4:
            # posiciona os coletáveis
            if c2_coletado == False:
                grupo_coletaveis.add(Coletavel("carangueijo2", 340, 200))

            # desenha o mapa
            tela.blit(self.mapa4, (0, 0))
            if not (chapeu_coletado and oculos_coletado):
                tela.blit(self.mapa_4_cerca, (0, 0))

        elif self.mapa_atual == 5:
            # posiciona os coletáveis
            if oculos_coletado == False:
                grupo_coletaveis.add(Coletavel("oculos", 176, 240))

            # desenha o mapa
            tela.blit(self.mapa5, (0, 0))

        elif self.mapa_atual == 6:

            # desenha o mapa
            tela.blit(self.mapa6, (0, 0))
        
        # retorna os coletaveis e os inimigos
        return grupo_coletaveis

    # desenha a camada de árvores para o player poder passar por trás delas
    def desenhar_arvores(self, tela):
        if self.mapa_atual == 1:
            tela.blit(self.mapa1_arvores, (0, 0))
        elif self.mapa_atual == 2:
             tela.blit(self.mapa2_arvores, (0, 0))
        elif self.mapa_atual == 3:
             tela.blit(self.mapa3_arvores, (0, 0))
        elif self.mapa_atual == 4:
             tela.blit(self.mapa4_arvores, (0, 0))
        elif self.mapa_atual == 5:
             tela.blit(self.mapa5_arvores, (0, 0))
        elif self.mapa_atual == 6:
             tela.blit(self.mapa6_arvores, (0, 0))

    # lógica de troca de mapas
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

            elif player.rect.bottom < 0:
                self.mapa_atual = 5
                player.rect.y = self.altura - player.rect.height
                player.pos_y = float(player.rect.y)

        elif self.mapa_atual == 4:
            if player.rect.bottom < 0:
                self.mapa_atual = 3
                player.rect.y = self.altura - player.rect.height
                player.pos_y = float(player.rect.y)

            elif player.rect.right < 0:
                self.mapa_atual = 6
                player.rect.x = self.largura - player.rect.width
                player.pos_x = float(player.rect.x)

        elif self.mapa_atual == 5:
            if player.rect.top > self.altura:
                self.mapa_atual = 3
                player.pos_y = 0.0
                player.rect.y = int(player.pos_y)

        elif self.mapa_atual == 6:
            if player.rect.left > self.largura:
                self.mapa_atual = 4
                player.rect.x = 0
                player.pos_x = 0.0

