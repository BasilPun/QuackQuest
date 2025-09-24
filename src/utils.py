import pygame 

 # Extract images from sprite sheet
def get_image(sheet, x, y, width, height):
  image = pygame.Surface((width, height), pygame.SRCALPHA)
  image.blit(sheet, (0, 0), (x, y, width, height))
  return image