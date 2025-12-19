import pygame
import math
import os

pygame.mixer.init()
som_dano_recebido = pygame.mixer.Sound("Assets/Efeitos Sonoros/ough-47202.mp3")

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Tamanho que o inimigo terá na tela
        self.tamanho = 64
        
        # Localiza a pasta das imagens 
        caminho_base = os.path.dirname(os.path.abspath(__file__))
        caminho_imgs = os.path.join(os.path.dirname(caminho_base), 'Assets', 'Imagens')

        # Função simples de carregar e cortar 
        def carregar_animacao(nome_arquivo):
            arquivo = os.path.join(caminho_imgs, nome_arquivo)
            sheet = pygame.image.load(arquivo).convert_alpha()
            
            largura_frame = sheet.get_width() // 4
            altura_frame = sheet.get_height()
            
            frames = []
            for i in range(4):
                pos_x = i * largura_frame
                corte = sheet.subsurface((pos_x, 0, largura_frame, altura_frame))
                img_final = pygame.transform.scale(corte, (self.tamanho, self.tamanho))
                frames.append(img_final)
                
            return frames

        # Carrega as 4 direções
        self.anim_cima     = carregar_animacao('sprite_caranguejo_costas.png')
        self.anim_baixo    = carregar_animacao('sprite_caranguejo_frente_final.png')
        self.anim_esquerda = carregar_animacao('sprite_caranguejo_esquerda.png')
        self.anim_direita  = carregar_animacao('sprite_caranguejo_direita.png')

        # Configuração inicial
        self.animacao_atual = self.anim_baixo
        self.frame_index = 0
        self.image = self.animacao_atual[self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Variáveis para o movimento 0.9
        self.x_real = float(x)
        self.y_real = float(y)

        # Hitbox menor para bater só de perto
        self.rect = self.image.get_rect(topleft = (x, y))
        self.hitbox = self.rect.inflate(-20, -20)

        # Status
        self.velocidade = 0.9 
        self.raio_alerta = 250
        self.dano = 1 
        
        # Controles de tempo
        self.ultimo_ataque = 0
        self.timer_animacao = 0

    def update(self, player):
        # Calcula distância
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distancia = math.hypot(dx, dy)
        
        andando = False

        # Perseguição
        if 0 < distancia < self.raio_alerta:
            andando = True
            
            # Move na direção do player
            self.x_real += (dx / distancia) * self.velocidade
            self.y_real += (dy / distancia) * self.velocidade
            
            # Impedir que saia do mapa
            if self.x_real < 0: self.x_real = 0
            if self.x_real > 960 - self.tamanho: self.x_real = 960 - self.tamanho
            if self.y_real < 0: self.y_real = 0
            if self.y_real > 640 - self.tamanho: self.y_real = 640 - self.tamanho

            # Passa a posição real para o jogo
            self.rect.x = int(self.x_real)
            self.rect.y = int(self.y_real)
            self.hitbox.center = self.rect.center # Atualiza hitbox

            # Escolhe a animação baseada na maior distância
            if abs(dx) > abs(dy):
                if dx > 0: self.animacao_atual = self.anim_direita
                else:      self.animacao_atual = self.anim_esquerda
            else:
                if dy > 0: self.animacao_atual = self.anim_baixo
                else:      self.animacao_atual = self.anim_cima

        # Gerencia a Animação
        if andando:
            agora = pygame.time.get_ticks()
            if agora - self.timer_animacao > 150: 
                self.timer_animacao = agora
                self.frame_index += 1
                if self.frame_index >= 4:
                    self.frame_index = 0
                self.image = self.animacao_atual[self.frame_index]
        else:
            self.image = self.animacao_atual[0] 

        # Ataque
        if self.hitbox.colliderect(player.hitbox):
            agora = pygame.time.get_ticks()
            if agora - self.ultimo_ataque > 1000: # 1 segundo de cooldown
                self.ultimo_ataque = agora
                if hasattr(player, 'vida'):
                    if player.vida != 0:
                        player.vida -= self.dano
                        som_dano_recebido.play()
                        print(f"Dano! Vida atual: {player.vida}")