#teste Samuel comentárioaaw
import pygame
from src.mapas import Mapas
from src.colisoes import Colisoes
from src.coletaveis import Coletavel
from src.player import Player
from src.inimigo import Inimigo 
from src.interface import interface
from src.tela_inicial import menu_principal

#rodando menu principal
menu_principal()

pygame.init() # Inicia o pygame
pygame.mixer.init()

#baixando os efeitos sonoros
som_coletando_itens = pygame.mixer.Sound("Assets/Efeitos Sonoros/game-start-317318.mp3")
som_gameover = pygame.mixer.Sound("Assets/Efeitos Sonoros/falled-sound-effect-278635.mp3")
alerta_vitoria = pygame.mixer.Sound("Assets/Efeitos Sonoros/winner-game-sound-404167.mp3")
som = True # Variavel para o efeito ser reproduzido apenas uma vez
vitoria = False # mesmo principio de funcionamento de som

largura = 960
altura = 640
mapas = Mapas(largura, altura)
tela = pygame.display.set_mode((largura, altura)) # Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") # Nome que aparece no título da janela

player = Player(250, 250)
player.vida = 3 # Começa com 3 corações

# variaveis para contagem de coletaveis
qnt_chapeu = 0
qnt_oculos = 0
qnt_carangueijo = 0
coletado, chapeu_coletado, oculos_coletado, c1_coletado, c2_coletado, c3_coletado = False, False, False, False, False, False

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

    # Lógica de Game Over 
    if player.vida <= 0:
        if som:
            som = False
            som_gameover.play()

    # desenha mapa
    pos_coletaveis = mapas.desenhar(tela, coletado, chapeu_coletado, oculos_coletado, c1_coletado, c2_coletado, c3_coletado)

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

    # lógica de coleta de itens
    for item in pos_coletaveis:
        if player.hitbox.colliderect(item.rect):
            item.kill() # remove o item do jogo e do grupo
            
            som_coletando_itens.play()
            
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

            elif item.tipo == "carangueijo1":
                print("pegou carangueijo")
                qnt_carangueijo+=1
                coletado = True
                c1_coletado = True

            elif item.tipo == "carangueijo2":
                print("pegou carangueijo")
                qnt_carangueijo+=1
                coletado = True
                c2_coletado = True

            elif item.tipo == "carangueijo3":
                print("pegou carangueijo")
                qnt_carangueijo+=1
                coletado = True
                c3_coletado = True

    if chapeu_coletado and oculos_coletado and not vitoria:
        alerta_vitoria.play()
        vitoria = True
        

    # DESCOMENTAR PARA TESTE DE COLISÕES
    # for coord in colisoes:
    #     caixa = pygame.Rect(coord[0], coord[1], 32, 32)
    #     pygame.draw.rect(tela, '#ff0000', caixa, 1)
        # Adicionar colisão do inimigo com paredes aqui futuramente

    #atualiza todos os sprites do grupo do player
    sprites_group.update() 

    # atualiza a movimentação dos inimigos
    grupo_inimigos.update(player)
    
    # Desenha os sprites na janela
    sprites_group.draw(tela)
    pos_coletaveis.draw(tela) #desenha os coletaveis
    grupo_inimigos.draw(tela) #Desenha os inimigos
    # pygame.draw.rect(tela, '#00ff00', player.hitbox, 1) # DESCOMENTAR PARA TESTAR HITBOX

    # HUD dos coletaveis
    hud.desenhar_hud(tela, qnt_chapeu, qnt_oculos, qnt_carangueijo, player.vida)

    # desenha a camada de árvores
    mapas.desenhar_arvores(tela)
   
    pygame.display.update()

pygame.quit()