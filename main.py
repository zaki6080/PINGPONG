
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
    score = font.render(str(R_score), True, (255, 255, 255))
    win.blit(score, (R_x, R_y))
    score = font.render(str(L_score), True, (255, 255, 255))
    win.blit(score, (L_x, L_y))
    #pygame.display.update()

def Winner():
    pass

def reset():
    global B_x
    global B_y
    global ball_y_vel
    global ball_x_vel
    global ball_x_vel
    if B_x <=0 or B_x >= W_width:
       B_x = W_width//2
       B_y = W_height//2
       ball_x_vel = 5
       ball_y_vel = 0
      
def Y_Boundary_Collision():
   global ball_y_vel
   if B_y + ball_radius > W_height or B_y - ball_radius < 0:
       ball_y_vel *= -1
   #return  ball_y_vel

def X_Boundary_Collision():
    global ball_y_vel
    global ball_x_vel      
    if ball_x_vel < 0:
       if B_y >= L_y and B_y <= L_y + L_height:
           if B_x - ball_radius <= L_x + L_width:
                ball_x_vel *= -1

                middle_y = L_y + L_height / 2
                difference_in_y = middle_y - B_y
                reduction_factor = (L_height / 2) / m_vel
                y_vel = difference_in_y / reduction_factor
                ball_y_vel = -1 * y_vel

                middle_y = L_y + L_height / 2
                difference_in_y = middle_y - B_y
                reduction_factor = (L_height / 2) / m_vel
                y_vel = difference_in_y / reduction_factor
                ball_y_vel = -1 * y_vel
    else:
            if B_y >= R_y and B_y <= R_y + R_height:
              if B_x + ball_radius >= R_x:
                 ball_x_vel *= -1                                      
                 middle_y = R_y + R_height / 2
                 difference_in_y = middle_y - B_y
                 reduction_factor = (R_height / 2) / m_vel
                 y_vel = difference_in_y / reduction_factor
                 ball_y_vel = -1 * y_vel