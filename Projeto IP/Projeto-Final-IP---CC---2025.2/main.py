import pygame

janela_jogo = pygame.display.set_mode((800, 600)) #Define o tamanho da janela do jogo
pygame.display.set_caption("Nome do jogo") #Nome que aparece no título da janela

rodar_jogo = True
while rodar_jogo:

    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            rodar_jogo = False

    pygame.display.update()

