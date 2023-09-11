import pygame
import sys

# Инициализация pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игровое меню")

# Создание кнопки
play_button = ImageButton(300, 200, 200, 100, "Играть", "path_to_image.png", "path_to_hover_image.png", "click_sound.wav")

def main_menu():
    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == play_button:
                print("Кнопка 'Играть' была нажата!")
                # Здесь вы можете вызвать функцию или событие, которое начнет игру

            play_button.handle_event(event)

        play_button.check_hover(pygame.mouse.get_pos())
        play_button.draw(screen)
        pygame.display.flip()

main_menu()
