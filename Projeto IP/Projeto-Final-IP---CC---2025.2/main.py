import pygame
from src.player import Player
from src.mapas import Mapas
from src.colisoes import Colisoes

pygame.init()

largura = 960
altura = 640
janela_jogo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Nome do jogo")

clock = pygame.time.Clock()

mapas = Mapas(largura, altura)

player_image = 'Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Personagem-removebg-preview.png'
player = Player(250, 250, player_image)

sprites_group = pygame.sprite.Group(player)

running_game = True
while running_game:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    # desenha mapa
    mapas.desenhar(janela_jogo)

    # troca de mapa (altera o rect diretamente)
    mapas.trocar_mapa(player.rect)

    # sincroniza posição lógica com o rect
    player.pos.x = player.rect.centerx
    player.pos.y = player.rect.centery

    # coletar colisões
    colisoes = Colisoes([3, 5, 9, 11, 241])
    colisoes = colisoes.criar_colisoes()
    for coord in colisoes:
        caixa = pygame.Rect(coord[0], coord[1], 32, 32)

    # atualiza sprites
    sprites_group.update()

    # desenha sprites
    sprites_group.draw(janela_jogo)

    pygame.display.update()

pygame.quit()
