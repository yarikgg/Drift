import pygame  # moduls
pygame.font.init()
w = 640  # screen resolution
h = 480
# window
display = pygame.display.set_mode((w, h))
pygame.display.set_caption('Drift')
p1 = pygame.image.load('assets/p1.png')
p2 = pygame.image.load('assets/p2.png')
map = pygame.image.load('assets/map.png')
# some variabls
menu = True

px = 510
py = 351

px2 = 473
py2 = 351

speed = 0.1

result = 0
result2 = 0

y_control = 0
x_control = 0

finish_controler = None
finish_controler2 = None

y_control2 = 0
x_control2 = 0

# main loop
start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # player 1
                y_control = 1
            elif event.key == pygame.K_s:
                y_control = -1
            elif event.key == pygame.K_a:
                x_control = -1
            elif event.key == pygame.K_d:
                x_control = 1
            if event.key == pygame.K_UP:  # player 2
                y_control2 = 1
            elif event.key == pygame.K_DOWN:
                y_control2 = -1
            elif event.key == pygame.K_LEFT:
                x_control2 = -1
            elif event.key == pygame.K_RIGHT:
                x_control2 = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                y_control = 0
                speed = 0.2
            elif event.key == pygame.K_s:
                y_control = 0
                speed = 0.2
            elif event.key == pygame.K_a:
                x_control = 0
                speed = 0.2
            elif event.key == pygame.K_d:
                x_control = 0
                speed = 0.2
            elif event.key == pygame.K_UP:
                y_control2 = 0
                speed = 0.2
            elif event.key == pygame.K_DOWN:
                y_control2 = 0
                speed = 0.2
            elif event.key == pygame.K_LEFT:
                x_control2 = 0
                speed = 0.2
            elif event.key == pygame.K_RIGHT:
                x_control2 = 0
                speed = 0.2
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    # move
    if y_control == 1 and x_control == 1:  # DRIIIIIIIFFFFFT:) p1
        py -= speed-0.04
        px += speed-0.04
        p1 = pygame.image.load('assets/p1_drift_up_right.png')
        result += 1
    elif y_control == -1 and x_control == 1:
        py += speed-0.04
        px += speed-0.04
        p1 = pygame.image.load('assets/p1_drift_back_right.png')
        result += 1
    elif y_control == -1 and x_control == -1:
        py += speed-0.04
        px -= speed-0.04
        p1 = pygame.image.load('assets/p1_drift_back_left.png')
        result += 1
    elif y_control == 1 and x_control == -1:
        py -= speed-0.04
        px -= speed-0.04
        p1 = pygame.image.load('assets/p1_drift_up_left.png')
        result += 1
    elif y_control == 1:
        py -= speed
        speed += 0.001
        p1 = pygame.image.load('assets/p1.png')
    elif y_control == -1:
        py += speed
        speed += 0.001
        p1 = pygame.image.load('assets/p1_back.png')
    elif x_control == 1:
        px += speed
        speed += 0.001
        p1 = pygame.image.load('assets/p1_right.png')
    elif x_control == -1:
        px -= speed
        speed += 0.001
        p1 = pygame.image.load('assets/p1_left.png')
    # player 2
    if y_control2 == 1 and x_control2 == 1:  # DRIIIIIIIFFFFFT:)
        py2 -= speed-0.05
        px2 += speed-0.05
        result2 += 1
        p2 = pygame.image.load('assets/p2_drift_up_left.png')
    elif y_control2 == -1 and x_control2 == 1:
        py2 += speed-0.05
        px2 += speed-0.05
        p2 = pygame.image.load('assets/p2_drift_back_right.png')
        result2 += 1
    elif y_control2 == -1 and x_control2 == -1:
        py2 += speed-0.05
        px2 -= speed-0.05
        p2 = pygame.image.load('assets/p2_drift_left.png')
        result2 += 1
    elif y_control2 == 1 and x_control2 == -1:
        py2 -= speed-0.05
        px2 -= speed-0.05
        p2 = pygame.image.load('assets/p2_drift_up_right.png')
        result2 += 1
    elif y_control2 == 1:
        py2 -= speed
        speed += 0.001
        p2 = pygame.image.load('assets/p2.png')
    elif y_control2 == -1:
        py2 += speed
        speed += 0.001
        p2 = pygame.image.load('assets/p2_back.png')
    elif x_control2 == 1:
        px2 += speed
        speed += 0.001
        p2 = pygame.image.load('assets/p2_right.png')
    elif x_control2 == -1:
        px2 -= speed
        speed += 0.001
        p2 = pygame.image.load('assets/p2_left.png')
    # main game
    f2 = pygame.font.SysFont('Arial', 48)
    text2 = f2.render(str(result2), True,
                      (255, 0, 0))
    f = pygame.font.SysFont('Arial', 48)
    text = f.render(str(result), True,
                    (255, 0, 0))
    if px <= 78 or py <= 12 or px >= 550 or py >= 430 or px >= 162 and py >= 146 and px < 465 and px > 161 and py < 341:  # for p1
        result -= 1
    if px2 <= 78 or py2 <= 12 or px2 >= 550 or py2 >= 430 or px2 >= 162 and py2 >= 146 and px2 < 465 and px2 > 161 and py2 < 341:  # for p2
        result2 -= 1
    if result >= 1000:
        print("p1 win")
    if result2 >= 1000:
        print("p2 win")
    # if px >= 282 and py < 144:
        #finish_controler = True
    # if px2 >= 282 and py2 < 144:
        #finish_controler2 = True
    # if finish_controler == True and px >= 216 and py <= 430 and py >= 343:
        #print(px, py)
    # if finish_controler == True and px2 >= 216 and py2 <= 430 and py2 >= 343:
        #print(px2, py2)
    # draw object
    display.blit(map, (0, 0))
    display.blit(text2, (0, 20))
    display.blit(text, (570, 20))
    display.blit(p2, (px2, py2))
    display.blit(p1, (px, py))
    pygame.display.update()
