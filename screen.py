import pygame


pygame.init() #initialising pygame
DISPLAY_WIDTH = 390 #setting height - Any drawn is based off a percentage of the width and height 
DISPLAY_HEIGHT = 700 #setting width


iphone = pygame.image.load('iphone.png') #loading image in 
iphone_position = [0,0]

Display_Size = [DISPLAY_WIDTH, DISPLAY_HEIGHT] #creating display size


screen = pygame.display.set_mode(Display_Size) #creating screen - can be called when ready to show 


clock = pygame.time.Clock() 
BLACK = [0,0,0]
rec_width = DISPLAY_WIDTH * 0.6
rec_height = DISPLAY_HEIGHT* 0.35
rec_Colour = red = [255,255,255]

Box = (rec_width,rec_height)

centre = ((DISPLAY_WIDTH // 2) - (Box[0] // 2), (DISPLAY_HEIGHT // 2) - (Box[1]//2))
print(centre)
Rectangle = pygame.Rect(centre, Box)



Imaginary = ('Maintain', 5)
commands = ('Maintain', 'Go Up', 'Go down')




pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render('Welcome to the OBD2 app', True, BLACK)

 


def main():
    running = True  
    while running:
    # The event loop.
        #print(event) # test to see event 
        # If a pygame.QUIT event is in the queue.
        if event.type == pygame.QUIT :
            running = False
        # To check if it was a `KEYDOWN` event.
        
        screen.fill(BLACK)
        pygame.display.update()

    
    screen.blit(iphone, iphone_position)
    pygame.display.flip(text,centre)
    
    
    for event in pygame.event.get():
    
        
        for command in commands:
            if command == Imaginary[0]:
                print('hello')
                
                

        # Use pygame.key.get_pressed to see if a key is held down.
    key = pygame.key.get_pressed()
    # This should not be in the event loop.
    if key[pygame.K_UP]:
        print('up arrow pressed')


    pygame.display.update()
    clock.tick(60)
    
    
pygame.quit()
quit()

#Update_Advice = (input('Gear command'), input('Gear number'))



