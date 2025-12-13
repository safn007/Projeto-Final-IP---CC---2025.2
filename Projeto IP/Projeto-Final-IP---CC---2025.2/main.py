import pygame
from src.coletaveis import Coletavel

largura = 800
altura = 600
janela_jogo = pygame.display.set_mode((largura, altura)) #Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") #Nome que aparece no título da janela

fundo_original = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Imagem_de_fundo.png')
fundo = pygame.transform.scale(fundo_original, (largura, altura))

personagem_original = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Personagem-removebg-preview.png')
personagem = pygame.transform.scale(personagem_original, (250, 150))

pos_x_jogador = 250
pos_y_jogador = 250
velocidade_jogador = 0.35

direcao = pygame.math.Vector2(0, 0)

grupo_coletaveis = pygame.sprite.Group() #criando os coletaveis
#adicionando no mapa
grupo_coletaveis.add(Coletavel("chapeu", 100, 100))
grupo_coletaveis.add(Coletavel("oculos", 150, 100))
grupo_coletaveis.add(Coletavel("carangueijo", 600, 500))
grupo_coletaveis.add(Coletavel("carangueijo", 400, 100))

#variaveis para contagem de coletaveis
qnt_chapeu = 0
qnt_oculos = 0
qnt_carangueijo = 0


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

    player_rect = personagem.get_rect()
    player_rect.topleft = (pos_x_jogador, pos_y_jogador)

    for item in grupo_coletaveis:
        if player_rect.colliderect(item.rect):
            item.kill() #remove o item do jogo e do grupo

            if item.tipo == "chapeu":
                print("pegou chapeu")
                qnt_chapeu+=1
            elif item.tipo == "oculos":
                print("pegou oculos")
                qnt_oculos+=1
            elif item.tipo == "carangueijo":
                print("pegou carangueijo")
                qnt_carangueijo+=1
    
    janela_jogo.blit(fundo, (0,0))
    janela_jogo.blit(personagem, (pos_x_jogador, pos_y_jogador))

    grupo_coletaveis.draw(janela_jogo) #desenha os coletaveis

    pygame.display.update()

