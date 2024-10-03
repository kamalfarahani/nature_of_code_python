import pygame


def limit(
    vector: pygame.Vector2,
    limit: float,
) -> pygame.Vector2:
    if vector.magnitude() > limit:
        return vector.normalize() * limit
    return vector
