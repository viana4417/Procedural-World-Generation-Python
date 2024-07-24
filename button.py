import pygame

class Button:
    def __init__(self, screen, text, x, y, w, h, color, on_click):
        self.screen = screen
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.on_click = on_click
        self.font = pygame.font.SysFont(None, 24)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        self.screen.blit(text_surf, text_rect)
