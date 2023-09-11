import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Обработка события нажатия кнопки")

# Создание кнопки
class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 255)
        self.is_clicked = False

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_clicked = True

    def reset(self):
        self.is_clicked = False

button = Button(300, 200, 200, 100)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        button.handle_event(event)

    screen.fill((255, 255, 255))
    button.draw()

    if button.is_clicked:
        print("Кнопка нажата!")
        # Добавьте здесь код, который должен выполняться при нажатии кнопки
        button.reset()

    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
