#teste Samuel comentário
import pygame
import sys
from src.mapas import Mapas
from src.colisoes import Colisoes
from src.coletaveis import Coletavel
from src.player import Player

def executar_jogo():
    pygame.init() # Inicia o pygame

    largura = 960
    altura = 640
    mapas = Mapas(largura, altura)
    tela = pygame.display.set_mode((largura, altura)) # Define o tamanho da janela do jogo
    pygame.display.set_caption("Ricardo Jones: Uma Aventura MangueBeat") # Nome que aparece no título da janela

    player = Player(250, 250)

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

    # Grupo de sprites
    sprites_group = pygame.sprite.Group()
    sprites_group.add(player)

    clock = pygame.time.Clock() # Cria relogio pra controlar FPS
    rodando_jogo = True

    while rodando_jogo:
        clock.tick(60) # Limita os FPS a 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.QUIT:
                rodando_jogo = False


        for item in grupo_coletaveis:
            if player.hitbox.colliderect(item.rect):
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
                    
        # desenha mapa
        mapas.desenhar(tela)

        # troca de mapa (altera o rect diretamente)
        mapas.trocar_mapa(player.rect)

        # coletar colisões
        colisoes = Colisoes([3, 5, 9, 11, 241])
        colisoes = colisoes.criar_colisoes()
        for coord in colisoes:
            caixa = pygame.Rect(coord[0], coord[1], 32, 32)

        # Atualiza todos os sprites do grupo
        sprites_group.update() 
        
        # Desenha os sprites na janela
        sprites_group.draw(tela)
        grupo_coletaveis.draw(tela) #desenha os coletaveis
    
        
        pygame.display.update()

    