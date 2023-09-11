import pygame

class ButtonWithTextImageSound:
    def __init__(self, screen, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = None
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.is_hovered = False
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_clicked = False

    def draw(self):
        if self.is_hovered and self.hover_image:
            self.screen.blit(self.hover_image, (self.x, self.y))
        else:
            self.screen.blit(self.image, (self.x, self.y))

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        self.screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        if (self.x < mouse_pos[0] < self.x + self.width) and (self.y < mouse_pos[1] < self.y + self.height):
            self.is_hovered = True
        else:
            self.is_hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            self.is_clicked = True
            if self.sound:
                self.sound.play()
        elif event.type == pygame.MOUSEBUTTONUP and self.is_clicked:
            self.is_clicked = False
            if self.is_hovered:
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'button_clicked': self}))

    def update(self):
        pass  # Дополнительная логика обновления, если необходимо

# Этот класс ButtonWithTextImageSound создает кнопку с текстом, изображением на фоне кнопки, поддерживает эффект "ховера", проигрывание звука при нажатии и генерацию события, когда кнопка нажата. Вы можете создать экземпляр этого класса, указав текст, пути к изображению, изображению для эффекта ховера и звуку. Затем можно использовать методы draw() для отображения кнопки, check_hover() для отслеживания положения курсора, handle_event() для обработки событий мыши и update() для дополнительной логики обновления, если это необходимо. Когда кнопка нажата, она генерирует событие pygame.USEREVENT, которое может быть обработано вашим кодом.
