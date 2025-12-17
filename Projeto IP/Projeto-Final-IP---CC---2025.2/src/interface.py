import pygame

class interface():
    def __init__(self):
        # Carrega a Fonte (ajuste o caminho se necessário)
        self.fonte = pygame.font.Font('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Fontes/MONOCRAFT.TTC', 23)
        
        # Carrega as Imagens dos ícones
        img_chapeu = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Chapeu-Chico-Science.png')
        self.icone_chapeu = pygame.transform.scale(img_chapeu, (39, 31.5))

        img_oculos = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Oculos-Chico-Science.png')
        self.icone_oculos = pygame.transform.scale(img_oculos, (48, 24))

        img_carangueijo = pygame.image.load('Projeto IP/Projeto-Final-IP---CC---2025.2/Assets/Imagens/Pata-Carangueijo.png')
        self.icone_carangueijo = pygame.transform.scale(img_carangueijo, (25.5, 48))
        # Cores
        self.BRANCO = (255, 255, 255)
        self.PRETO = (0, 0, 0)

    def _desenhar_texto_com_borda(self, tela, texto, x, y):
        grossura = 2
        
        # Renderiza a borda preta
        img_borda = self.fonte.render(texto, False, self.PRETO)
        
        # Desenha a sombra em várias direções
        for dx in range(-grossura, grossura + 1):
            for dy in range(-grossura, grossura + 1):
                if dx != 0 or dy != 0:
                    tela.blit(img_borda, (x + dx, y + dy))

        # Renderiza o texto principal branco
        img_texto = self.fonte.render(texto, False, self.BRANCO)
        tela.blit(img_texto, (x, y))

    def desenhar_hud(self, tela, qnt_chapeu, qnt_oculos, qnt_carangueijo):
        # --- ITEM 1: CHAPÉU ---
        tela.blit(self.icone_chapeu, (15, 15)) # Desenha ícone
        self._desenhar_texto_com_borda(tela, f"x {qnt_chapeu}", 60, 15) # Desenha texto

        # --- ITEM 2: ÓCULOS ---
        tela.blit(self.icone_oculos, (120, 20))
        self._desenhar_texto_com_borda(tela, f"x {qnt_oculos}", 175, 15) 

        # --- ITEM 3: CARANGUEIJO ---
        tela.blit(self.icone_carangueijo, (235, 12))
        self._desenhar_texto_com_borda(tela, f"x {qnt_carangueijo}", 270, 15)