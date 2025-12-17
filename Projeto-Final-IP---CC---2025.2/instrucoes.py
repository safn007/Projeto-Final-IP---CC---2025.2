import pygame
import sys
import os
images_path_base = os.path.join("Assets", "Imagens")
#salvando mundanças instruções
def mostrar_instrucao():
    pygame.init()
    LARGURA, ALTURA = 960, 640
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Tela de Instruções")

    #plano de fundo
    try:
        imagem_fundo = pygame.image.load(os.path.join(images_path_base, 'plano_de_fundo_instrucoes_oficial.png')).convert()
        imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
    
    except:
        imagem_fundo = pygame.Surface((LARGURA, ALTURA))
        imagem_fundo.fill((75, 83, 32))
    
    # 2. Definição de Cores
    VERDE_CLARO = (100, 110, 45) # Cor para quando o mouse estiver em cima
    BRANCO      = (255, 255, 255)
    PRETO       = (0, 0, 0)

    # 3. Fontes
    fonte_titulo = pygame.font.SysFont("Arial", 50, bold=True)
    fonte_subtitulo = pygame.font.SysFont("Arial", 30, bold=True)
    fonte_botao  = pygame.font.SysFont("Arial", 30, bold=True)

    def desenhar_texto(texto, fonte, cor, x, y):
        superficie_texto = fonte.render(texto, True, cor)
        rect = superficie_texto.get_rect(center=(x, y))
        tela.blit(superficie_texto, rect)

    # 4. Configurações do Botão
    largura_btn, altura_btn = 300, 60
    # Criamos o retângulo centralizado
    botao_rect = pygame.Rect((LARGURA//2 - largura_btn//2, ALTURA//2 + 140, largura_btn, altura_btn))

    # 5. Loop Principal
    while True:
        tela.blit(imagem_fundo, (0, 0))
        
        # Posição do mouse
        mouse_pos = pygame.mouse.get_pos()
        
        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(mouse_pos):
                    return

        # Lógica de "Hover" (mudar cor quando o mouse passa por cima)
        cor_atual_btn = VERDE_CLARO if botao_rect.collidepoint(mouse_pos) else PRETO

        # Desenhar o Título
        desenhar_texto("INSTRUÇÕES", fonte_titulo, PRETO, LARGURA // 2, 150)
        desenhar_texto("Movimentação do Player:", fonte_subtitulo, PRETO, LARGURA // 2, 250)
        desenhar_texto("W - A - S - D", fonte_subtitulo, PRETO, LARGURA // 2, 300)
        
        desenhar_texto("Objetivo:", fonte_subtitulo, PRETO, LARGURA // 2, 350)
        desenhar_texto("Sobreviver aos ataques dos caranguejos", fonte_subtitulo, PRETO, LARGURA // 2, 400)
        
        # Desenhar o Retângulo do Botão
        pygame.draw.rect(tela, cor_atual_btn, botao_rect, border_radius=15)
        # Desenhar borda para o botão
        pygame.draw.rect(tela, BRANCO, botao_rect, width=2, border_radius=15)

        # Desenhar o texto do botão
        desenhar_texto("VOLTAR AO MENU", fonte_botao, BRANCO, botao_rect.centerx, botao_rect.centery)

        pygame.display.flip()


