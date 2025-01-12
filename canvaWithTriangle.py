import pygame
import sys

def main():
    pygame.init()


    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Canvas Example")
    screen.fill((255, 255, 255))  # Fill the canvas with white color


    pygame.draw.line(screen, (255, 0, 0), (50, 50), (250, 50), 3)  # Red line with width 3 and length 200 pixels


    pygame.draw.polygon(screen, (0, 0, 0), [(150, 100), (200, 50), (250, 100)], 1)
    pygame.draw.polygon(screen, (0, 0, 0), [(200, 150), (250, 100), (300, 150)], 1)
    pygame.draw.polygon(screen, (0, 0, 0), [(250, 200), (300, 150), (350, 200)], 1)


    pygame.draw.circle(screen, (128, 0, 128), (250, 100), 5)


    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
