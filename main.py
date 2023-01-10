import pygame
from modules.level import *
import modules.character as character_module
import modules.tile as tile_module

def game(screen, background_game_img):
    # создадим группу, содержащую все спрайты
    FPS = 60
    tick = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player_group.update(event)
        screen.fill((0, 0, 0))
        screen.blit(background_game_img, (0, 0))
        # изменяем ракурс камеры
        camera.update(player, width, height)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.update()

        tiles_group.draw(screen)
        player_group.draw(screen)
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()

def get_platform_group():
    return platform_group


if __name__ == '__main__':
    pygame.init()
    background_game_img = pygame.image.load("../data/background.png")
    size = width, height = 700, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Редиска')
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    lvl = Level('../data/lvl.txt')
    player, level_x, level_y = lvl.generate_level(tile_module, character_module, player_group, tiles_group, platform_group, all_sprites)
    camera = Camera()
    game(screen, background_game_img)