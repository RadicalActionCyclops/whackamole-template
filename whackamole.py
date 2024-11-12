import pygame, random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        WIDTH = 640
        HEIGHT = 512
        SQUARE = 32
        mole_pos = (0, 0)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (mole_pos[0], mole_pos[1]) <= (event.pos[0], event.pos[1]) <= (mole_pos[0]+32, mole_pos[1]+32):
                        mole_pos = random.randrange(0, WIDTH, SQUARE), random.randrange(0, HEIGHT, SQUARE)
            screen.fill("light green")
            color = "black"
            # Draw grid
            for x1 in range(0, WIDTH, SQUARE):
                for y1 in range(0, HEIGHT, SQUARE):
                    pygame.draw.line(screen, color, (0, y1), (WIDTH, y1))
                pygame.draw.line(screen, color, (x1, 0), (x1, HEIGHT))
            # Display mole
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
