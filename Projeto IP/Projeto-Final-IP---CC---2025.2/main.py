#teste Samuel comentárioaaw
import pygame
from src.mapas import Mapas
from src.colisoes import Colisoes
from src.player import Player
from src.inimigo import Inimigo
from src.interface import interface

pygame.init() # Inicia o pygame

largura = 960
altura = 640
mapas = Mapas(largura, altura)
tela = pygame.display.set_mode((largura, altura)) # Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") # Nome que aparece no título da janela

player = Player(250, 250, [])
player.vida = 3 # Começa com 3 corações

# variaveis para contagem de coletaveis
qnt_chapeu = 0
qnt_oculos = 0
qnt_carangueijo = 0
coletado, chapeu_coletado, oculos_coletado = False, False, False

# Grupo de sprites
sprites_group = pygame.sprite.Group()
sprites_group.add(player)

clock = pygame.time.Clock() # Cria relogio pra controlar FPS
running_game = True

# Inicializa o sistema de fontes
pygame.font.init() 

# Cria o HUD dos coletaveis
hud = interface()

# variável para inicializar os mapas
inicializar = True

while running_game:
    clock.tick(60) # Limita os FPS a 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
    
    # desenha mapa
    pos_coletaveis = mapas.desenhar(tela, coletado, chapeu_coletado, oculos_coletado)

    # troca de mapa/ inicializa colisões e inimigos
    mapa_antigo = mapas.mapa_atual
    mapas.trocar_mapa(player)
    if mapa_antigo != mapas.mapa_atual or inicializar == True:
        coletado = False       
        inicializar = False
        # coletar colisões
        atual = mapas.mapa_atual
        colisoes = Colisoes([])
        colisoes = colisoes.lista_colisoes(atual)
        player.colisoes = colisoes  

        pos_inimigos = mapas.get_inimigos()
        grupo_inimigos = pygame.sprite.Group() 
        for pos in pos_inimigos:
            # Cria um inimigo para cada posição e adiciona ao grupo
            inimigo = Inimigo(pos[0], pos[1])
            grupo_inimigos.add(inimigo)

    # Lógica de Game Over 
    if player.vida <= 0:
        print("GAME OVER")
        running_game = False

    # Atualiza inimigos passando o player
    grupo_inimigos.update(player)

    for item in pos_coletaveis:
        if player.hitbox.colliderect(item.rect):
            item.kill() # remove o item do jogo e do grupo
            
            if item.tipo == "chapeu":
                print("pegou chapeu")
                qnt_chapeu+=1
                coletado = True
                chapeu_coletado = True

            elif item.tipo == "oculos":
                print("pegou oculos")
                qnt_oculos+=1
                coletado = True
                oculos_coletado = True

            elif item.tipo == "carangueijo":
                print("pegou carangueijo")
                qnt_carangueijo+=1
                coletado = True

    # for coord in colisoes:
    #     caixa = pygame.Rect(coord[0], coord[1], 32, 32)
    #     pygame.draw.rect(tela, '#ff0000', caixa, 1)
        # Adicionar colisão do inimigo com paredes aqui futuramente

    #atualiza todos os sprites do grupo do player
    sprites_group.update() 
    
    # Desenha os sprites na janela
    sprites_group.draw(tela)
    pos_coletaveis.draw(tela) #desenha os coletaveis
    grupo_inimigos.draw(tela) #Desenha os inimigos
    # pygame.draw.rect(tela, '#00ff00', player.hitbox, 1)

    # HUD dos coletaveis
    hud.desenhar_hud(tela, qnt_chapeu, qnt_oculos, qnt_carangueijo, player.vida)
    
    # desenha a camada de árvores
    mapas.desenhar_arvores(tela)

    pygame.display.update()

pygame.quit()