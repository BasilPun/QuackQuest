import pygame, random
from utils import get_image
from Obstacle import Obstacle
from terrain import TerrainManager
import os

base_dir = os.path.dirname(__file__)

class obstacleManager:
  def __init__(self):
    self.obstacleSpritesheet = pygame.image.load(os.path.join(base_dir, "assets", "obstacles", "obstacles_spritesheet_v2.png")).convert_alpha()
    self.obstacle_sprites = {
      "tree": get_image(self.obstacleSpritesheet, 0, 0, 20, 40),
      "rock": get_image(self.obstacleSpritesheet,20, 0, 20, 40),
      "spike": get_image(self.obstacleSpritesheet, 40, 0, 20, 40),
      "bush": get_image(self.obstacleSpritesheet, 0, 40, 20, 40),
      "trashcan": get_image(self.obstacleSpritesheet, 20, 40, 20, 40)
    }

    for i in self.obstacle_sprites:
      self.obstacle_sprites[i] = pygame.transform.scale(self.obstacle_sprites[i], (40, 80))

    self.obstacles = pygame.sprite.Group()

    #spawn varaibles
    self.spawn_timer = 0 
    self.spawn_interval = 2000
  
  def generate_obstacle(self, game, dt, terrain):
    self.spawn_timer = self.spawn_timer + dt
    if self.spawn_timer >= self.spawn_interval:
        image = random.choice(list(self.obstacle_sprites.values()))
        
        # Proposed X position
        x = game.WIDTH * 2
        obstacle_rect = image.get_rect(topleft=(x, 0))  # y=0 for now

        # Collect all ground blocks under the obstacle's span
        obstacle_mid_x = obstacle_rect.centerx
        span_blocks = [b for b in terrain.blocks if b.rect.left <= obstacle_mid_x <= b.rect.right]


        if span_blocks:
            # Pick the topmost ground (lowest y)
            ground_y = min(b.rect.y for b in span_blocks)
            y = ground_y - obstacle_rect.height
            obstacle_rect.y = y
        else:
            # fallback if no ground under obstacle
            ground_y = terrain.segment_starting_y
            y = ground_y - obstacle_rect.height
            obstacle_rect.y = y

        # Make a 1-pixel wide rect along the right edge
        right_edge_rect = pygame.Rect(obstacle_rect.right, obstacle_rect.top, 1, obstacle_rect.height)

        # Same for left edge
        left_edge_rect = pygame.Rect(obstacle_rect.left - 20, obstacle_rect.top, 20, obstacle_rect.height)

        # Check right edge collision
        if any(right_edge_rect.colliderect(b.rect) for b in terrain.blocks):
            # Push left until no collision
            while any(obstacle_rect.colliderect(b.rect) for b in terrain.blocks):
                print("right collision")
                obstacle_rect.x -= 10
        # Check left edge collision
        if any(left_edge_rect.colliderect(b.rect) for b in terrain.blocks):
            # Push right until no collision
            while any(obstacle_rect.colliderect(b.rect) for b in terrain.blocks):
                print("left collision")
                obstacle_rect.x += 20

        
        # Finally spawn obstacle
        obstacle = Obstacle(image, obstacle_rect.x, obstacle_rect.y, game.world_speed)
        self.obstacles.add(obstacle)

        self.spawn_timer = 0

  def update(self, game, dt, terrain):
    self.generate_obstacle(game, dt, terrain)
    self.obstacles.update(game)

  def draw(self, screen):
    self.obstacles.draw(screen)