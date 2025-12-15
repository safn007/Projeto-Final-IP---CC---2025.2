import pygame

class Colisoes:
    def __init__(self, blocks):
        self.blocks = blocks

    def coletar_xy(self, num):
        num -= 1
        x = num % 16
        y = int(num / 16)
        return (x * 32, y * 32)

    def criar_colisoes(self):
        coords = []

        for block in self.blocks:
            coord = self.coletar_xy(block)
            coords.append(coord)

        return coords


