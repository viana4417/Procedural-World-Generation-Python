import pygame
import noise
from settings import WIDTH, HEIGHT, SCALE, OCTAVES, PERSISTENCE, LACUNARITY, COLORS, BORDER_WIDTH, BORDER_HEIGHT, RANDOM_SEED

class World:
    def __init__(self, screen, seed=RANDOM_SEED):
        self.screen = screen
        self.seed = seed
        self.world, self.chunks, self.chunk_size = self.generate_world()
        self.current_chunk = 0
        self.generation_complete = False

    def generate_world(self):
        world = pygame.Surface((WIDTH, HEIGHT))
        chunk_size = 120
        chunks = [(x, y) for y in range(0, HEIGHT, chunk_size) for x in range(0, WIDTH, chunk_size)]
        return world, chunks, chunk_size

    def generate_chunk(self, start_x, start_y, width, height):
        for y in range(start_y, start_y + height):
            for x in range(start_x, start_x + width):
                if x >= WIDTH or y >= HEIGHT:
                    continue
                nx = x / WIDTH - 0.5
                ny = y / HEIGHT - 0.5
                distance_from_center = ((nx)**2 + (ny)**2)**0.5
                elevation = noise.snoise2(nx * SCALE, ny * SCALE, octaves=OCTAVES, persistence=PERSISTENCE, lacunarity=LACUNARITY, repeatx=1024, repeaty=1024, base=self.seed)
                
                edge_distance_x = min(x / BORDER_WIDTH, (WIDTH - x) / BORDER_WIDTH)
                edge_distance_y = min(y / BORDER_HEIGHT, (HEIGHT - y) / BORDER_HEIGHT)
                edge_factor = min(1.0, edge_distance_x * 5, edge_distance_y)

                if edge_factor < 1:
                    elevation -= (1 - edge_factor)
                
                gradient = abs(nx) * 0.7
                elevation -= gradient * 1.5
                
                if distance_from_center > 0.5:
                    elevation -= (distance_from_center - 0.5)
                
                terrain_type = "water" if elevation < 0 else "grass"
                color = COLORS[terrain_type]
                self.world.set_at((x, y), color)

    def add_snow(self):
        for y in range(20):
            for x in range(WIDTH):
                self.world.set_at((x, y), COLORS["snow"])
        
        for y in range(HEIGHT - 20, HEIGHT):
            for x in range(WIDTH):
                self.world.set_at((x, y), COLORS["snow"])

        for y in range(20, 60):
            for x in range(WIDTH):
                nx = x / WIDTH
                ny = y / HEIGHT
                elevation = noise.snoise2(nx * SCALE, ny * SCALE, octaves=OCTAVES, persistence=PERSISTENCE, lacunarity=LACUNARITY, repeatx=1024, repeaty=1024, base=self.seed)
                if elevation > -0.2 + (y - 20) / 40:
                    self.world.set_at((x, y), COLORS["snow"])

        for y in range(HEIGHT - 60, HEIGHT - 20):
            for x in range(WIDTH):
                nx = x / WIDTH
                ny = y / HEIGHT
                elevation = noise.snoise2(nx * SCALE, ny * SCALE, octaves=OCTAVES, persistence=PERSISTENCE, lacunarity=LACUNARITY, repeatx=1024, repeaty=1024, base=self.seed)
                if elevation > -0.2 + (HEIGHT - 20 - y) / 40:
                    self.world.set_at((x, y), COLORS["snow"])

    def update(self):
        if self.current_chunk < len(self.chunks):
            chunk_x, chunk_y = self.chunks[self.current_chunk]
            self.generate_chunk(chunk_x, chunk_y, self.chunk_size, self.chunk_size)
            self.current_chunk += 1

        if self.current_chunk == len(self.chunks) and not self.generation_complete:
            self.add_snow()
            self.generation_complete = True

    def draw(self):
        self.screen.blit(self.world, (0, 0))
