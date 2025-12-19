import pygame
import os

pygame.mixer.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Configuracao da animacao
        self.frame_index = 0
        self.animation_speed = 0.15
        self.facing = "down" # Guarda a ultima direcao
        self.status = "idle_down" # Comeca para baixo
        
        self.som_passo = pygame.mixer.Sound("Assets/Efeitos Sonoros/walking-on-grass-363353.mp3") #som do passo
        self.som_passo.set_volume(0.3) # Volume do passo

        # Variável para controlar o ritmo
        self.tempo_ultimo_passo = 0
        self.intervalo_passos = 550 # Milissegundos entre cada passo 

        # Carrega as imagens
        self.animations = {
            "idle_up": [], "run_up": [],
            "idle_down": [], "run_down": [],
            "idle_left": [], "run_left": [],
            "idle_right": [], "run_right": [],
        }
        self.import_assets() # Chama a funcao q carrega as imagens
        
        # Imagem inicial
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = (x, y))
        self.hitbox = self.rect.inflate(-200, -100) # Reduz o hitbox do jogador
        
        # Movimento
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.speed = 2
        self.direction = pygame.math.Vector2(0, 0)
        
    def import_assets(self):
        diretory = os.path.dirname(__file__) # Pega a pasta onde o player.py ta
        path = os.path.join(diretory, "..", "Assets", "Imagens") # Caminho ate a pasta das imagens
        
        def load_animation(name, frames):
            # Recorta sprite sheets 
            
            caminho_completo = os.path.join(path, name)
            # Carrega a imagem inteira
            sheet = pygame.image.load(caminho_completo).convert_alpha()
            
            width_sheet = sheet.get_width()
            height_sheet = sheet.get_height()
            
            # Descobre a largura de um boneco
            frame_width = width_sheet / frames
            
            frame_list = []
            
            for i in range(frames):
                # Define o retângulo de corte
                # O i * frame_width faz o corte andar pra a direita
                crop = (i * frame_width, 0, frame_width, height_sheet)
                
                # Cria o recorte
                frame = sheet.subsurface(crop)
                
                # Redimensiona o frame
                chosen_frame = pygame.transform.scale(frame, (250, 150))

                frame_list.append(chosen_frame)
                
            return frame_list
        
        self.animations["run_up"] = load_animation('run_up.png', 8)
        self.animations["run_down"] = load_animation('run_down.png', 8)
        self.animations["run_left"] = load_animation('run_left.png', 8)
        self.animations["run_right"] = load_animation('run_right.png', 8)
        
        self.animations["idle_up"] = load_animation('idle_up.png', 8) 
        self.animations["idle_down"] = load_animation('idle_down.png', 8)
        self.animations["idle_left"] = load_animation('idle_left.png', 8)
        self.animations["idle_right"] = load_animation('idle_right.png', 8)

    def get_status(self):
        # Decide qual animacao selecionada
        
        # Se o vetor for (0, 0) ele ta parado
        if self.direction.x == 0 and self.direction.y == 0:
            self.status = "idle_" + self.facing
        else:
            self.status = "run_" + self.facing
        
    def input(self):
        # Teclas
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        self.direction.y = 0

        agora = pygame.time.get_ticks()
        andando = False

        # Movimento e definicao de onde olha
        if keys[pygame.K_w]:
            self.direction.y -= 1
            self.facing = "up"
            andando = True
        elif keys[pygame.K_s]:
            self.direction.y += 1
            self.facing = "down"
            andando = True
        elif keys[pygame.K_a]:
            self.direction.x -= 1
            self.facing = "left"
            andando = True
        elif keys[pygame.K_d]:
            self.direction.x += 1
            self.facing = "right"
            andando = True
            
        # Faz nao andar mais rapido na diagonal
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        if andando:
            # Se já passou tempo suficiente desde o último som
            if agora - self.tempo_ultimo_passo > self.intervalo_passos:
                self.tempo_ultimo_passo = agora
                self.som_passo.play()
            
    def animate(self):
        animation = self.animations[self.status]
        
        # Loop da animacao
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
    
    def update(self):
        self.input()
        self.get_status()
        self.animate()

        # colisão horizontal
        self.pos_x += self.direction.x * self.speed
        self.hitbox.centerx = int(self.pos_x + (self.rect.width / 2))
        
        for barreira in self.colisoes:
            if self.hitbox.colliderect(barreira):
                if self.direction.x > 0:
                    self.hitbox.right = barreira.left
                if self.direction.x < 0:
                    self.hitbox.left = barreira.right
                self.pos_x = self.hitbox.centerx - (self.rect.width / 2)

        # colisão vertical
        self.pos_y += self.direction.y * self.speed
        self.hitbox.centery = int(self.pos_y + (self.rect.height / 2)) # Sincroniza hitbox com a nova pos_y

        for barreira in self.colisoes:
            if self.hitbox.colliderect(barreira):
                if self.direction.y > 0:
                    self.hitbox.bottom = barreira.top
                if self.direction.y < 0:
                    self.hitbox.top = barreira.bottom
                self.pos_y = self.hitbox.centery - (self.rect.height / 2)

        self.rect.center = self.hitbox.center