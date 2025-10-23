import pygame
import os 
from duck import Duck
from terrain import TerrainManager
from obstacles import obstacleManager

base_dir = os.path.dirname(__file__)
class Game:
  def __init__(self):
    pygame.init()
    self.WIDTH, self.HEIGHT = 800 , 600
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    pygame.display.set_caption("QuackQuest")
    self.clock = pygame.time.Clock()
    self.fps = 60
    self.running = True #Game loop starts
    self.base_world_speed = 5
    self.world_speed = 5
    self.spawn_pos = (100, 350)
    self.duck = Duck(self.spawn_pos[0], self.spawn_pos[1])
    self.terrain_manager = TerrainManager(self.WIDTH, self.HEIGHT)

     #score + lives
    self.score = 0
    self.lives = 3
    self.pixel_font = pygame.font.Font(os.path.join(base_dir, "assets", "game", "Grand9K Pixel.ttf"), 20)
    self.heart_image = pygame.image.load(os.path.join(base_dir, "assets", "game", "heart.png")).convert_alpha()

    #game states
    self.game_state = "menu"
    self.game_over = False

    #obstacles
    self.obstacleManager = obstacleManager()

  #Main game loop, handles all different components of game.
  def run(self):
    while self.running == True:
      dt = self.clock.tick(self.fps)
      self.handle_events()
      self.update(dt)
      self.draw()
    pygame.quit()

  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w and self.duck.jump_count < 1000000: #for testing
          self.duck.jump()
        if event.key == pygame.K_r and self.game_state == "game_over":
          self.reset_game()
        if event.key == pygame.K_RETURN and self.game_state == "menu":
          self.reset_game()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and self.game_state == "running" and self.duck.bouncing_back == False:
        self.duck.duck(self)
    if self.duck.on_ground and not keys[pygame.K_SPACE]:
        self.duck.run(self)

  def reset_game(self):
    self.duck = Duck(self.spawn_pos[0], self.spawn_pos[1])  # reset duck
    self.terrain_manager = TerrainManager(self.WIDTH, self.HEIGHT)  # reset terrain
    self.obstacleManager = obstacleManager()  # reset obstacles
    self.score = 0
    self.lives = 3
    self.world_speed = 5
    self.game_state = "running"

  def update(self, dt):
    self.duck.update(dt, self.terrain_manager.blocks, self)
    self.terrain_manager.update(self.world_speed)
    self.score_handler()
    self.obstacleManager.update(self, dt, self.terrain_manager)


  def draw(self):
    if self.game_state == "menu":
      self.draw_start_screen()
      pygame.display.flip()
      return
    self.screen.fill((135, 206, 235)) #Sky blue background
    self.terrain_manager.draw(self.screen)
    self.obstacleManager.draw(self.screen)
    self.duck.draw(self.screen)
    self.draw_score()
    self.draw_lifes()
    self.retry_screen()
    pygame.display.flip()   

  def score_handler(self):
    if self.world_speed > 0:
      self.score = self.score + 1

  def draw_score(self):
    score_text = self.pixel_font.render(f"Score: {self.score}", True, (0, 0, 0))
    self.score_rect = score_text.get_rect(topright=(self.WIDTH - 10, 10))  # right-align + padding
    self.screen.blit(score_text, self.score_rect)

  def draw_lifes(self):
     # Draw lives (hearts to the left of score)
    heart_x = self.score_rect.left - 10  # start 10px left of score
    for i in range(self.lives):
      self.screen.blit(self.heart_image, (heart_x - ((i+1) * (self.heart_image.get_width() + 5)), 10))


  def check_death(self):
    if self.lives <= 0:
      return True
    else: 
      return False
    
  def retry_screen(self):
    if self.check_death() == True:
      self.game_state = "game_over"
      #no need to stop world, already handled in duck.py
      
      # Semi-transparent black overlay
      overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
      overlay.set_alpha(180)  # 0 = fully transparent, 255 = solid
      overlay.fill((0, 0, 0))
      self.screen.blit(overlay, (0, 0))

      # Draw retry box
      box_width, box_height = 300, 150
       #to get center
      box_x = (self.WIDTH - box_width) // 2 
      box_y = (self.HEIGHT - box_height) // 2
      pygame.draw.rect(self.screen, (255, 255, 255), (box_x, box_y, box_width, box_height), border_radius=10)

      # Draw "Game Over" text
      title = self.pixel_font.render("Game Over", True, (0, 0, 0))
      title_rect = title.get_rect(center=(self.WIDTH // 2, box_y + 40))
      self.screen.blit(title, title_rect)

      # Draw press R to retry text
      prompt = self.pixel_font.render("Press R to retry", True, (0, 0, 0))
      prompt_rect = prompt.get_rect(center=(self.WIDTH // 2, box_y + 90))
      self.screen.blit(prompt, prompt_rect)

  def draw_start_screen(self):
    self.screen.fill((135, 206, 235))  # background sky-blue

    title = self.pixel_font.render("QuackQuest", True, (0, 0, 0))
    title_rect = title.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 3))
    self.screen.blit(title, title_rect)

    prompt = self.pixel_font.render("Press ENTER to Start", True, (0, 0, 0))
    prompt_rect = prompt.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
    self.screen.blit(prompt, prompt_rect)

    #draw duck sprite as decoration
    duck_preview = pygame.transform.scale(self.duck.image, (64, 64))
    self.screen.blit(duck_preview, (self.WIDTH // 2 - 32, self.HEIGHT // 2 + 60))
    


