import pygame
import math
import os

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Tamanho que o inimigo terá na tela
        self.tamanho = 64
        
        # --- Localiza a pasta das imagens ---
        caminho_base = os.path.dirname(os.path.abspath(__file__))
        # Sobe uma pasta (src -> Projeto) e entra em Assets/Imagens
        caminho_imgs = os.path.join(os.path.dirname(caminho_base), 'Assets', 'Imagens')

        # --- Função simples de carregar e cortar ---
        def carregar_animacao(nome_arquivo):
            # Monta o caminho e carrega a imagem
            arquivo = os.path.join(caminho_imgs, nome_arquivo)
            sheet = pygame.image.load(arquivo).convert_alpha()
            
            # Descobre o tamanho de cada quadro (largura total / 4)
            largura_frame = sheet.get_width() // 4
            altura_frame = sheet.get_height()
            
            frames = []
            for i in range(4):
                # Recorta o pedaço (X muda a cada loop, Y é sempre 0)
                pos_x = i * largura_frame
                corte = sheet.subsurface((pos_x, 0, largura_frame, altura_frame))
                
                # Aumenta para o tamanho final (64x64)
                img_final = pygame.transform.scale(corte, (self.tamanho, self.tamanho))
                frames.append(img_final)
                
            return frames

        # --- Carrega as 4 direções ---
        # Certifique-se que os nomes estão CORRETOS na pasta
        self.anim_cima     = carregar_animacao('sprite_caranguejo_costas.png')
        self.anim_baixo    = carregar_animacao('sprite_caranguejo_frente_final.png')
        self.anim_esquerda = carregar_animacao('sprite_caranguejo_esquerda.png')
        self.anim_direita  = carregar_animacao('sprite_caranguejo_direita.png')

        # Configuração inicial
        self.animacao_atual = self.anim_baixo
        self.frame_index = 0
        self.image = self.animacao_atual[self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Hitbox menor para bater só de perto
        self.hitbox = self.rect.inflate(-30, -30)

        # Status
        self.velocidade = 2
        self.raio_alerta = 250
        self.dano = 10
        
        # Controles de tempo
        self.ultimo_ataque = 0
        self.timer_animacao = 0

    def update(self, player):
        # 1. Calcula distância
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distancia = math.hypot(dx, dy)
        
        andando = False

        # 2. Perseguição
        if 0 < distancia < self.raio_alerta:
            andando = True
            
            # Move na direção do player
            self.rect.x += (dx / distancia) * self.velocidade
            self.rect.y += (dy / distancia) * self.velocidade
            self.hitbox.center = self.rect.center # Atualiza hitbox

            # Escolhe a animação baseada na maior distância (X ou Y)
            if abs(dx) > abs(dy):
                if dx > 0: self.animacao_atual = self.anim_direita
                else:      self.animacao_atual = self.anim_esquerda
            else:
                if dy > 0: self.animacao_atual = self.anim_baixo
                else:      self.animacao_atual = self.anim_cima

        # 3. Gerencia a Animação
        if andando:
            agora = pygame.time.get_ticks()
            if agora - self.timer_animacao > 150: # Velocidade da troca (ms)
                self.timer_animacao = agora
                self.frame_index += 1
                if self.frame_index >= 4:
                    self.frame_index = 0
                self.image = self.animacao_atual[self.frame_index]
        else:
            self.image = self.animacao_atual[0] # Fica parado no frame 0

        # 4. Ataque
        if self.hitbox.colliderect(player.rect):
            agora = pygame.time.get_ticks()
            if agora - self.ultimo_ataque > 1000: # 1 segundo de cooldown
                self.ultimo_ataque = agora
                if hasattr(player, 'vida'):
                    player.vida -= self.dano
                    print(f"Dano! Vida atual: {player.vida}")