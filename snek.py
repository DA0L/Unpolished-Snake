import pygame
import random

def update_direction(keys):
    global direccioX, direccioY

    if keys[pygame.K_w]:
        direccioY = 1
        direccioX = -1

    if keys[pygame.K_a]:
        direccioX = 0
        direccioY = -1

    if keys[pygame.K_d]:
        direccioX = 1
        direccioY = -1

    if keys[pygame.K_s]:
        direccioY = 0
        direccioX = -1


def drawGrid(w, rows, surface):
	for i in range(1,rows+1):
		pygame.draw.line(surface, (0,255,0), (0,i*(w/rows)), (w,i*(w/rows)))
		pygame.draw.line(surface, (0,255,0), (i*(w/rows),0), (i*(w/rows), w))

def le_nek(snake_list, sf, snok):
    for m in snake_list:
        if m != snok:
            pygame.draw.rect(sf, (255,0,0), pygame.Rect(m[0]*(width/rows), m[1]*(width/rows), (width/rows)+1, (width/rows)+1))
        else:
            pygame.draw.rect(sf, (0,0,255), pygame.Rect(m[0]*(width/rows), m[1]*(width/rows), (width/rows)+1, (width/rows)+1))



def redrawWindow(surface, frux, fruy):
    global rows, width, square_xpos, square_ypos, x, y
    surface.fill((0,0,0))
    drawGrid(width,rows, surface)
    a = (255,0,0)


    if fruy == 25:
        fruy = 24
    if frux == 25:
        frux = 24
    pygame.draw.rect(surface, (255,255,255), pygame.Rect(frux*(width/rows), fruy*(width/rows), (width/rows)+1, (width/rows)+1))
    
def ptsdraw(surface):
    font = pygame.font.SysFont("Arial", 20)
    text = font.render('Points '+str(pts), True, (255,255,255))
    surface.blit(text,(0,0)) 



def main():
    global width, rows, square_xpos, square_ypos, direccioX, direccioY, x, y, frux, fruy, pts, win, dead
    dead = False
    width = 500
    rows = 25

    hs = []

    x = 0
    y = 0
    direccioX = -1
    direccioY = -1
    pts = 10000

    frux = random.randint(0, rows)
    fruy = random.randint(0, rows)

    snake_List = []
    Length_of_snake = 1

    pygame.init()


    
    win = pygame.display.set_mode((width,width))

    pygame.display.set_caption("SNAKE")

    square_xpos=20
    square_ypos=20
    dell = 100

    run = True
    startgem = True
    while run:  
        
        if startgem == True:
            my_font = pygame.font.SysFont('times new roman', 90)
            my_fontt = pygame.font.SysFont('times new roman', 15)
            game_start_surface = my_font.render('Controls', True, (255,0,0))
            game_start_surfacee = my_fontt.render('"F" to start  "W""A""S""D" to move  "V" and "B" to turn speed up and down', True, (255,255,255))
            game_start_rect = game_start_surface.get_rect()
            game_start_rectt = game_start_surfacee.get_rect()
            game_start_rect.midtop = (width/2, width/4)
            game_start_rectt.midtop = (width/2, width/2)
            win.fill((0,0,0))
            win.blit(game_start_surface, game_start_rect)
            win.blit(game_start_surfacee, game_start_rectt)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                startgem = False
                pygame.display.set_caption("SNAKE Points 0")
                x = 0
                y = 0 
                direccioX = -1
                direccioY = -1
                pts = 10000
                Length_of_snake = 1

                frux = random.randint(1, rows)
                fruy = random.randint(1, rows)
                snake_List = []
                Length_of_snake = 1

        if startgem != True:       
            drawGrid(width, rows, win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.time.delay(dell)
        pygame.display.set_caption("SNAKE Points "+str(pts))

        # Speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_v]:
            dell -= 5
        if keys[pygame.K_b]:
            dell += 10


        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for k in snake_List[:-1]:
            if snake_Head == k:
                dead = True

        update_direction(pygame.key.get_pressed())

        # Movement
        if dead != True:

            if direccioX == 1:
                x += 1
                pts -= 10
            if direccioX == 0:
                x -= 1
                pts -= 10
            if direccioY == 1:
                y -= 1
                pts -= 10
            if direccioY == 0:
                y += 1
                pts -= 10
        
        # Constraints
        if snake_Head[0] > rows-1:
            dead = True
            x = rows
        elif snake_Head[1] > rows-1:
            dead = True
            y = rows
        if snake_Head[0] < 0:
            dead = True
            x = -1
        elif snake_Head[1] < 0:
            dead = True
            y = -1 

        if x == frux and y == fruy:
            frux = random.randint(0, rows-1)
            fruy = random.randint(0, rows-1)
            pts += 1500
            Length_of_snake += 1

        if dead != True:
            redrawWindow(win, frux, fruy)
            le_nek( snake_List, win, snake_Head)
            ptsdraw(win)
            pygame.display.update()

        if dead == True:
            my_font = pygame.font.SysFont('times new roman', 90)
            my_fontt = pygame.font.SysFont('times new roman', 15)
            game_over_surface = my_font.render('YOU DIED', True, (255,0,0))
            game_over_surfacee = my_fontt.render('"F" to restart', True, (255,255,255))
            s_surfacee = my_fontt.render('Score: '+str(pts+10), True, (255,255,255))
            hs.append(pts+10)
            hs_surfacee = my_fontt.render('Highscore: '+str(max(hs)), True, (255,255,255))


            game_over_rect = game_over_surface.get_rect()
            game_over_rectt = game_over_surfacee.get_rect()
            s_rectt = s_surfacee.get_rect()
            hs_rectt = hs_surfacee.get_rect()
            game_over_rect.midtop = (width/2, width/4)
            game_over_rectt.midtop = (width/2, width/1.75)
            hs_rectt.midtop = (width/2, width/2)
            s_rectt.midtop = (width/2, width/1.87)
            win.fill((0,0,0))
            win.blit(game_over_surface, game_over_rect)
            win.blit(game_over_surfacee, game_over_rectt)
            win.blit(s_surfacee, s_rectt)
            win.blit(hs_surfacee, hs_rectt)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                dead = False
                pygame.display.set_caption("SNAKE Points 0")
                x = 0
                y = 0 
                direccioX = -1
                direccioY = -1
                pts = 10000
                Length_of_snake = 1

                frux = random.randint(1, rows)
                fruy = random.randint(1, rows)
                snake_List = []
                Length_of_snake = 1
        
    pygame.quit()
        
    
main()
