import pygame
import random
from TerrainBlock import TerrainBlock
from utils import get_image

class TerrainManager:
  def __init__(self, screen_width, screen_height):
    self.spriteSheet = pygame.image.load(r"assets\terrain\terrain_spritesheet.png").convert_alpha()
    self.block_sprites = {
      "grass": get_image(self.spriteSheet, 0, 0, 20, 20),
      "dirt": get_image(self.spriteSheet, 0, 20, 20, 20)
    }

    self.blocks = pygame.sprite.Group()

    self.game_starting_y = 400
    self.new_y = self.game_starting_y
    self.block_height = 20
    self.block_width = 20
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.world_offset = 0

    self.starting_terrain()

    self.segment_starting_x = self.block_width * 20
    self.segment_starting_y = self.game_starting_y

    while (self.segment_starting_x < self.screen_width * 2): #pre-load at least 2 screens
       self.segment_generator(self.segment_starting_x, self.segment_starting_y)

  def starting_terrain(self):
    for x in range(0, self.block_width * 20, self.block_width):
      for y in range(self.game_starting_y, self.screen_height, self.block_height):
        if y == self.game_starting_y:
          block = TerrainBlock(x, y, self.block_sprites["grass"])
        else:
          block = TerrainBlock(x, y, self.block_sprites["dirt"])
        self.blocks.add(block)

  def segment_generator(self, segment_starting_x, segment_starting_y):
    segment_width = random.randint(6, 15) * self.block_width

    step = random.randint(-3, 3) * self.block_height
    new_y = segment_starting_y + step

    #control y-height
    lowest_y = self.block_height * (30-3) #3 from the bottom
    highest_y = self.block_height * 5 # 10 from the top
    if new_y >= lowest_y:
      new_y = lowest_y
    elif new_y <= highest_y:
      new_y = highest_y


    for x in range(segment_starting_x, segment_starting_x + segment_width, self.block_width):
      for y in range (new_y, self.screen_height, self.block_height):
        if y == new_y:
          block = TerrainBlock(x, y, self.block_sprites["grass"])
          
        else:
          block = TerrainBlock(x, y, self.block_sprites["dirt"])
        self.blocks.add(block)

    self.segment_starting_x = max(block.rect.right for block in self.blocks) #the most right block generated
    self.segment_starting_y = new_y

  def update(self, world_speed):
    for block in self.blocks:
      block.rect.x = block.rect.x - world_speed
    self.world_offset = self.world_offset + world_speed
    if self.segment_starting_x - self.world_offset < self.screen_width * 2: #load up 2 screens worth
      self.segment_generator(max(block.rect.right for block in self.blocks), self.segment_starting_y)

    # Remove blocks that are far off screen
    for block in list(self.blocks):  # copy to avoid modifying while iterating
        if block.rect.right < -self.block_width * (self.screen_width // self.block_width):
            self.blocks.remove(block)
    



  def draw(self, screen):
    self.blocks.draw(screen)

