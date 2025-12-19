import pygame

class interface():
    def __init__(self):
        # Carrega a Fonte 
        self.fonte_maior = pygame.font.Font('Assets/Fontes/MONOCRAFT.TTC', 23)
        self.fonte_menor = pygame.font.Font('Assets/Fontes/MONOCRAFT.TTC', 12)
        
        # Carrega as Imagens dos ícones
        img_chapeu = pygame.image.load('Assets/Imagens/Chapeu-Chico-Science.png').convert_alpha()
        self.icone_chapeu = pygame.transform.scale(img_chapeu, (39, 31.5))

        img_oculos = pygame.image.load('Assets/Imagens/Oculos-Chico-Science.png').convert_alpha()
        self.icone_oculos = pygame.transform.scale(img_oculos, (48, 24))

        img_carangueijo = pygame.image.load('Assets/Imagens/Pata-Carangueijo.png').convert_alpha()
        self.icone_carangueijo = pygame.transform.scale(img_carangueijo, (25.5, 48))

        img_vida = pygame.image.load('Assets/Imagens/vida-jogador.png').convert_alpha()
        self.icone_vida = pygame.transform.scale(img_vida, (33, 31.5))

        # Cores
        self.BRANCO = (255, 255, 255)
        self.PRETO = (0, 0, 0)

    def _desenhar_texto_com_borda(self, tela, texto, x, y, fonte=None):
        if fonte == None:
            fonte = self.fonte_maior
            grossura = 2
        else:
            fonte = self.fonte_menor
            grossura = 1
        # Renderiza a borda preta
        img_borda = fonte.render(texto, False, self.PRETO)
        
        # Desenha a sombra em várias direções
        for dx in range(-grossura, grossura + 1):
            for dy in range(-grossura, grossura + 1):
                if dx != 0 or dy != 0:
                    tela.blit(img_borda, (x + dx, y + dy))

        # Renderiza o texto principal branco
        img_texto = fonte.render(texto, False, self.BRANCO)
        tela.blit(img_texto, (x, y))

    def desenhar_hud(self, tela, qnt_chapeu, qnt_oculos, qnt_carangueijo, qnt_vidas):
        # Chapéu
        tela.blit(self.icone_chapeu, (15, 15)) # Desenha ícone
        self._desenhar_texto_com_borda(tela, f"x {qnt_chapeu}", 60, 15) # Desenha texto

        # Óculos
        tela.blit(self.icone_oculos, (120, 20))
        self._desenhar_texto_com_borda(tela, f"x {qnt_oculos}", 175, 15) 

        # Caranguejo
        tela.blit(self.icone_carangueijo, (235, 12))
        self._desenhar_texto_com_borda(tela, f"x {qnt_carangueijo}", 270, 15)
        self._desenhar_texto_com_borda(tela, f"velocidade", 260, 45, self.fonte_menor)
        
        # Vidas
        tela.blit(self.icone_vida, (850, 13))
        self._desenhar_texto_com_borda(tela, f"x {qnt_vidas}", 895, 15)