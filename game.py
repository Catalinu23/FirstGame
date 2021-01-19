import pygame
pygame.init()
pygame.mixer.init()

display_height = 720
display_width = 1280

pygame.mixer.music.load("files/track.mp3")

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
bg = pygame.image.load("files/bg.jpg")

x_rect = display_width / 2
y_rect = display_height - 70
left_limit = x_rect
right_limit = x_rect + 240
vel = 2

radius = 12
x_circle = 1000
y_circle = 20
vel_circle_x = 1
vel_circle_y = 2


def ok(x):
    return int(x_rect) <= x_circle and x_circle <= int(x_rect+240)

## MAIN
run = True
pygame.mixer.music.play(-1)
while run == True:
    clock.tick(75)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x_rect -= vel
        if(x_rect < 0):
            x_rect = 0
    if keys[pygame.K_RIGHT]:
        x_rect += vel
        if(x_rect + 240 > display_width):
            x_rect = display_width - 240

    if (x_circle == 0 or x_circle == display_width) :
        vel_circle_x *= (-1)
    if (y_circle == 0 or (ok(x_circle) and y_circle == y_rect) ) :
        vel_circle_y *= (-1)
    if y_circle >= display_height:
        run = False

    x_circle += vel_circle_x
    y_circle += vel_circle_y


    win.blit(bg, (0,0))



    pygame.draw.rect(win, (144, 45, 243), ((x_rect, y_rect), (240, 40)))
    pygame.draw.circle(win, (10, 65, 249), (x_circle, y_circle), radius)
    pygame.display.update()

pygame.quit()
