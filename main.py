import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((800,700),pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption('T-Rex','rex')

    runing = True

    t_rex = pygame.Rect(screen.get_width()/3.5,screen.get_height()-110, 50, 100)
    ground = pygame.Rect(0,screen.get_height()-10,screen.get_width(),10)
    speed = 5
    keys_pressed = pygame.key.get_pressed()
    can_jump = True
    gravity = 1
    jump = 24
    is_jump = False
    down = False
    obstacle = pygame.Rect(screen.get_width(),screen.get_height()-60,30,50)

    while runing:
        down = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
            if event.type == pygame.VIDEORESIZE:
                ground = pygame.Rect(0,screen.get_height()-10,screen.get_width(),10)
                t_rex = pygame.Rect(screen.get_width()/3.5,screen.get_height()-110, 50, 100)


        # Obstaculos
        obstacle.x -= speed
        if obstacle.colliderect(t_rex):
            print("Perdiste")
        

        # Obtener teclas
        keys_pressed = pygame.key.get_pressed()

        # Actualizar posicion del rectangulo
        if keys_pressed[pygame.K_s]:
            down = True
            t_rex = pygame.Rect(t_rex.x,screen.get_height()-60, 50, 50)
            
        if down == False:
            t_rex = pygame.Rect(t_rex.x,t_rex.y if t_rex.height == 100 else t_rex.y-50, 50, 100)

        
        
        # Iniciacion del salto
        if can_jump and keys_pressed[pygame.K_SPACE] and is_jump == False and not down:
            t_rex.y -= jump
            can_jump = False
            gravity = 1
            is_jump = True
            jump = 24

        # Salto prolongado
        if is_jump and jump > 0:
            jump -= 1
            t_rex.y -= jump

        # Efecto de gravedad    
        gravity += 0.5
        
        if not can_jump:
            t_rex.y += gravity
            if t_rex.colliderect(ground):
                t_rex.y = ground.y - t_rex.height
                can_jump = True
                is_jump = False


        # Actualizar el color pantalla 
        screen.fill(color='grey')
        # Frames por segundo
        clock.tick(60)
        # Dibujar el suelo
        pygame.draw.rect(screen,(0,0,0),ground)
        # dibujar el trex
        pygame.draw.rect(screen,(255, 0, 0), t_rex)
        # dibujar los obstaculos
        pygame.draw.rect(screen,(123,134,9),obstacle)
        
        # Actualizar toda la pantalla
        pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
    main()