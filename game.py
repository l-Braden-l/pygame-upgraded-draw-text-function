# -- Pygame Game Template -- #
import pygame
import sys
import config # Import the config module 

def init_game (): 
    pygame.init()
    pygame.font.init() #initialize fonts here
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True

# --- Functions ---#

def draw_text(screen, text, font_size, font_name, color, position, anti_aliased = True, bold = False, italic=False):
   if font_name:
      font = pygame.font.Font(font_name, font_size)
   else: 
      font = pygame.font.Font(None, font_size)

   font.set_bold(bold)
   font.set_italic(italic)
   
   text_surface = font.render(text, True, color)
   screen.blit(text_surface, position)






def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here

   # --- Define Properties ---#
   font_name1 = 'c:\Fonts\RobotoMono-VariableFont_wght.ttf'
   font_color1 = config.RED
   font_color2 = config.ORANGE
   font_color3 = config.SKY_BLUE
   font_size_normal = 36
   font_size_bold_ital = 30
   font_size_custom = 48 

   # -- Use True Type Font --#
   font_name_ttf = 'c:\Fonts\BebasNeue-Regular.ttf'

   #-- Define X,Y Corrdinate(top left) (stamp) --#
   text_pos1 = [50, 50]
   text_pos2 = [150, 150]
   text_pos3 = [350, 350]

   running = True
   while running:
      running = handle_events()
      screen.fill(config.WHITE) # Use color from config

      #-- Text One --#
      draw_text(screen, "Hello, Pygame!", font_size_normal, font_name1, font_color1, text_pos1, italic=True)

      #-- Text Two --#
      draw_text(screen, "This text is bolded and italic!", font_size_bold_ital, font_name_ttf, font_color2, text_pos2, bold=True, italic=True)

      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()