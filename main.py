
import pygame 
pygame.init() 
W_width =700
W_height = 500
win = pygame.display.set_mode((W_width, W_height)) 
pygame.display.set_caption("PINGPONG") 
m_vel = 7
L_x = 10
L_y = 200
R_x = 680
R_y = 200
L_width = 10
L_height = 90
R_width = 10
R_height = 90
ball_radius = 7
B_x = W_width//2
B_y = W_height//2
vel = 7
ball_x_vel = 5
ball_y_vel = 0
FPS = 60