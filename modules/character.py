import pygame
from main import get_platform_group


class Radish(pygame.sprite.Sprite):
    is_alive = True
    is_jump = False
    power_jump = 20
    gravity = 1
    coins = 0
    is_in_house = False

    def __init__(self, image, pos, size, speed, *group):
        super().__init__(*group)
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect().move(
            size[0] * pos[0] + 15, size[1] * pos[1] + 5)

    def walk(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.rect.x -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.rect.x += self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            self.rect.y -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            self.rect.y += self.speed

    def is_alive(self):
        pass

    def die(self):
        pass

    def jump(self):
        pass

    def stop_jump(self):
        pass

    def pick_up_coins(self, группа_монет):
        pass

    def go_in_house(self, группа_зданий):
        pass

    def fall(self):
        if pygame.sprite.spritecollideany(self, get_platform_group()) is None:
            self.rect.y += self.gravity

    def update(self, *args):
        if args:
            self.walk(args[0])



class Grater(pygame.sprite.Sprite):
    def __init__(self, image, pos, size, speed, *group):
        super().__init__(*group)
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect().move(
            size[0] * pos[0] + 15, size[1] * pos[1] + 5)

    def run(self):
        self.rect.x += self.speed

    def update(self, *args):
        self.run()

