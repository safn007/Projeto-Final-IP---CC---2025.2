import pygame
import os
#salvando mudança

images_path_base = os.path.join("Assets", "Imagens")

pygame.init()

# Configurações da Janela
LARGURA, ALTURA = 960, 640
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo - Tela Inicial")

#imagem do fundo
imagem_fundo = pygame.image.load(os.path.join(images_path_base, 'plano_de_fundo_tela_inicial.png'))

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
    rodando = True
    while rodando:
        tela.blit(imagem_fundo, (0, 0)) # Fundo da tela
        
        # Posicionamento do Mouse
        mouse_pos = pygame.mouse.get_pos()

        # Título
        desenhar_texto("Ricardo Jones", fonte_titulo, PRETO, LARGURA // 2, 150)
        desenhar_texto("Uma Aventura MANGUEBEAT", fonte_subtitulo, PRETO, LARGURA // 2, 210)

        # Definição dos Retângulos dos Botões
        btn_iniciar = pygame.Rect(LARGURA // 2 - 100, 300, 200, 50)
        btn_instrucoes = pygame.Rect(LARGURA // 2 - 100, 400, 200, 50)

        # Desenho e Lógica Visual dos Botões (Efeito Hover)
        cor_btn_1 = VERDE if btn_iniciar.collidepoint(mouse_pos) else AZUL
        cor_btn_2 = VERDE if btn_instrucoes.collidepoint(mouse_pos) else AZUL

        pygame.draw.rect(tela, cor_btn_1, btn_iniciar, border_radius=12)
        pygame.draw.rect(tela, cor_btn_2, btn_instrucoes, border_radius=12)

        # Texto nos Botões
        desenhar_texto("INICIAR", fonte_botao, COR_TEXTO, LARGURA // 2, 325)
        desenhar_texto("INSTRUÇÕES", fonte_botao, COR_TEXTO, LARGURA // 2, 425)

        # Tratamento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if btn_iniciar.collidepoint(mouse_pos):
                    import main
                    main.executar_jogo()
                    pygame.quit()
                elif btn_instrucoes.collidepoint(mouse_pos):
                    from instrucoes import mostrar_instrucao
                    mostrar_instrucao()

        
        pygame.display.update()


if __name__ == "__main__":
        menu_principal()



