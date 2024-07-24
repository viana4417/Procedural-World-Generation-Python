import pygame
from world import World
from hud import HUD
from settings import WIDTH, HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Procedural World Generation")

    clock = pygame.time.Clock()
    running = True

    world = World(screen)
    hud = HUD(screen, world)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            hud.handle_event(event)

        if hud.regenerate_world:
            world = World(screen, seed=hud.new_seed_value)
            hud.regenerate_world = False

        world.update()
        screen.fill((255, 255, 255))
        world.draw()
        hud.draw(clock)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
