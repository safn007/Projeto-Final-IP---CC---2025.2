#teste Samuel comentário
import pygame
from src.coletaveis import Coletavel
import os
from src.player import Player

pygame.init() # Inicia o pygame

width = 800
height = 600
screen = pygame.display.set_mode((width, height)) # Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") # Nome que aparece no título da janela

diretory = os.path.dirname(__file__)  # Pega o diretório do arquivo main.py
path = os.path.join(diretory, "Assets", "Imagens", "Imagem_de_fundo.png")  # Caminho até a imagem de fundo

# Fundo
background_original = pygame.image.load(path).convert()
background = pygame.transform.scale(background_original, (width, height))

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

while running_game:
    clock.tick(60) # Limita os FPS a 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False


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

    grupo_coletaveis.draw(janela_jogo) #desenha os coletaveis

    # Atualiza todos os sprites do grupo
    sprites_group.update() 
    
    # Desenha o fundo 
    screen.blit(background, (0, 0))
    
    # Desenha os sprites na janela
    sprites_group.draw(screen)
   
    pygame.display.update()

pygame.quit()