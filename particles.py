import pygame, random

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((4, 4))  # pixel "chunk"
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [random.randint(-5, 5), random.randint(-8, -2)]
        self.gravity = 0.3
        self.lifetime = 60  # frames until it disappears

    def update(self):
        self.velocity[1] += self.gravity  # gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()

class Explosion:
    def __init__(self, x, y):
        self.particles = pygame.sprite.Group()
        colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0)]  # red, orange, yellow
        for _ in range(30):
            color = random.choice(colors)
            self.particles.add(Particle(x, y, color))

    def update(self, screen):
        self.particles.update()
        self.particles.draw(screen)
