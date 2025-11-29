import pygame
import sys

from button import Button

pygame.init()

WIDTH, HEIGHT = 1000, 720
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Игра - викторина "Один день из жизни школьника"')
clock = pygame.time.Clock()

button1 = Button(WIDTH/2-(252/2), 100, 252, 74, "", "png-klev-club-6oo7-p-knopka-zelenaya-png-21.png", "621fa35b6ffe2821124de94d0e7081a1.jpg", "850bae87-e7c2-44bd-b763-ff45928a13f3.mp3")

def main_menu():
    running = True
    while running:

        screen.fill((255, 255, 255))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("BUTTON TEST", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(300, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            button1.handle_event(event)

        button1.check_hover(pygame.mouse.get_pos())
        button1.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
main_menu()
