import random
import pygame
import numpy as np

from dataclasses import dataclass


@dataclass
class ColorCircle:
    rect: pygame.Rect
    color: tuple[int, int, int]


@dataclass
class PaintSplat:
    x_center: int
    y_center: int
    color: tuple[int, int, int]
    x_radius: int
    y_radius: int
    number_of_circles: int = 10000
    circles_radius: int = 5

    def generate(self) -> list[ColorCircle]:
        color_circles = []
        for _ in range(self.number_of_circles):
            x_center = np.random.normal(self.x_center, self.x_radius)
            y_center = np.random.normal(self.y_center, self.y_radius)
            color_circles.append(
                ColorCircle(
                    rect=pygame.Rect(
                        x_center,
                        y_center,
                        self.circles_radius,
                        self.circles_radius,
                    ),
                    color=self.color,
                ),
            )

        return color_circles


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    colors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255),
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        splat_x_center = np.random.randint(0, display_width)
        splat_y_center = np.random.randint(0, display_height)
        splat_x_radius = np.random.randint(10, 100)
        splat_y_radius = np.random.randint(10, 100)
        splat_color = random.choice(colors)
        splat = PaintSplat(
            x_center=splat_x_center,
            y_center=splat_y_center,
            color=splat_color,
            x_radius=splat_x_radius,
            y_radius=splat_y_radius,
        )

        color_circles = splat.generate()

        for color_circle in color_circles:
            pygame.draw.circle(
                surface=screen,
                color=color_circle.color,
                center=(color_circle.rect.centerx, color_circle.rect.centery),
                radius=color_circle.rect.width // 2,
            )

        pygame.display.update()
        clock.tick(0.5)


if __name__ == "__main__":
    main()
