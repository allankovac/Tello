from djitellopy.tello import Tello
import time
import pygame

pygame.init()
display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
tello = Tello()
S = 60

def eventoKeyDown(event):
    if event.key == pygame.K_r:
        tello.takeoff()
    elif event.key == pygame.K_p:
        tello.land()
    elif event.key == pygame.K_w:
        tello.send_rc_control(0, 0, S,0)
    elif event.key == pygame.K_s:
        tello.send_rc_control(0, 0, -S, 0)
    elif event.key == pygame.K_a:
        tello.send_rc_control(0, 0, 0, -S)
    elif event.key == pygame.K_d:
        tello.send_rc_control(0, 0, 0,  S)
    elif event.key == pygame.K_UP:
        tello.send_rc_control(0, S, 0, 0)
    elif event.key == pygame.K_DOWN:
        tello.send_rc_control(0, -S, 0, 0)
    elif event.key == pygame.K_LEFT:
        tello.send_rc_control(-S, 0, 0, 0)
    elif event.key == pygame.K_RIGHT:
        tello.send_rc_control(S, 0, 0, 0)

def eventoKeyUp(event):
    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        tello.send_rc_control(0, 0, 0, 0)
    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        tello.send_rc_control(0, 0, 0, 0)
    elif event.key == pygame.K_w or event.key == pygame.K_s:
        tello.send_rc_control(0, 0, 0, 0)
    elif event.key == pygame.K_a or event.key == pygame.K_d:
        tello.send_rc_control(0, 0, 0, 0)

def main():
    tello.connect()
    pygame.display.set_caption("Tello video stream")
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    sair = False
    while not sair:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                tello.land()
                sair = True
            elif event.type == pygame.KEYDOWN:
                eventoKeyDown(event = event)
            elif event.type == pygame.KEYUP:
                eventoKeyUp(event = event)
        display.fill((255,255,2))
        textsurface = myfont.render('Bateria:'+str(tello.get_battery())+'% | Altitude: '+ str(tello.get_attitude()) + ' | Altura: '+ str(tello.get_height())+'cm', False, (0, 188, 0))
        display.blit(textsurface,(0,0))
        pygame.display.update()

    tello.end()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
