#teste Samuel comentárioaaw
import pygame
from src.mapas import Mapas
from src.colisoes import Colisoes
from src.player import Player
from src.inimigo import Inimigo 
from src.interface import interface
from src.tela_inicial import menu_principal
from src.telas_finais import tela_game_over
from src.telas_finais import tela_vitoria


#rodando menu principal
menu_principal()

pygame.init() # Inicia o pygame
pygame.mixer.init()

#baixando os efeitos sonoros
som_coletando_itens = pygame.mixer.Sound("Assets/Efeitos Sonoros/game-start-317318.mp3")
som_coletando_patas = pygame.mixer.Sound("Assets/Efeitos Sonoros/high-speed-02-192899.mp3")
som_gameover = pygame.mixer.Sound("Assets/Efeitos Sonoros/falled-sound-effect-278635.mp3")
alerta_vitoria = pygame.mixer.Sound("Assets/Efeitos Sonoros/winner-game-sound-404167.mp3")
som = True # Variavel para o efeito ser reproduzido apenas uma vez
vitoria = False # mesmo principio de funcionamento de som

largura = 960
altura = 640
mapas = Mapas(largura, altura)
tela = pygame.display.set_mode((largura, altura)) # Define o tamanho da janela do jogo
pygame.display.set_caption("Uma aventura Manguebeat") # Nome que aparece no título da janela

player = Player(230, 250)
player.vida = 3 # Começa com 3 corações

# variaveis para contagem de coletaveis
qnt_chapeu = 0
qnt_oculos = 0
qnt_carangueijo = 0

chapeu_coletado = oculos_coletado = coracao1_coletado = coracao2_coletado = c1_coletado = c2_coletado = c3_coletado = False

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
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(f"Coordenada atual: X={mouse_x}, Y={mouse_y}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    # Lógica de Game Over 
    if player.vida <= 0:
        if som:
            som = False
            som_gameover.play()
        tela_game_over()

    # desenha mapa
    pos_coletaveis = mapas.desenhar(tela, chapeu_coletado, oculos_coletado, coracao1_coletado, coracao2_coletado, c1_coletado, c2_coletado, c3_coletado)

    # troca de mapa/ inicializa colisões e inimigos
    mapa_antigo = mapas.mapa_atual
    mapas.trocar_mapa(player)
    if mapa_antigo != mapas.mapa_atual or inicializar == True:  
        inicializar = False
        # coletar colisões
        atual = mapas.mapa_atual
        colisoes = Colisoes([])
        colisoes = colisoes.lista_colisoes(atual, chapeu_coletado, oculos_coletado)

        pos_inimigos = mapas.get_inimigos()
        grupo_inimigos = pygame.sprite.Group() 
        for pos in pos_inimigos:
            # Cria um inimigo para cada posição e adiciona ao grupo
            inimigo = Inimigo(pos[0], pos[1])
            grupo_inimigos.add(inimigo)
        
        player.colisoes = colisoes  

    # aumentar velocidade de acordo com numero de patas
    if qnt_carangueijo == 1:
        player.speed = 2.33
    if qnt_carangueijo == 2:
        player.speed = 2.66
    if qnt_carangueijo == 3:
        player.speed = 3

    # lógica de coleta de itenssss
    for item in pos_coletaveis:
        if player.hitbox.colliderect(item.rect):
            item.kill() # remove o item do jogo e do grupo
            
            if "carangueijo" in item.tipo:
                som_coletando_patas.play()
            else:
                som_coletando_itens.play()
            if item.tipo == "coracao1":
                print("pegou vida") 
                if player.vida < 3: 
                    player.vida += 1
                coracao1_coletado = True

            if item.tipo == "coracao2":
                if player.vida < 3:  
                    player.vida += 1
                coracao2_coletado = True
            
            elif item.tipo == "chapeu":
                qnt_chapeu+=1
                chapeu_coletado = True

            elif item.tipo == "oculos":
                qnt_oculos+=1
                oculos_coletado = True

            elif item.tipo == "carangueijo1":
                qnt_carangueijo+=1
                c1_coletado = True

            elif item.tipo == "carangueijo2":
                qnt_carangueijo+=1
                c2_coletado = True

            elif item.tipo == "carangueijo3":
                qnt_carangueijo+=1
                c3_coletado = True

    if chapeu_coletado and oculos_coletado and not vitoria:
        alerta_vitoria.play()
        vitoria = True

    # criar retangulo da vitoria
    if mapas.mapa_atual == 6:
        vitoria = pygame.Rect(450, 350, 32, 32)

        if player.hitbox.colliderect(vitoria):
            tela_vitoria()
            
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