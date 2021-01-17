import pygame
pygame.init()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("First Game")

x = 100
y = 100
radius = 8
vel = 8

run = True
while run == True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        if(x < 0):
            x = 0
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))
    pygame.draw.circle(win, (10, 240, 20), (x, y), radius)
    pygame.display.update()

pygame.quit()
