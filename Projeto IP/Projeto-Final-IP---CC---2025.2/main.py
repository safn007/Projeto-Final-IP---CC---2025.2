import pygame
from src.mapas import Mapas 

largura = 960
altura = 640
janela_jogo = pygame.display.set_mode((largura, altura)) #Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") #Nome que aparece no título da janela

mapas = Mapas(largura, altura)

personagem_original = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Personagem-removebg-preview.png')
personagem = pygame.transform.scale(personagem_original, (150, 90))

pos_x_jogador = 250
pos_y_jogador = 250
velocidade_jogador = 1

direcao = pygame.math.Vector2(0, 0)

rodar_jogo = True
while rodar_jogo:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            rodar_jogo = False

    teclas = pygame.key.get_pressed()
    direcao.x = 0
    direcao.y = 0

    if teclas[pygame.K_w]:
        direcao.y -= 1
    if teclas[pygame.K_s]:
        direcao.y += 1
    if teclas[pygame.K_a]:
        direcao.x -= 1
    if teclas[pygame.K_d]:
        direcao.x += 1

    if direcao.length() > 0:
        direcao = direcao.normalize()

    pos_x_jogador += direcao.x * velocidade_jogador
    pos_y_jogador += direcao.y * velocidade_jogador
    
    # controlar fase
    mapas.desenhar(janela_jogo)
    janela_jogo.blit(personagem, (pos_x_jogador, pos_y_jogador))

    pos_y_jogador = mapas.trocar_mapa(pos_y_jogador)

    pygame.display.update()

pygame.quit()
