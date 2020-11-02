from motorcontroller import *
import logging
import pygame
import logging
pygame.init()


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Mecanum controller")

x = 50
y = 50
width = 40
height = 60
vel = 5*2

drive_time = 0.2
drive_speed = 'LOW'

run = True
motor_controller = MotorController()
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    move = False

    
    # Change motorspeed of the robot.
    speed_premap = 0
    if keys[pygame.K_t]:
        try:
            speed_premap = (input("set speed from 0 to 100: "))
            if not type(speed_premap) is int:
                raise TypeError("Please only use integers for speed setting ")
            elif (speed_premap < 0) or (speed_premap > 100):
                raise ValueError("Speedrange is from 0 to 100: ")
        except Exception as e:
                print("Error occured ", e)
        motor_controller.speed_change(speed_premap)
        
        """ if drive_speed == 'LOW':
            drive_speed = 'HIGH'
            print('Drive speed is now HIGH')
        elif drive_speed == 'HIGH':
            drive_speed = 'LOW'
            print('Drive speed is now LOW')       
        """
        
    if (keys[pygame.K_w] and keys[pygame.K_d])   or (keys[pygame.K_UP] and keys[pygame.K_RIGHT]):
        logging.debug('wd')
        move = True; y -= vel; x += vel
        motor_controller.diagonals(direction = 'wd', drivetime = drive_time)
    elif (keys[pygame.K_w] and keys[pygame.K_a]) or (keys[pygame.K_UP] and keys[pygame.K_LEFT]):
        logging.debug('wa')
        move = True; y -= vel; x -= vel
        motor_controller.diagonals(direction = 'wa', drivetime = drive_time)
    elif (keys[pygame.K_s] and keys[pygame.K_d]) or (keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]):
        logging.debug('sd')
        move = True; y += vel; x += vel
        motor_controller.diagonals(direction = 'sd', drivetime = drive_time)
    elif (keys[pygame.K_s] and keys[pygame.K_a]) or (keys[pygame.K_DOWN] and keys[pygame.K_LEFT]):
        logging.debug('sa')
        move = True; y += vel; x -= vel
        motor_controller.diagonals(direction = 'sa', drivetime = drive_time)
    elif keys[pygame.K_w] or keys[pygame.K_UP]:
        logging.debug('up')
        move = True
        y -= vel
        motor_controller.forward(drivetime = drive_time)
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        logging.debug('down')
        move = True
        y += vel
        motor_controller.backward(drivetime = drive_time)
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        logging.debug('left')
        move = True
        x -= vel
        motor_controller.left(drivetime = drive_time)
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        logging.debug('right')
        move = True
        x += vel
        motor_controller.right(drivetime = drive_time)
    elif keys[pygame.K_q]:
        logging.debug('counterclockwise')
        move = True
        motor_controller.rotate(direction = 'q',drivetime = drive_time)
    elif keys[pygame.K_e]:
        logging.debug('clockwise')
        move = True
        motor_controller.rotate(direction = 'e',drivetime = drive_time)   
    
    if move == False:
        motor_controller.stop()
    else:
        pass
        
    
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()