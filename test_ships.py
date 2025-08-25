#!/usr/bin/env python3
"""
测试飞船数量显示的简单脚本
"""

import sys
import os
sys.path.append('alien_invasion')
os.chdir('alien_invasion')

from game_stats import GameStats
from settings import Settings

class MockAIGame:
    def __init__(self):
        self.settings = Settings()

# 测试游戏统计
mock_game = MockAIGame()
stats = GameStats(mock_game)

print(f"初始飞船数量: {stats.ships_left}")
print(f"船只限制: {stats.settings.ship_limit}")

# 模拟飞船被撞击
if stats.ships_left > 0:
    print(f"飞船被撞击前: {stats.ships_left}")
    stats.ships_left -= 1
    print(f"飞船被撞击后: {stats.ships_left}")

# 再次撞击
if stats.ships_left > 0:
    print(f"飞船再次被撞击前: {stats.ships_left}")
    stats.ships_left -= 1
    print(f"飞船再次被撞击后: {stats.ships_left}")
