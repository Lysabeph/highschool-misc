#Not this crap again...

import pygame

#Initiates pygame.
pygame.init()

#Default values.
Width = 640
Height = 480
Border = 4
WindowGen = True

def Menu():
    global Border, Height, Width
        
    if WindowGen != True:
        Width = event.dict['size'][0]
        Height = event.dict['size'][1]

    #Creates the Menu window.
    Menu = pygame.display.set_mode((Width,Height), HWSURFACE|DOUBLEBUF|RESIZABLE)
    pygame.display.set_caption("Battleships")

    #Sets background colour.
    x, y = Menu.get_size()
    pygame.draw.rect(Menu, (156,156,156), (0,0,x,y))

    pygame.draw.rect(Menu, (84,84,84), (Width/4, 0, Width*3/4, Height), 0)
    pygame.draw.rect(Menu, (0,0,0), (Width/4, 0, Width*3/4, Height), int(Border*Width/x))
    pygame.display.flip()

Menu()
WindowGen = False

while True:

    pygame.event.pump()
    event = pygame.event.wait()

    if event.type == QUIT: pygame.display.quit()
    
    elif event.type == VIDEORESIZE:
        Menu()
