
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
clock =pygame.time.Clock()
run = True
font = pygame.font.Font('freesansbold.ttf', 32)
L_score = 0
R_score = 0
R_score_text_y = 10
R_score_text_x = 670
L_score_text_y = 10
L_score_text_x = 10
def start():
    global B_x
    global B_y
    B_x += ball_x_vel
    B_y += ball_y_vel

def score ():
   global B_x
   global B_y
   global R_score
   global L_score 
   global ball_y_vel
   global ball_x_vel

   if B_x <= 0:
      start()
      R_score +=1
      B_x = W_width//2
      B_y = W_height//2
      ball_x_vel = 9
      ball_y_vel = 0
   elif B_x >= W_width:
      start()
      L_score +=1
      B_x = W_width//2
      B_y = W_height//2
      ball_x_vel = 9
      ball_y_vel = 0
def show_score(R_x, R_y,L_x,L_y):
   global B_x
   global B_y
   global R_score
   global L_score 
   global ball_y_vel
   global ball_x_vel

   #B_x += ball_x_vel
   #B_y += ball_y_vel