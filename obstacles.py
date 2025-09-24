import pygame, random
from utils import get_image
from Obstacle import Obstacle
from terrain import TerrainManager

class obstacleManager:
  def __init__(self):
    self.obstacleSpritesheet = pygame.image.load(r"assets\obstacles\obstacles_spritesheet_v2.png").convert_alpha()
    self.obstacle_sprites = {
      "tree": get_image(self.obstacleSpritesheet, 0, 0, 20, 40),
      "rock": get_image(self.obstacleSpritesheet,20, 0, 20, 40),
      "spike": get_image(self.obstacleSpritesheet, 40, 0, 20, 40),
      "bush": get_image(self.obstacleSpritesheet, 0, 40, 20, 40),
      "trashcan": get_image(self.obstacleSpritesheet, 20, 40, 20, 40)
    }

    

    self.obstacles = pygame.sprite.Group()

    #spawn varaibles
    self.spawn_timer = 0 
    self.spawn_interval = 2000
  
  def generate_obstacle(self, game, dt, terrain):
    self.spawn_timer = self.spawn_timer + dt
    if self.spawn_timer >= self.spawn_interval:
        image = random.choice(list(self.obstacle_sprites.values()))
        
        # Align obstacle with ground level
        # ground_y = terrain.segment_starting_y  # <-- current surface top
        # x = game.WIDTH * 2

        # # Find the ground at that x, chatgpt i dont undestand this part
        # ground_blocks = [b for b in terrain.blocks if b.rect.x <= x <= b.rect.right]
        # if ground_blocks:
        #     top_block = min(ground_blocks, key=lambda b: b.rect.y)  # topmost (lowest y)
        #     ground_y = top_block.rect.y
        # else:
        #     ground_y = terrain.segment_starting_y  # fallback
           

        # Place obstacle so it sits on ground
        # y = ground_y - image.get_height()
        x = game.WIDTH * 2
        y = terrain.segment_starting_y - image.get_height()

        obstacle = Obstacle(image, x, y, game.world_speed)
        self.obstacles.add(obstacle)
        self.spawn_timer = 0

  def update(self, game, dt, terrain):
    self.generate_obstacle(game, dt, terrain)
    self.obstacles.update(game)

  def draw(self, screen):
    self.obstacles.draw(screen)