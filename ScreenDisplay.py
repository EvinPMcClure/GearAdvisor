import pygame


pygame.init() #initialising pygame

DISPLAY_WIDTH = 390 #setting height - Any drawn is based off a percentage of the width and height 
DISPLAY_HEIGHT = 700 #setting width
Display_Size = [DISPLAY_WIDTH, DISPLAY_HEIGHT] #creating display size
screen = pygame.display.set_mode(Display_Size) #creating screen - can be called when ready to show 

BLACK = [0,0,0]
WHITE = [255,255,255]
FPS = 60

IPHONE_IMAGE = pygame.image.load('iphone.png') #loading image in 
IPHONE_POSITION = [0,0]
iphone_size = pygame.transform.scale(IPHONE_IMAGE,(DISPLAY_WIDTH,DISPLAY_HEIGHT))








clock = pygame.time.Clock() 

rec_width = DISPLAY_WIDTH * 0.6
rec_height = DISPLAY_HEIGHT* 0.35
rec_Colour = red = [255,255,255]

box = (rec_width,rec_height)
x_axis = (DISPLAY_WIDTH // 2) - (box[0] // 2)
y_axis = (DISPLAY_HEIGHT // 2) - (box[1]//2)

rec_start = (x_axis, y_axis)
Rectangle = pygame.Rect(rec_start, box)



Imaginary = ('Maintain', 5)
commands = ('Maintain', 'Go Up', 'Go down')




pygame.display.set_caption('Show Text')
 

font = pygame.font.Font('freesansbold.ttf', 20)

centre = (x_axis, y_axis)


x = ('Miantain', 5)


def intro():
    screen.fill(BLACK)
    screen.blit(iphone_size, IPHONE_POSITION)
    pygame.draw.rect(screen, WHITE, Rectangle)
    intro_text = font.render('Welcome to the OBD2 app', True, BLACK)

    screen.blit(intro_text,centre)
    
    pygame.display.update()
    clock.tick(FPS) #sets clock to reset at 60 FPS 
    main()


def text_maintain(gear):
    screen.fill(BLACK)
    screen.blit(iphone_size, IPHONE_POSITION)
    pygame.draw.rect(screen, WHITE, Rectangle)

    text_maintain = font.render('Maintain Gear ' + str(gear), True, BLACK)
    screen.blit(text_maintain,centre)
    
    pygame.display.update()
    clock.tick(FPS) #sets clock to reset at 60 FPS 
    main()

def text_up(gear):
    screen.fill(BLACK)
    screen.blit(iphone_size, IPHONE_POSITION)
    pygame.draw.rect(screen, WHITE, Rectangle)

    text_go_up = font.render('Go up a gear to ' + str(gear), True, BLACK)
    screen.blit(text_go_up,centre)
    
    pygame.display.update()
    clock.tick(FPS) #sets clock to reset at 60 FPS 
    main()

def text_down(gear):
    screen.fill(BLACK)
    screen.blit(iphone_size, IPHONE_POSITION)
    pygame.draw.rect(screen, WHITE, Rectangle)

    text_go_down = font.render('Go up a gear to ' + str(gear), True, BLACK)
    screen.blit(text_go_down,centre)
    
    pygame.display.update()
    clock.tick(FPS) #sets clock to reset at 60 FPS 
    main()


def main():
    running = True
    while running:
    # The event loop.
        #print(event) # test to see event 
        for event in pygame.event.get():
        # If a pygame.QUIT event is in the queue.
            if event.type == pygame.QUIT :
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #If the escape key was pressed
                    running = False
                    pygame.quit()
                    quit()

        
        # To check if it was a `KEYDOWN` event.
        if x[0] == 'Maintain':
            text_maintain(x[1])
        elif x[0] == 'Up':
            text_up(x[1])
        elif x[0] == 'Down':
            text_down(x[1])
        else:
            intro()
            
        

    pygame.quit()



main()