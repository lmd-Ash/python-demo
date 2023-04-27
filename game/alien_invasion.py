import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    # aliens = Alien(ai_settings, screen  )
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        gf.update_screen(ai_settings, stats, screen, ship, bullets, aliens, play_button, sb)


run_game()
