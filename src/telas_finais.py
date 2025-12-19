import pygame
import os
import sys

pygame.init()

pygame.mixer.init()
som_clique = pygame.mixer.Sound("Assets/Efeitos Sonoros/computer-mouse-click-352734.mp3")
imagens_path = os.path.join("Assets", "Imagens")

# Configurações da Janela
LARGURA, ALTURA = 960, 640
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Uma aventura Manguebeat")

#imagem do fundo
imagem_fundo = pygame.image.load(os.path.join(imagens_path, 'Tela-Gameover.png')).convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

imagem_vitoria = pygame.image.load(os.path.join(imagens_path, 'Tela-vitoria.png')).convert()
imagem_vitoria = pygame.transform.scale(imagem_vitoria, (LARGURA, ALTURA))

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 150, 200)
VERDE = (50, 200, 150)
COR_TEXTO = (255, 255, 255)

# Fontes
fonte_titulo = pygame.font.SysFont("Arial", 64, bold=True)
fonte_subtitulo = pygame.font.SysFont("Arial", 54, bold=True)
fonte_botao = pygame.font.SysFont("Arial", 32)

def desenhar_texto(texto, fonte, cor, x, y):
    img = fonte.render(texto, True, cor)
    rect = img.get_rect(center=(x, y))
    tela.blit(img, rect)

def tela_game_over():

    rodando = True
    while rodando:
        
        # 1. Desenha o fundo (pode ser o mesmo ou uma tela preta/vermelha)
        tela.blit(imagem_fundo, (0, 0)) 
        
        # 3. Posicionamento do Mouse
        mouse_pos = pygame.mouse.get_pos()

        # 4. Definição dos Retângulos dos Botões
        btn_sair = pygame.Rect(LARGURA // 2 - 110, ALTURA // 2 + 80, 230, 50)


        # 7. Tratamento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if btn_sair.collidepoint(mouse_pos):
                    som_clique.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def tela_vitoria():

    som_trilha_vitoria = pygame.mixer.music.load("Assets/Efeitos Sonoros/Chico_Science_Na_o_Zumbi_-_A_Praieira_1994_(mp3.pm)-[AudioTrimmer.com].mp3")
    pygame.mixer.music.play(-1)
    
    rodando = True
    while rodando:
        
        # 1. Desenha o fundo (pode ser o mesmo ou uma tela preta/vermelha)
        tela.blit(imagem_vitoria, (0, 0)) 
        
        # 3. Posicionamento do Mouse
        mouse_pos = pygame.mouse.get_pos()

        # 4. Definição dos Retângulos dos Botões
        btn_sair = pygame.Rect(LARGURA // 2 - 115, ALTURA // 2 + 245, 230, 50)

        # 7. Tratamento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if btn_sair.collidepoint(mouse_pos):
                    som_clique.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()