from sys import exit
import pygame
from pygame.locals import *
from src.Const import *
from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.EntityMediator import EntityMediator
from src.Menu import Menu
from src.Platform import Platform
from src.Player import Player


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1'))

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIMER)
        self.entity_list.append(EntityFactory.get_entity('Enemy'))

    def run(self, ):
        pygame.mixer_music.load(BGML2)
        pygame.mixer_music.play(-1, fade_ms=1500)
        pygame.mixer_music.set_volume(0.45)
        clock = pygame.time.Clock()
        countdown_timer = pygame.USEREVENT + 1
        countdown = 120
        pygame.time.set_timer(countdown_timer, 1000)
        todas_as_sprites = pygame.sprite.Group()

        player = Player()
        for i in range(LARGURA // 100 + 2):
            chao = Platform(i)
            todas_as_sprites.add(chao)

        todas_as_sprites.add(player)

        while True:
            clock.tick(30)
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            todas_as_sprites.draw(self.window)
            todas_as_sprites.update()
            self.text_level(f'Timeout= {countdown}', 20, (100, 30))
            self.text_level(f'Entitys = {len(self.entity_list)}', 20, (LARGURA //2, 30))

            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == EVENT_ENEMY:
                    # if len(self.entity_list) > 12: # Criei uma condição para limitar o numero de objetos Enemy criados (Poupar recursos)
                    #     continue
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == countdown_timer:
                    countdown -= 1
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = Menu(self.window)
                        menu.run()
                    if event.key == K_SPACE:
                        if player.rect.y != player.pos_y_inicial:
                            pass
                        else:
                            player.pular()
                    elif event.key == K_LCTRL or K_RCTRL:
                        print('ATIRANDO!')
                        # player.atirar()

            # verificar colisoes e a vida
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def text_level(self, text: str, size: int, text_center_pos: tuple):
        text_font = pygame.font.Font(FONT_PATH_ITALLIC, size=size)  # padroniza uma fonte e o tamanho
        text_surf = text_font.render(text, True, WHITE).convert_alpha()  # Renderiza o texto
        text_rect = text_surf.get_rect(center=text_center_pos)  # Desenha um retangulo que será a área em que o texto ocupará
        self.window.blit(source=text_surf, dest=text_rect)  # carrega o texto e imprime na area do retangulo