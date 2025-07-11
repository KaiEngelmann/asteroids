import pygame

class Button:
    def __init__(self, text, x, y, width, height, font, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.callback = callback
        self.color = (100, 100, 100)
        self.hover_color = (150, 150, 150)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)
        pygame.draw.rect(screen, self.hover_color if is_hovered else self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (
            self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
            self.rect.y + (self.rect.height - text_surface.get_height()) // 2
        ))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.callback()