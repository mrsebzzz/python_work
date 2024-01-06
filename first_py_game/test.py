import pygame
import os

WIDTH, HEIGHT = 1200, 900
FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Testing New Game")

def draw_window():
    WINDOW.blit(0,0)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
    
if __name__ == "__main__":
    main()