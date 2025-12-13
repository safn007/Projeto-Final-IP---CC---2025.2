import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        
        # Carrega e transforma a imagem
        player_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(player_image, (250, 150))
        
        # Hitbox para posicionamento e colisoes
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        # Posicao
        self.pos_x = float(x)
        self.pos_y = float(y)
        
        # Movimento
        self.speed = 0.5
        self.direction = pygame.math.Vector2(0, 0)
        
    def input(self):
        # Teclas
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        self.direction.y = 0
        
        if keys[pygame.K_w]:
            self.direction.y -= 1
        if keys[pygame.K_s]:
            self.direction.y += 1
        if keys[pygame.K_a]:
            self.direction.x -= 1
        if keys[pygame.K_d]:
            self.direction.x += 1
            
        # Faz nao andar mais rapido na diagonal
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
    
    def update(self):
        self.input() # Chama a funcao input
        
        # Atualiza posicao
        self.pos_x += self.direction.x * self.speed
        self.pos_y += self.direction.y * self.speed
        
        # Atualiza o rect -> que é o que o Pygame desenha na tela
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)
    
        