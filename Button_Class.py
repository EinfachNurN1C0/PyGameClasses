# --- Imports all necessary modules: ---
import pygame

# --- Defines the button class requirements and syntax: ---
# --- ButtonName = Button_Class.Button(Button Width, Button Height, Link to an Button Image, Button Scale)
# --- z.B. ---
# --- BUTTON_IMAGE = pygame.image.load(os.path.join('Assets', 'Buttons', 'Button_Image.png'))
# --- BUTTON = Button_Class.Button(250, 250, BUTTON_IMAGE, 1)
# --- BUTTON.draw(Definition of the window)

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    # --- This function checks if a button has been clicked: ---
    # --- You can use the function as follows: ---
    # --- if BUTTON.draw(Definition of the window): <-- If BUTTON is pressed
    # ---   print("Hello World")
    
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
                
        surface.blit(self.image, (self.rect.x, self.rect.y))
            
        
        return action