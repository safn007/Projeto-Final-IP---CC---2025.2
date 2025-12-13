import pygame
from src.player import Player

width = 800
height = 600
screen = pygame.display.set_mode((width, height)) #Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") #Nome que aparece no título da janela

background_original = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Imagem_de_fundo.png')
background = pygame.transform.scale(background_original, (width, height))

player_image = 'Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Personagem-removebg-preview.png'
player = Player(250, 250, player_image)

# Grupo de sprites
sprites_group = pygame.sprite.Group()
sprites_group.add(player)

running_game = True
while running_game:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running_game = False

    # Atualiza todos os sprites do grupo
    sprites_group.update() 
    
    # Desenha o fundo 
    screen.blit(background, (0, 0))
    
    # Desenha os sprites na janela
    sprites_group.draw(screen)
   
    pygame.display.update()

