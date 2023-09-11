import pygame

class ButtonWithTextAndImage:
    def __init__(self, screen, x, y, width, height, text, image_path, hover_image_path=None, text_color=(255, 255, 255)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = None
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.is_hovered = False

    def draw(self):
        if self.is_hovered and self.hover_image:
            self.screen.blit(self.hover_image, (self.x, self.y))
        else:
            self.screen.blit(self.image, (self.x, self.y))

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        self.screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        if (self.x < mouse_pos[0] < self.x + self.width) and (self.y < mouse_pos[1] < self.y + self.height):
            self.is_hovered = True
        else:
            self.is_hovered = False

    def is_clicked(self, mouse_pos):
        if self.is_hovered:
            return True
        return False
