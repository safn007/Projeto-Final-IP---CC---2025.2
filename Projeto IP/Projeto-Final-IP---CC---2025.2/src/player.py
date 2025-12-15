import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        
        # imagem
        player_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(player_image, (180, 120))
        
        # rect SEMPRE baseado no centro
        self.rect = self.image.get_rect(center=(x, y))
        
        # posição lógica (float)
        self.pos = pygame.math.Vector2(x, y)
        
        # movimento
        self.speed = 3
        self.direction = pygame.math.Vector2(0, 0)
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.update(0, 0)
        
        if keys[pygame.K_w]:
            self.direction.y -= 1
        if keys[pygame.K_s]:
            self.direction.y += 1
        if keys[pygame.K_a]:
            self.direction.x -= 1
        if keys[pygame.K_d]:
            self.direction.x += 1
            
        # normaliza para não andar mais rápido na diagonal
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
    
    def update(self):
        self.input()
        # move
        self.pos += self.direction * self.speed
        
        # atualiza rect
        self.rect.center = self.pos
