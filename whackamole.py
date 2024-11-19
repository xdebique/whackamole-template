import pygame
import random

def main():
    try:
        pygame.init()
        
        
        screen_width, screen_height = 640, 512
        grid_size = 32
        cols = screen_width // grid_size
        rows = screen_height // grid_size

        
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()
        mole_image = pygame.image.load("mole.png")

        # Mole's initial position (top-left corner)
        mole_x, mole_y = 0, 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mole was clicked
                    mouse_x, mouse_y = event.pos
                    mole_rect = pygame.Rect(mole_x, mole_y, grid_size, grid_size)
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        # Move the mole to a new random position
                        mole_x = random.randrange(0, cols) * grid_size
                        mole_y = random.randrange(0, rows) * grid_size

            # i tried to say light green but it wasnt working so i just gave up pretty much 
            screen.fill((144, 238, 144))

            # Draw the grid
            for x in range(0, screen_width, grid_size):
                pygame.draw.line(screen, (0, 0, 139), (x, 0), (x, screen_height))  # Vert line
            for y in range(0, screen_height, grid_size):
                pygame.draw.line(screen, (0, 0, 139), (0, y), (screen_width, y))  # Horiz line 

            # Draw the mole
            screen.blit(mole_image, (mole_x, mole_y))

            # Update 
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()