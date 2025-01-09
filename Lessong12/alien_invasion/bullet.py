import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
  """Класс для управления пулями, выпущенными кораблем."""
  def __init__(self, ai_game):
    """Создает объект пули в текущем положении корабля."""
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.color = self.settings.bullet_color

    # Создание пули в (0,0) и назначение правильной позиции.
    self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
      self.settings.bullet_height)
    self.rect.midtop = ai_game.ship.rect.midtop

    # Позиция пули хранится в вещественном формате.
    self.y = float(self.rect.y)

  def update(self): 
    """Перемещает пулю вверх по экрану."""
    # Обновляет позицию пули.
    self.y -= self.settings.bullet_speed
    # Обновляет позицию пули.
    self.rect.y = self.y

  def draw_bullet(self):
    """Отрисовывает пулю в текущем положении."""
    pygame.draw.rect(self.screen, self.color, self.rect)