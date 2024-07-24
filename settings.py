import random

WIDTH, HEIGHT = 1280, 720
SCALE = 5.0
OCTAVES = 6
PERSISTENCE = 0.5
LACUNARITY = 2
BORDER_WIDTH = WIDTH // 8
BORDER_HEIGHT = HEIGHT // 8
RANDOM_SEED = random.uniform(0, 1000000)

COLORS = {
    "water": (0, 0, 255),
    "grass": (0, 255, 0),
    "snow": (255, 255, 255)
}
