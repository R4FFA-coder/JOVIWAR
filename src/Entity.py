from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, postition: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png')
        self.rect = self.surf.get_rect(left= postition[0],top= postition[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
