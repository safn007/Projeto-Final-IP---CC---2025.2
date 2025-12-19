import pygame
import os
import sys

pygame.mixer.init()
som_clique = pygame.mixer.Sound("Assets/Efeitos Sonoros/computer-mouse-click-352734.mp3")
imagens_path = os.path.join("Assets", "Imagens")

pygame.init()

# Configurações da Janela
LARGURA, ALTURA = 960, 640
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Uma aventura Manguebeat")

#imagem do fundo
imagem_fundo = pygame.image.load(os.path.join(imagens_path, 'plano_de_fundo_tela_inicial.webp'))
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

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




def menu_principal():

    som_trilha_sonora = pygame.mixer.music.load("Assets/Efeitos Sonoros/Chico_Science_Na_o_Zumbi_-_Bai_o_Ambiental_(mp3.pm).mp3")
    pygame.mixer.music.play(-1) # Toca em loop infinito
    
    rodando = True
    while rodando:

        tela.blit(imagem_fundo, (0, 0)) # Fundo da tela
        
        # Posicionamento do Mouse
        mouse_pos = pygame.mouse.get_pos()

        # Definição dos Retângulos dos Botões
        btn_iniciar = pygame.Rect(LARGURA // 2 - 105, 320, 200, 50)
        btn_instrucoes = pygame.Rect(LARGURA // 2 - 105, 385, 200, 50)


        # Tratamento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if btn_iniciar.collidepoint(mouse_pos):
                    som_clique.play()
                    pygame.mixer.music.fadeout(3000)
                    rodando = False
                    return
                
                elif btn_instrucoes.collidepoint(mouse_pos):
                    som_clique.play()
                    from src.instrucoes import mostrar_instrucao
                    mostrar_instrucao()

        
        pygame.display.update()