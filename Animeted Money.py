import os
import sys
import pygame



class Character(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, *groups):
        super().__init__(*groups)
        self.frames = []
        self.frames_idle = []
        self.frames_walk = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.cur_frame_walk = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def game(screen):
    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    Character(load_image("12.png"), 5, 2, 10, 10, player_group, all_sprites)
    FPS = 10
    tick = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        player_group.update()
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()


# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
game(screen)