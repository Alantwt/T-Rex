import pygame
from src.player.t_rex import T_Rex


def main():
    
    pygame.init()

    # Screen Settings
    main_screen = pygame.display.Info()
    screen_width,screen_height = main_screen.current_w,main_screen.current_h-70
    screen = pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE,display=0)
    clock = pygame.time.Clock()
    pygame.display.set_caption('T-Rex','rex')

    ground = pygame.Rect(0,screen_height-10,screen_width,10)

    # Player    
    t_rex = T_Rex(x=screen.get_width()/2,y=screen.get_height()/2)

    game_loop = True

    while game_loop:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            if event.type == pygame.VIDEORESIZE:
                print(screen.get_size())
                t_rex.set_position(x=screen.get_width()/2,y=screen.get_height()/2)

        # Entrada de usuario
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_d]:
            print(t_rex._rect.x,t_rex._rect.y)
            t_rex.run()
        elif keys_pressed[pygame.K_s]:
            print(t_rex._rect.x,t_rex._rect.y)
            t_rex.down_run()
        else:
            # print(t_rex._rect.x,t_rex._rect.y)
            t_rex.stop()
        
        

        

        # Screen Settings
        screen.fill(color='grey')
        clock.tick(60)

        # Dibujar en pantalla
        screen.blit(t_rex.img,t_rex._rect)
        pygame.draw.rect(screen,(0,0,0),ground)

        # Actualizar pantalla
        pygame.display.flip()

        




if __name__ == '__main__':
    main()