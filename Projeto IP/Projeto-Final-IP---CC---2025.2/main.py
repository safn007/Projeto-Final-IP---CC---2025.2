#teste Samuel comentário
import pygame
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

    # Atualiza todos os sprites do grupo
    sprites_group.update() 
    
    # Desenha o fundo 
    screen.blit(background, (0, 0))
    
    # Desenha os sprites na janela
    sprites_group.draw(screen)
   
    pygame.display.update()

pygame.quit()