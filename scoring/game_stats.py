import json


class GameStats:
    """游戏信息统计"""
    
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        with open('high_score.txt', 'r') as file_object:
            number = json.load(file_object)
        self.high_score = number

        
    def reset_stats(self):
        """游戏信息统计"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1