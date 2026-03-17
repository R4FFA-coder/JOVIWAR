from sys import exit
from pygame.locals import *
from src.Const import *
from src.Enemy import Enemy
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
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        self.player = Player()
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIMER)
        self.entity_list.append(EntityFactory.get_entity('Enemy'))
        self.entity_list.append(self.player)

    def run(self, ):
        pygame.mixer_music.load(BGML2)
        pygame.mixer_music.play(-1, fade_ms=1500)
        pygame.mixer_music.set_volume(0.45)
        clock = pygame.time.Clock()
        countdown_timer = pygame.USEREVENT + 1
        countdown = 120
        pygame.time.set_timer(countdown_timer, 1000)
        todas_as_sprites = pygame.sprite.Group()

        for i in range(LARGURA // 100 + 2):
            chao = Platform(i)
            todas_as_sprites.add(chao)

        todas_as_sprites.add(self.player)

        while True:
            clock.tick(30)
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
                if isinstance(ent, Enemy):
                    shot = ent.atirar()
                    if shot is not None:
                        self.entity_list.append(shot)

            todas_as_sprites.draw(self.window)
            todas_as_sprites.update()

            self.text_level(f'Timeout= {countdown}', 20, (100, 30))
            self.text_level(f'Entitys = {len(self.entity_list)}', 20, (LARGURA // 2, 30))
            self.text_level(f'FPS: {clock.get_fps():.0f}', 12, (LARGURA - 100, 20))
            self.text_level(f'SCORE: {self.player.score}', 20, (LARGURA - 100, 40))
            if self.name == 'Level_infinite':
                pass
            else:
                self.text_level2(ORANGE,f'player health: {self.player.health}', 20, (100, 60))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == EVENT_ENEMY:
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
                        if self.player.rect.y != self.player.pos_y_inicial:
                            pass
                        else:
                            self.player.pular()
                    if self.player.rect.y == self.player.pos_y_inicial:
                        if event.key == K_RCTRL or event.key == K_LCTRL:
                            player_shot = self.player.atirar()
                            self.entity_list.append(player_shot)
            if self.player.health <= 0:
                if self.name == 'Level_infinite':
                    pass
                else:
                    print('VOCE MORREU')
                    print(f'Pontuação Final ->  {self.player.score} Pontos')
                    break

            # verificar colisoes e a vida
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def text_level(self, text: str, size: int, text_center_pos: tuple):
        text_font = pygame.font.Font(FONT_PATH_ITALLIC, size=size)  # padroniza uma fonte e o tamanho
        text_surf = text_font.render(text, True, WHITE).convert_alpha()  # Renderiza o texto
        text_rect = text_surf.get_rect(
            center=text_center_pos)  # Desenha um retangulo que será a área em que o texto ocupará
        self.window.blit(source=text_surf, dest=text_rect)  # carrega o texto e imprime na area do retangulo

    def text_level2(self,color,  text: str, size: int, text_center_pos: tuple):
        text_font = pygame.font.Font(FONT_PATH_BOLD, size=size)
        text_surf = text_font.render(text, True, color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
