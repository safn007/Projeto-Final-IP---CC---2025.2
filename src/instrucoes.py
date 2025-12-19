import pygame
import os
images_path_base = os.path.join("Assets", "Imagens")

pygame.mixer.init()
som_clique = pygame.mixer.Sound("Assets/Efeitos Sonoros/computer-mouse-click-352734.mp3")

def mostrar_instrucao():
    pygame.init()
    LARGURA, ALTURA = 960, 640
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Uma aventura Manguebeat")

    #plano de fundo
    try:
        imagem_fundo = pygame.image.load(os.path.join(images_path_base, 'plano_de_fundo_instrucoes.webp')).convert()
        imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
    
    except:
        imagem_fundo = pygame.Surface((LARGURA, ALTURA))
        imagem_fundo.fill((75, 83, 32))


    # 4. Configurações do Botão
    largura_btn, altura_btn = 220, 60
    # Criamos o retângulo centralizado
    botao_rect = pygame.Rect(((LARGURA//2 - largura_btn//2) - 3, ALTURA//2 + 80, largura_btn, altura_btn))

    # 5. Loop Principal
    while True:
        tela.blit(imagem_fundo, (0, 0))
        
        # Posição do mouse
        mouse_pos = pygame.mouse.get_pos()
        
        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(mouse_pos):
                    som_clique.play()
                    return

        pygame.display.flip()