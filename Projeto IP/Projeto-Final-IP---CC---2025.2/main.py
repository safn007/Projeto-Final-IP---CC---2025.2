#teste Samuel comentário
import pygame
from src.mapas import Mapas
from src.colisoes import Colisoes
from src.coletaveis import Coletavel
from src.player import Player
from src.inimigo import Inimigo #

pygame.init() # Inicia o pygame

largura = 960
altura = 640
mapas = Mapas(largura, altura)
tela = pygame.display.set_mode((largura, altura)) # Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") # Nome que aparece no título da janela

player = Player(250, 250)
player.vida = 100 #Definindo vida para o player 

#criando grupo de inimigos e adicionando um
grupo_inimigos = pygame.sprite.Group()
inimigo_teste = Inimigo(600, 300)
grupo_inimigos.add(inimigo_teste)

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
running_game = True

while running_game:
    clock.tick(60) # Limita os FPS a 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    #Lógica de Game Over simples
    if player.vida <= 0:
        print("GAME OVER")
        running_game = False

    #Atualiza inimigos passando o player (para eles saberem quem perseguir)
    grupo_inimigos.update(player)

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
        # Adicionar colisão do inimigo com paredes aqui futuramente

    #atualiza todos os sprites do grupo do player
    sprites_group.update() 
    
    # Desenha os sprites na janela
    sprites_group.draw(tela)
    grupo_coletaveis.draw(tela) #desenha os coletaveis
    grupo_inimigos.draw(tela)   #Desenha os inimigos
   
    pygame.display.update()

pygame.quit()