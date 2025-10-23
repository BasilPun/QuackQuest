import pygame
import os
from utils import get_image
from terrain import TerrainManager
from particles import Explosion

base_dir = os.path.dirname(__file__)

class Duck:
  def __init__(self, x, y):
    self.spriteSheet = pygame.image.load(os.path.join(base_dir, "assets", "duck", "duck_spritesheet.png")).convert_alpha()
    self.states = ["running", "jumping", "ducking"]
    self.frames = [
      #collumn 1
      get_image(self.spriteSheet, 0, 0, 59, 50), #jump
      get_image(self.spriteSheet, 59, 0, 59, 50), #run1
      #collumn 2
      get_image(self.spriteSheet, 0, 50, 59, 50), #run2
      get_image(self.spriteSheet, 59, 50, 59, 50), #duck1
      #collumn 3
      get_image(self.spriteSheet, 0, 100, 59, 50), #duck2
    ]

    #starting stae
    self.state = "running"
    self.current_frame = 1
    self.animation_index = 0
    self.animation_timer = 0
    self.reset_time = 100
    self.on_ground = True


    self.image = self.frames[self.current_frame]
    self.rect = self.image.get_rect(topleft=(x, y))


    #gravity and jump variables
    self.gravity = 0.5
    self.jump_strength = -10 #negative for upward movement
    self.velocity_y = 0
    self.ground_y = y

    #bounce back variables
    self.bouncing_back = False
    self.bounce_timer = 0
    self.bounce_reset_time = 1000
    self.bounce_amount = 8
    self.velocity_x = 0


  def update(self, dt, blocks, game):
    self.handleGravity(blocks)
    self.handleWallCollision(blocks, game)
    self.stay_in_bounds()
    self.animate(dt)

  def handleGravity(self, blocks):
    #make duck fall down
    if not self.on_ground:
      self.velocity_y = self.velocity_y + self.gravity
      self.rect.y = self.rect.y + self.velocity_y

    self.on_ground = False;
    #make duck land on ground
    for block in blocks:
      if self.rect.colliderect(block.rect) and self.velocity_y > 0:
        self.rect.bottom = block.rect.top
        self.velocity_y = 0
        self.on_ground = True
        self.jump_count = 0
      
  def handleWallCollision(self, blocks, game):
    for block in blocks:
      # Check right-side collision
      if self.rect.colliderect(block.rect) and not self.bouncing_back:
          global stop_point
          if self.rect.right >= block.rect.left:
            #stop world movement first
            game.world_speed = 0
            stop_point = block.rect.left
            #snap duck to left of block
            self.rect.x = game.spawn_pos[0]
            self.bounce_back()
            game.lives = game.lives - 1
            break

    if self.bouncing_back == True:
      now  = pygame.time.get_ticks()
      self.state = "running"
      self.rect.x = self.rect.x + self.velocity_x
      self.velocity_x = self.velocity_x * 0.9 #slow down over time
      if now - self.bounce_timer > self.bounce_reset_time:
        self.bouncing_back = False
        self.bounce_timer = 0

    # 3 because it bugs out at 0 with ducking logic constantly accleerating
    if game.world_speed <= 3 and self.bouncing_back == False and game.lives>= 1:
      self.rect.x = self.rect.x + 5
      if self.rect.right > stop_point and self.rect.x >= game.spawn_pos[0]: 
        self.rect.x = game.spawn_pos[0]
        game.world_speed = 5
    else:
      pass

                  

  def bounce_back(self):
    self.velocity_x = self.velocity_x - self.bounce_amount
    self.bouncing_back = True
    self.bounce_timer = pygame.time.get_ticks()

  def animate(self, dt):
    self.possible_frames = []
    self.animation_timer = self.animation_timer + dt
    if self.animation_timer >= self.reset_time: #change frame every 100 ms
      self.animation_timer = 0

      if self.state == "jumping":
        self.possible_frames = [0]
      elif self.state == "ducking":
        self.possible_frames = [3, 4]
      elif self.state == "running":
        self.possible_frames = [1, 2]
      else:
        raise ValueError(f"Unknown state: {self.state}")
      
      #this way, if 1 frame, it stays on that frame, if multiple frames, it cycles through them
      self.animation_index = (self.animation_index + 1) % len(self.possible_frames)
      self.current_frame = self.possible_frames[self.animation_index]
      self.image = self.frames[self.current_frame]

  def stay_in_bounds(self):
    # if self.rect.right != game.spawn_pos[0] and not self.bouncing_back:
    #   self.rect.right = game.spawn_pos[0]
    if self.rect.right < 0:
      self.rect.right = 0

  def jump(self):
    self.state = "jumping"
    self.velocity_y = self.velocity_y + self.jump_strength
    self.on_ground = False
    self.jump_count = self.jump_count + 1


  def duck(self, game):
    if self.state == "jumping":
      self.state == "ducking" #allow ducking in air
    self.state = "ducking"
    game.world_speed = min(game.world_speed + 0.05, 10)  # max speed 10


  def run(self, game):
    self.state = "running"
    if game.world_speed > game.base_world_speed:
      game.world_speed = game.base_world_speed

  def draw(self, screen):
    screen.blit(self.image, self.rect)
  

