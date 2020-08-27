import pygame
import time
import random
from PIL import Image, ImageDraw

#строчка с фатальными изменениями

def tank(x, y): # Код отрисовки танка, взависимости от направления движения
    if direction == 'U':
        pygame.draw.rect(window, (250, 0, 250), (x, y, size/3, size))
        pygame.draw.rect(window, (0, 250, 250), (x+size/3*2, y, size/3, size))
        pygame.draw.rect(window, (250, 0, 0), (x+size/6, y+size/6, size/3*2, size/3*2))
        pygame.draw.rect(window, (250, 250, 0), (x+size/9*4, y, size/9, size/2))
    elif direction == 'D':
        pygame.draw.rect(window, (250, 0, 250), (x, y, size/3, size))
        pygame.draw.rect(window, (0, 250, 250), (x+size/3*2, y, size/3, size))
        pygame.draw.rect(window, (250, 0, 0), (x+size/6, y+size/6, size/3*2, size/3*2))
        pygame.draw.rect(window, (250, 250, 0), (x+size/9*4, y+size/2, size/9, size/2))
    elif direction == 'R':        
        pygame.draw.rect(window, (250, 0, 250), (x, y, size, size/3))
        pygame.draw.rect(window, (0, 250, 250), (x, y+size/3*2, size, size/3))
        pygame.draw.rect(window, (250, 0, 0), (x+size/6, y+size/6, size/3*2, size/3*2))
        pygame.draw.rect(window, (250, 250, 0), (x+size/9*4, y+size/9*4, size/2, size/9))  
    elif direction == 'L':          
        pygame.draw.rect(window, (250, 0, 250), (x, y, size, size/3))
        pygame.draw.rect(window, (0, 250, 250), (x, y+size/3*2, size, size/3))
        pygame.draw.rect(window, (250, 0, 0), (x+size/6, y+size/6, size/3*2, size/3*2))
        pygame.draw.rect(window, (250, 250, 0), (x, y+size/9*4, size/2, size/9))      


def Walls(Walls_types): #Код рисования стен
    image = Image.open(f"img/map{Walls_types}.png") # "img/map" + str(Walls_types) + ".png"
    pix = image.load()
    for i in range(0, screen_height):
        for j in range(0, screen_width):
            if pix[j, i][0] > 10 or pix[j, i][1] > 10 or pix[j, i][2] > 10:
                mat[i][j] = 1        
                pygame.draw.rect(window, pix[j, i], (j, i, 1, 1))
            else:
                mat[i][j] = 0        
    pygame.display.update()
    if Walls_types == 0:
        iszero = True
        while iszero: # Стартовый экран
            events = pygame.event.get()
            for i in range(len(events)):
                if events[i].type == pygame.QUIT:
                    pygame.quit()
                if events[i].type == pygame.KEYUP:
                    #mat = [[0] * screen_width for i in range(screen_height)]
                    pygame.draw.rect(window, (0, 0, 0), (0, 0, screen_width, screen_height))
                    iszero = False
                    Walls(random.randint(1, 5))
                    break


def laser(x, y, direction):
    if direction == 'U':
        pygame.draw.rect(window, (250, 0, 0), (x, 0, size, y))
        # pygame.display.update()
        for i in range(y):
            for j in range(x, x+size):
                if mat[i][j] == 1:
                    mat[i][j] = 0
        pygame.draw.rect(window, (0, 0, 0), (x, 0, size, y))
    elif direction == 'D':
        pygame.draw.rect(window, (250, 0, 0), (x, y+size, size, screen_height - y-size))
        for i in range(y+size, screen_height):
            for j in range(x, x+size):
                if mat[i][j] == 1:
                    mat[i][j] = 0
        pygame.draw.rect(window, (0, 0, 0), (x, y+size, size, screen_height - y-size))
    elif direction == 'R':        
        pygame.draw.rect(window, (250, 0, 0), (x, y, screen_width-x, size))
        for i in range(y, y+size):
            for j in range(x, screen_width):
                if mat[i][j] == 1:
                    mat[i][j] = 0
        pygame.draw.rect(window, (0, 0, 0), (x, y, screen_width-x, size))
    elif direction == 'L':          
        pygame.draw.rect(window, (250, 0, 0), (0, y, x, size))
        for i in range(y, y+size):
            for j in range(x):
                if mat[i][j] == 1:
                    mat[i][j] = 0
        pygame.draw.rect(window, (0, 0, 0), (0, y, x, size)) 


def draw_bullet(x, y, direction):
    if direction == 'U':
        pygame.draw.rect(window, (250, 0, 0), (x, 0, size, y))
        pygame.display.update()
        for i in range(y):
            for j in range(x, x+size):
                if mat[i][j] == 1:
                    mat[i][j] = 0
        pygame.draw.rect(window, (0, 0, 0), (x, 0, size, y))
    elif direction == 'D':
        pygame.draw.rect(window, (250, 0, 0), (x, 0, size, screen_height - y))
        for i in range(y, screen_height):
            for j in range(x, x+size):
                if mat[i][j] == 1:
                    mat[i][j] = 0
        pygame.draw.rect(window, (0, 0, 0), (x, 0, size, screen_height - y))
    elif direction == 'R':        
        pygame.draw.rect(window, (250, 0, 0), (x, y, screen_width-x, size))
        for i in range(y):
            for j in range(x, x+size):
                if mat[i][j] == 1:
                    mat[i][j] = 0
        pygame.draw.rect(window, (250, 0, 0), (0, y, x, size))
    elif direction == 'L':          
        pygame.draw.rect(window, (250, 0, 0), (0, y, x, size))
        for i in range(y):
            for j in range(x, x+size):
                if mat[i][j] == 1:
                    mat[i][j] = 0
        pygame.draw.rect(window, (0, 0, 0), (0, y, x, size))


def wall_horizontal(x, y, size):
    for i in range(size):
        if mat[y][x+i] == 1:
            return False
    return True


def wall_vertical(x, y, size):
    for i in range(size):
        if mat[y+i][x] == 1:
            return False
    return True


direction='U'  #направление танка      
screen_width = 800
screen_height = 600
mat = [[0] * screen_width for i in range(screen_height)]
is_fire = False
x = 500
y = 500
size = 60
border = 0
go_down = False
go_up = False
go_left = False
go_right = False
move_time = time.time()
kd_time = time.time()

pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
Walls(0) #  Число 0 выбирает случайных комплект стен. Числа 1 или 2 выбирают из существующих: 1 или 2   


#очистим текстуры под танком +1 пиксель
for i in range(y-1, y + size+1): 
    for j in range(x+1, x + size+1):
        mat[j][i] = 0
        pygame.draw.rect(window, (0, 0, 0), (j, i, 1, 1))


while True:
    events = pygame.event.get()
    for i in range(len(events)):
        if events[i].type == pygame.QUIT:
            pygame.quit()
        if events[i].type == pygame.KEYUP:
            if events[i].key == pygame.K_b and time.time() - kd_time > 5:
                kd_time = time.time()
                laser(x, y, direction)
            if events[i].key == pygame.K_DOWN or events[i].key == pygame.K_s:
                go_down = False
            if events[i].key == pygame.K_UP or events[i].key == pygame.K_w:
                go_up = False
            if events[i].key == pygame.K_RIGHT or events[i].key == pygame.K_d:
                go_right = False
            if events[i].key == pygame.K_LEFT or events[i].key == pygame.K_a:
                go_left = False
        if events[i].type == pygame.KEYDOWN:
            if events[i].key == pygame.K_SPACE and is_fire == False:
                is_fire = True
                bullet_x, bullet_y, bullet_direction, bullet_R = x+size//2, y+size//2, direction, size//3                
            if events[i].key == pygame.K_LEFT or events[i].key == pygame.K_a:
                go_left = True
            if events[i].key == pygame.K_RIGHT or events[i].key == pygame.K_d:
                go_right = True
            if events[i].key == pygame.K_UP or events[i].key == pygame.K_w:
                go_up = True
            if events[i].key == pygame.K_DOWN or events[i].key == pygame.K_s:
                go_down = True
    if time.time() - move_time > 0.01:
        move_time = time.time()
        pygame.draw.rect(window, (0, 0, 0), (x, y, size, size))
        if go_right and x + 1 + size <= screen_width - border and wall_vertical(x+size, y, size):
            x += 1
            direction='R'
        elif go_left and x - 1 >= border and wall_vertical(x-1, y, size):
            x -= 1
            direction='L'
        elif go_down and y + 1 + size <= screen_height - border and wall_horizontal(x, y+size, size):
            y += 1
            direction='D'
        elif go_up and y - 1 >= border and wall_horizontal(x, y-1, size):
            y -= 1
            direction='U'
        if is_fire == True:
            pygame.draw.circle(window, (0, 0, 0), (bullet_x, bullet_y), bullet_R)
            if bullet_direction == 'R':
                bullet_x += 4
            elif bullet_direction == 'L':                
                bullet_x -= 4               
            elif bullet_direction == 'D':                
                bullet_y += 4             
            elif bullet_direction == 'U':                
                bullet_y -= 4
                # 1) реализовать попадание снаряда в стену
                # 2) реализовать конец полёта, при выходе за рамки
            if (bullet_x < bullet_R or bullet_x > screen_width - bullet_R
                or bullet_y < bullet_R or bullet_y > screen_height - bullet_R):
                is_fire = False
            elif bullet_direction == 'R':
                if wall_vertical(bullet_x+bullet_R, bullet_y-bullet_R, bullet_R*2) == False:
                    is_fire = False
            elif bullet_direction == 'L':
                if wall_vertical(bullet_x-bullet_R, bullet_y-bullet_R, bullet_R*2) == False:
                    is_fire = False
            elif bullet_direction == 'D':
                if wall_horizontal(bullet_x-bullet_R, bullet_y-bullet_R, bullet_R*2) == False:
                    is_fire = False
            elif bullet_direction == 'U':
                if wall_horizontal(bullet_x-bullet_R, bullet_y-bullet_R, bullet_R*2) == False:
                    is_fire = False
            if is_fire == False:
                #print('print', bullet_y-size, bullet_y+size, bullet_x-size, bullet_x-size)
                for i in range(bullet_y-size, min(bullet_y+size, screen_height)):
                    for j in range(bullet_x-size, min(bullet_x+size, screen_width)):
                            mat[i][j] = 0        
                            pygame.draw.rect(window, (255, 0, 0), (j, i, 1, 1))
                tank(x, y)
                pygame.display.update()
                for i in range(bullet_y-size, min(bullet_y+size, screen_height)):
                    for j in range(bullet_x-size, min(bullet_x+size, screen_width)):                                  
                            pygame.draw.rect(window, (0, 0, 0), (j, i, 1, 1))
            else:
                pygame.draw.circle(window, (255, 0, 0), (bullet_x, bullet_y), bullet_R)
        #draw_bullet(x, y, direction)
        #print(direction)
        tank(x, y)
        pygame.display.update()