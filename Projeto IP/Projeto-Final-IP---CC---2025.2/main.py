#teste Samuel comentário
import pygame
from src.mapas import Mapas
from src.colisoes import Colisoes
from src.coletaveis import Coletavel
from src.player import Player

pygame.init() # Inicia o pygame

largura = 960
altura = 640
mapas = Mapas(largura, altura)
tela = pygame.display.set_mode((largura, altura)) # Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") # Nome que aparece no título da janela

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
running_game = True

pygame.font.init() # Inicializa o sistema de fontes
fonte_jogo = pygame.font.SysFont('Monocraft', 23, bold=True)
cor_texto = (255, 255, 255) # Branco (R, G, B)

# Carregando UI dos coletaveis
img_chapeu_ui = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Chapeu-Chico-Science.png') # Coloque o caminho certo aqui
img_chapeu_ui = pygame.transform.scale(img_chapeu_ui, (39, 31.5))

img_oculos_ui = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Oculos-Chico-Science.png')
img_oculos_ui = pygame.transform.scale(img_oculos_ui, (48, 24))

img_carangueijo_ui = pygame.image.load("Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Pata-Carangueijo.png")
img_carangueijo_ui = pygame.transform.scale(img_carangueijo_ui, (25.5, 48))

while running_game:
    clock.tick(60) # Limita os FPS a 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False


    for item in grupo_coletaveis:
        if player.rect.colliderect(item.rect):
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
    
    chapeus = fonte_jogo.render(f"Chapéus: {qnt_chapeu}", True, cor_texto)
    oculos = fonte_jogo.render(f"Óculos: {qnt_oculos}", True, cor_texto)
    carangueijo = fonte_jogo.render(f"Carangueijos: {qnt_carangueijo}", True, cor_texto)

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


    # UI dos coletaveis
    tela.blit(img_chapeu_ui, (15, 15))
    texto_chapeu = fonte_jogo.render(f"x {qnt_chapeu}", False, cor_texto)
    tela.blit(texto_chapeu, (60, 15))

    tela.blit(img_oculos_ui, (120, 20))
    texto_oculos = fonte_jogo.render(f"x {qnt_oculos}", False, cor_texto)
    tela.blit(texto_oculos, (175, 15))

    tela.blit(img_carangueijo_ui, (235, 12))
    texto_carangueijo = fonte_jogo.render(f"x {qnt_carangueijo}", False, cor_texto)
    tela.blit(texto_carangueijo, (270, 15))
    
   
    pygame.display.update()

pygame.quit()
