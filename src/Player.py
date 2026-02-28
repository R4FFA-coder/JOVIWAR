import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images_player = []
        for c in range(3):
            img = sprite_sheet.subsurface((32 * c, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.images_player.append(img)

        self.current = 0
        self.image = self.images_player[self.current]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.frames = 0
        self.max_frames = 2

    def update(self):
        if self.frames > self.max_frames:
            self.frames = 0
            self.current += 1
        if self.current > len(self.images_player) - 1:
            self.current = 0
        self.frames += 1
        self.image = self.images_player[self.current]
