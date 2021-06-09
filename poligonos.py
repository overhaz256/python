import sys
import pygame

pygame.init()

width = 500

height = 600

surface = pygame.display.set_mode( (width, height) ) #superficie

pygame.display.set_caption('Objetos2')

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

#pygame.mixer.music.load('sonidos/Haggstrom.mp3')
#pygame.mixer.music.play()

imagen = pygame.image.load('imagenespy/codi.png')
rect = imagen.get_rect()
rect.center = (width // 2, height // 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a :
                message = 'Izquierda'

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                message = 'Derecha'

            if event.key == pygame.K_DOWN or event.key == pygame.K_s :
                message = 'Abajo'

            if event.key == pygame.K_UP or event.key == pygame.K_w :
                message = 'Arriba'

            print(message)

        if event.type == pygame.KEYUP:
           # print('Tecla liberada')
            pass
    surface.fill(white)
   
    
    pygame.display.update()    