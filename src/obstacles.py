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
        
        # Step 1: Collect all blocks at this X position
        x = game.WIDTH * 2
        ground_blocks = []

        # Step 1: find all ground blocks under this X
        for block in terrain.blocks:
            if block.rect.x <= x <= block.rect.right:
                ground_blocks.append(block)

        # Step 2: find the topmost block (smallest y)
        if ground_blocks:
            top_block = ground_blocks[0]
            for block in ground_blocks:
                if block.rect.y < top_block.rect.y:
                    top_block = block

            # Step 3: adjust X so obstacle doesn’t overlap edges
            right_edge = top_block.rect.right
            left_edge = top_block.rect.left
            if x + image.get_width() > right_edge:
                x = right_edge - image.get_width()
                print("adjsuted right")
            elif x < left_edge:
                x = left_edge
                print("adjusted left")

            ground_y = top_block.rect.y
        else:
            # fallback if no block found
            ground_y = terrain.segment_starting_y

        # Step 4: place obstacle on top of ground
        y = ground_y - image.get_height()

        obstacle = Obstacle(image, x, y, game.world_speed)
        self.obstacles.add(obstacle)
        self.spawn_timer = 0

  def update(self, game, dt, terrain):
    self.generate_obstacle(game, dt, terrain)
    self.obstacles.update(game)

  def draw(self, screen):
    self.obstacles.draw(screen)