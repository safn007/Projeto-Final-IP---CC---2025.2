import pygame

from src.mapas import Mapas
from src.colisoes import Colisoes
from src.coletaveis import Coletavel
from src.player import Player
from src.inimigo import Inimigo
from src.interface import Interface

pygame.init()
pygame.font.init()

LARGURA = 960
ALTURA = 640
FPS = 60

# Cria a janela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo")
clock = pygame.time.Clock()

# Carrega mapa e interface
mapas = Mapas(LARGURA, ALTURA)
hud = Interface()

# Cria o jogador
player = Player(250, 250)

# Garante que o player tenha os atributos básicos
if not hasattr(player, 'rect'):
    player.rect = pygame.Rect(250, 250, 32, 48)
if not hasattr(player, 'hitbox'):
    player.hitbox = player.rect.copy()
if not hasattr(player, 'vida'):
    player.vida = 3
if not hasattr(player, 'invulneravel'):
    player.invulneravel = False
if not hasattr(player, 'invencibilidade_timer'):
    player.invencibilidade_timer = 0

# Grupo de inimigos
grupo_inimigos = pygame.sprite.Group()
posicoes_inimigos = [(600, 300), (800, 100), (150, 500), (850, 550)]
for x, y in posicoes_inimigos:
    grupo_inimigos.add(Inimigo(x, y))

# Grupo de itens coletáveis
grupo_coletaveis = pygame.sprite.Group()
grupo_coletaveis.add(Coletavel("chapeu", 100, 100))
grupo_coletaveis.add(Coletavel("oculos", 150, 100))
grupo_coletaveis.add(Coletavel("carangueijo", 600, 500))
grupo_coletaveis.add(Coletavel("carangueijo", 400, 100))

# Inventário do jogador
inventario = {
    "chapeu": 0,
    "oculos": 0,
    "carangueijo": 0
}

# Gerenciador de colisões com paredes
col_manager = Colisoes([3, 5, 9, 11, 241])
parede_rects = []

# Atualiza as paredes do mapa
def atualizar_paredes():
    global parede_rects
    try:
        coords = col_manager.criar_colisoes()
        if coords and len(coords[0]) >= 4:
            parede_rects = [pygame.Rect(x, y, w, h) for x, y, w, h in coords]
        else:
            parede_rects = [pygame.Rect(x, y, 32, 32) for x, y in coords]
    except:
        parede_rects = []

atualizar_paredes()
last_map_id = mapas.current_map if hasattr(mapas, 'current_map') else None

# Impede o personagem de atravessar a parede
def bloquear_movimento(sprite, pos_anterior):
    if not hasattr(sprite, 'rect'):
        return

    rect_colisao = sprite.hitbox if hasattr(sprite, 'hitbox') else sprite.rect

    for parede in parede_rects:
        if rect_colisao.colliderect(parede):
            sprite.rect.topleft = pos_anterior
            if hasattr(sprite, 'hitbox'):
                sprite.hitbox.topleft = sprite.rect.topleft
            return

# Loop principal do jogo
running = True
while running:
    dt = clock.tick(FPS)
    delta_time = dt / 1000

    # Eventos (teclado, fechar janela, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if hasattr(player, 'handle_event'):
            player.handle_event(event)

    # Verifica se o jogador morreu
    if player.vida <= 0:
        print("GAME OVER")
        running = False
        continue

    # Troca de mapa
    try:
        mapa_mudou = mapas.trocar_mapa(player)
    except:
        mapa_mudou = False

    current_map_id = mapas.current_map if hasattr(mapas, 'current_map') else None
    if mapa_mudou or current_map_id != last_map_id:
        atualizar_paredes()
        last_map_id = current_map_id

    # Guarda posição antiga para colisão
    pos_player_antiga = player.rect.topleft
    pos_inimigos_antiga = {id(i): i.rect.topleft for i in grupo_inimigos}

    # Atualiza os objetos
    player.update()
    grupo_inimigos.update(player)
    grupo_coletaveis.update()

    # Colisão com paredes
    bloquear_movimento(player, pos_player_antiga)
    for inimigo in grupo_inimigos:
        bloquear_movimento(inimigo, pos_inimigos_antiga[id(inimigo)])

    # Sincroniza hitbox
    if hasattr(player, 'hitbox'):
        player.hitbox.topleft = player.rect.topleft

    # Coleta de itens
    for coletavel in grupo_coletaveis.copy():
        if player.rect.colliderect(coletavel.rect):
            tipo = coletavel.tipo
            inventario[tipo] += 1
            print(f"Pegou {tipo}")
            grupo_coletaveis.remove(coletavel)

    # Dano dos inimigos
    if not player.invulneravel:
        for inimigo in grupo_inimigos:
            if player.rect.colliderect(inimigo.rect):
                player.vida -= 1
                player.invulneravel = True
                player.invencibilidade_timer = 1
                break

    # Tempo de invencibilidade
    if player.invulneravel:
        player.invencibilidade_timer -= delta_time
        if player.invencibilidade_timer <= 0:
            player.invulneravel = False

    # Desenho na tela
    tela.fill((0, 0, 0))
    mapas.desenhar(tela)
    grupo_coletaveis.draw(tela)
    grupo_inimigos.draw(tela)

    # Pisca quando toma dano
    if not player.invulneravel or pygame.time.get_ticks() % 200 < 100:
        tela.blit(player.image, player.rect)

    # Desenha HUD
    hud.desenhar_hud(
        tela,
        inventario["chapeu"],
        inventario["oculos"],
        inventario["carangueijo"],
        player.vida
    )

    pygame.display.update()

pygame.quit()
