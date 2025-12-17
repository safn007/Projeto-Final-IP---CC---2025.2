#teste Samuel comentárioaaw
import pygame
from src.mapas import Mapas
from src.colisoes import Colisoes
from src.coletaveis import Coletavel
from src.player import Player
from src.inimigo import Inimigo 
from src.interface import interface

pygame.init() # Inicia o pygame

largura = 960
altura = 640
mapas = Mapas(largura, altura)
tela = pygame.display.set_mode((largura, altura)) # Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") # Nome que aparece no título da janela

player = Player(250, 250)
player.vida = 3 # Começa com 3 corações

# Criando grupo de inimigos espalhados
grupo_inimigos = pygame.sprite.Group()

posicoes_inimigos = [
    (600, 300), 
    (800, 100), 
    (150, 500), 
    (850, 550) 
]

for pos in posicoes_inimigos:
    # Cria um inimigo para cada posição e adiciona ao grupo
    inimigo = Inimigo(pos[0], pos[1])
    grupo_inimigos.add(inimigo)

grupo_coletaveis = pygame.sprite.Group() # criando os coletaveis
grupo_coletaveis.add(Coletavel("chapeu", 100, 100))
grupo_coletaveis.add(Coletavel("oculos", 150, 100))
grupo_coletaveis.add(Coletavel("carangueijo", 600, 500))
grupo_coletaveis.add(Coletavel("carangueijo", 400, 100))

# variaveis para contagem de coletaveis
qnt_chapeu = 0
qnt_oculos = 0
qnt_carangueijo = 0

# Grupo de sprites
sprites_group = pygame.sprite.Group()
sprites_group.add(player)

clock = pygame.time.Clock() # Cria relogio pra controlar FPS
running_game = True

# Inicializa o sistema de fontes
pygame.font.init() 

# Cria o HUD dos coletaveis
hud = interface()

while running_game:
    clock.tick(60) # Limita os FPS a 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    # Lógica de Game Over 
    if player.vida <= 0:
        print("GAME OVER")
        running_game = False

    # Atualiza inimigos passando o player
    grupo_inimigos.update(player)

    for item in grupo_coletaveis:
        if player.hitbox.colliderect(item.rect):
            item.kill() # remove o item do jogo e do grupo

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

    # troca de mapa 
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
    grupo_inimigos.draw(tela) #Desenha os inimigos
    
    # HUD dos coletaveis
    hud.desenhar_hud(tela, qnt_chapeu, qnt_oculos, qnt_carangueijo, player.vida)
   
    pygame.display.update()

pygame.quit()