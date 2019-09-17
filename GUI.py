import os, pygame, random, sys, time, tkinter
from pygame.locals import *
from gi.repository import Gtk

def Login():
    
    window = tkinter.Tk()

    def LoginCheck():
        
        if (usrname_ent.get() == "123") and (passwd_ent.get() == "asd"):
            info_lbl.configure(text = "Correct login details. Logging in...")
            window.update_idletasks()
            time.sleep(1.5)
            window.destroy()
            MainGame()

        else:
            info_lbl.configure(text = "Incorrect details.")

    usrname_lbl = tkinter.Label(window, text="Username:", fg="#FFFFFF", bg="#000000")
    usrname_ent = tkinter.Entry(window)
    passwd_lbl = tkinter.Label(window, text="Password:", fg="#FFFFFF", bg="#000000")
    passwd_ent = tkinter.Entry(window, show="*")
    login_btn = tkinter.Button(window, text="Login", command=LoginCheck)
    info_lbl = tkinter.Label(window, text="Please enter your details!")

    usrname_lbl.pack()
    usrname_ent.pack()
    passwd_lbl.pack()
    passwd_ent.pack()
    login_btn.pack()
    info_lbl.pack()

    window.title(">.<")
    window.geometry("512x512")

    window.mainloop()

def MainGame():

    #Tiles.
    DIRT     = 0
    GRASS    = 1
    STONE    = 2
    WATER    = 3
    LAVA     = 4
    COAL     = 5
    OBSIDIAN = 6
    IRON     = 7
    GOLD     = 8
    DIAMOND  = 9
    BEDROCK  = 99
    
    #Inventory.
    Inventory = {
                    DIRT    : 0,
                    GRASS   : 0,
                    STONE   : 0,
                    COAL    : 0,
                    IRON    : 0,
                    GOLD    : 0,
                    DIAMOND : 0,
    }
    
    #Dimentions.
    TILESIZE  = 32
    MAPWIDTH  = 32
    MAPHEIGHT = 24
    
    #Colours & Textures.
    if os.path.exists("Resources/Textures"):
        os.chdir("Resources/Textures")
        
        Textures = {
                    DIRT     : pygame.transform.scale(pygame.image.load('Dirt.jpg'), (TILESIZE, TILESIZE)),
                    GRASS    : pygame.transform.scale(pygame.image.load('Grass.png'), (TILESIZE, TILESIZE)),
                    STONE    : pygame.transform.scale(pygame.image.load('Stone_small.png'), (TILESIZE, TILESIZE)),
                    WATER    : pygame.transform.scale(pygame.image.load('Water_animated.gif'), (TILESIZE, TILESIZE)),
                    LAVA     : pygame.transform.scale(pygame.image.load('Lava_animated.gif'), (TILESIZE, TILESIZE)),
                    COAL     : pygame.transform.scale(pygame.image.load('Coal.png'), (TILESIZE, TILESIZE)),
                    OBSIDIAN : pygame.transform.scale(pygame.image.load('Obsidian_small.png'), (TILESIZE, TILESIZE)),
                    IRON     : pygame.transform.scale(pygame.image.load('Iron.png'), (TILESIZE, TILESIZE)),
                    GOLD     : pygame.transform.scale(pygame.image.load('Gold.png'), (TILESIZE, TILESIZE)),
                    DIAMOND  : pygame.transform.scale(pygame.image.load('Diamond.png'), (TILESIZE, TILESIZE)),
                    BEDROCK  : pygame.transform.scale(pygame.image.load('Bedrock.png'), (TILESIZE, TILESIZE)),
        }                                                                                                            
        
        os.chdir("../..")
    
    BROWN      = (97 , 65 , 38 )
    GREEN      = (0  , 255, 0  )
    GREY       = (189, 189, 189)
    BLUE       = (0  , 0  , 255)
    RED        = (255, 0  , 0  )
    BLACK      = (0  , 0  , 0  )
    PURPLE     = (17 , 5  , 27 )
    DARK_GREY  = (37 , 63 , 63 )
    YELLOW     = (255, 215, 0  )
    LIGHT_BLUE = (0  , 255, 255)
    PINK       = (255, 192, 203)
    WHITE      = (255, 255, 255)
    
    Colours = {
                DIRT     : BROWN,
                GRASS    : GREEN,
                STONE    : GREY,
                WATER    : BLUE,
                LAVA     : RED,
                COAL     : BLACK,
                OBSIDIAN : PURPLE,
                IRON     : DARK_GREY,
                GOLD     : YELLOW,
                DIAMOND  : LIGHT_BLUE,
                BEDROCK  : WHITE,
    }
    
    #Generates the map.
    Tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
    
    for line in range(0, MAPHEIGHT):
        for Tile in range(0, MAPWIDTH):
            RandomTile = random.randint(0,25)
            
            if RandomTile <= 4: Tilemap[line][Tile] = STONE
            
            elif (RandomTile >=5) and (RandomTile <=7): Tilemap[line][Tile] = GRASS
                
            elif (RandomTile == 8) or (RandomTile == 9): Tilemap[line][Tile] = COAL
                
            elif (RandomTile == 10) or (RandomTile == 11): Tilemap[line][Tile] = WATER
                
            elif (RandomTile == 12) or (RandomTile == 13): Tilemap[line][Tile] = LAVA
            
            elif RandomTile == 14:
                if random.randint(0, 1) == 0: Tilemap[line][Tile] = IRON
                
                if random.randint(0, 3) == 0: Tilemap[line][Tile] = GOLD
                
                if random.randint(0, 7) == 0: Tilemap[line][Tile] = DIAMOND
                
            else: Tilemap[line][Tile] = DIRT
    
    print(len(Tilemap))
    
    #Makes Obsidian.
    for line in range(0, MAPHEIGHT):
        print(Tilemap[line])
        
        for Tile in range(0, MAPWIDTH):
            if Tilemap[line][Tile] == LAVA:
                
                if (line - 1 >= 0) and (Tilemap[line - 1][Tile] == WATER):
                    Tilemap[line - 1][Tile] = OBSIDIAN
                
                if (Tile + 1 <= MAPWIDTH - 1) and (Tilemap[line][Tile + 1] == WATER):
                    Tilemap[line][Tile + 1] = OBSIDIAN
                
                if (line + 1 <= MAPHEIGHT - 1) and (Tilemap[line + 1][Tile] == WATER):
                    Tilemap[line + 1][Tile] = OBSIDIAN
                
                if (Tile - 1 >= 0) and (Tilemap[line][Tile - 1] == WATER):
                    Tilemap[line][Tile - 1] = OBSIDIAN
    
    #Initialises the game.
    pygame.init()    
    DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))
    pygame.display.set_caption("2D Platformer")
    PlayerPos = [0, 0]
    Tilemap[PlayerPos[1]][PlayerPos[0]] = OBSIDIAN
    
    #Checks for music files.
    if os.path.exists("Resources/Music"):
        os.chdir("Resources/Music")
        pygame.mixer.music.load("1. Ground Theme.mp3")
        pygame.mixer.music.set_volume(0.10)
        pygame.mixer.music.play(-1)
        os.chdir("../..")
    
    #Main loop.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_RIGHT and PlayerPos[0] < MAPWIDTH - 1: PlayerPos[0] += 1
                
                if event.key == K_LEFT and PlayerPos[0] > 0: PlayerPos[0] -= 1
                
                if event.key == K_DOWN and PlayerPos[1] < MAPHEIGHT - 1: PlayerPos[1] += 1
                
                if event.key == K_UP and PlayerPos[1] > 0: PlayerPos[1] -= 1
                
                if event.key == K_SPACE:
                    if Tilemap[PlayerPos[1]][PlayerPos[0]] in Inventory:
                        Inventory[Tilemap[PlayerPos[1]][PlayerPos[0]]] += 1
                        Tilemap[PlayerPos[1]][PlayerPos[0]] = BEDROCK
            
            if Tilemap[PlayerPos[1]][PlayerPos[0]] == LAVA:
                
                #Something needs to go here so that the user knows they died...
                
                if os.path.exists("Resources/Music"):
                    os.chdir("Resources/Music")
                    pygame.mixer.music.fadeout(500)
                    pygame.mixer.music.load("17. Lost a Life.mp3")
                    pygame.mixer.music.play(1)
                    os.chdir("../..")
                                    
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
            
                #Checks for texture files.
                if os.path.exists("Resources/Textures"):
                
                    os.chdir("Resources/Textures")
                    DISPLAYSURF.blit(Textures[Tilemap[row][column]], (column*TILESIZE, row*TILESIZE))
                    Player = pygame.transform.scale(pygame.image.load('Player_outline_large.png').convert_alpha(),
                                                (TILESIZE, TILESIZE))
                    os.chdir("../..")
                
                else:
                
                    pygame.draw.rect(DISPLAYSURF, Colours[Tilemap[row][column]], (column*TILESIZE, row*TILESIZE))
                    Player = pygame.draw.rect(DISPLAYSURF, PINK, (TILESIZE, TILESIZE))
                DISPLAYSURF.blit(Player, (PlayerPos[0]*TILESIZE, PlayerPos[1]*TILESIZE))
        
        PlacePos = 10
        INVFONT = pygame.font.Font('Resources/UbuntuMono-BI.ttf', 18)
        for item in Inventory:
            DISPLAYSURF.blit(Textures[item], (PlacePos, MAPHEIGHT*TILESIZE + 20))
            PlacePos += 50
            ItemAmountText = INVFONT.render(str(Inventory[item]), True, WHITE, BLACK)
            DISPLAYSURF.blit(ItemAmountText, (PlacePos, MAPHEIGHT*TILESIZE + 20))
            PlacePos += 70
            
        pygame.display.update()
    
Login()
