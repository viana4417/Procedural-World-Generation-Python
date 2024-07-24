import pygame
import random
from button import Button
from settings import WIDTH, SCALE, OCTAVES, PERSISTENCE, LACUNARITY, RANDOM_SEED

class HUD:
    def __init__(self, screen, world):
        self.screen = screen
        self.world = world
        self.font = pygame.font.SysFont(None, 24)
        self.show_hud = True
        self.buttons = self.create_buttons()
        self.regenerate_world = False
        self.new_seed_value = RANDOM_SEED

    def create_buttons(self):
        buttons = []
        buttons.append(Button(self.screen, "New seed", WIDTH - 160, 10, 150, 30, (255, 255, 0), self.new_seed))
        return buttons

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            self.show_hud = not self.show_hud
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    button.on_click()

    def draw(self, clock):
        if self.show_hud:
            hud_background = pygame.Surface((250, 90))
            hud_background.set_alpha(100)
            hud_background.fill((0, 0, 0))
            self.screen.blit(hud_background, (0, 90))

            for button in self.buttons:
                button.draw()

            self.draw_text(f"FPS: {int(clock.get_fps())}", 10, 100, (200, 200, 0))
            self.draw_text(f"Seed: {self.new_seed_value}", 10, 130, (200, 200, 0))
            self.draw_text("Press T to toggle HUD", 10, 160, (200, 200, 0))

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        text_surf = self.font.render(text, True, color)
        self.screen.blit(text_surf, (x, y))

    def new_seed(self):
        self.new_seed_value = random.uniform(0, 1000000)
        self.regenerate_world = True
