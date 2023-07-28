import pygame
import random
import sys
def ds():
    c = int(pygame.time.get_ticks() /1000)- st
    sc = tf.render(f'Score: {c}',False,'Black')
    sr = sc.get_rect(topleft = (40,20))
    screen.blit(sc,sr)
    return c
pygame.init()
r2 = random.randint(-5,760)
r3 = random.randint(-5,760)
screen = pygame.display.set_mode((800,650))
b = pygame.image.load("Dodgeball/back.png")
ball = pygame.image.load("Dodgeball/ball.png").convert_alpha()
balls = pygame.transform.scale(ball,(70,70))
ballr = balls.get_rect(center = (400,50))
ball2 = pygame.image.load("Dodgeball/ball.png").convert_alpha()
balls2 = pygame.transform.scale(ball,(70,70))
ballr2 = balls.get_rect(center = (r2,50))
ball3 = pygame.image.load("Dodgeball/ball.png").convert_alpha()
balls3 = pygame.transform.scale(ball,(70,70))
ballr3 = balls.get_rect(center = (r3,50))
plr = pygame.image.load("Dodgeball/Player.png").convert_alpha()
plrs = pygame.transform.scale(plr,(100,100))
plrr = plrs.get_rect(center = (400,580))

Pe = pygame.image.load("Dodgeball/Person.webp").convert_alpha()
Pes = pygame.transform.scale(Pe,(150,240))
Per = Pes.get_rect(center = (400,243))
clock = pygame.time.Clock()
game = True

Lives = 3
st = 0
r = pygame.Surface((600,400))
r.fill('Sky blue')
rr = r.get_rect(center = (400,324.5))
tf = pygame.font.Font("Dodgeball/text.ttf",100)


re = tf.render(f'RESTART',False,'Red')
rer = re.get_rect(center = (400,400))
while True:
    rx = random.randint(-5,760)
    rx2 = random.randint(-5,760)
    rx3 = random.randint(-5,760)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game == True:
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                plrr.x -= 5
            
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                plrr.x += 5
        if ballr.colliderect(plrr):
            ballr.y = -50
            Lives -= 1
        if ballr2.colliderect(plrr):
            ballr2.y = -50
            Lives -= 1
        if ballr3.colliderect(plrr):
            ballr3.y = -50
            Lives -= 1
        if Lives <= 0:
            game = False
        ballr.y += 8
        if ballr.y >= 700:
            ballr.y = -50
            ballr = balls.get_rect(center = (rx,50))
        ballr2.y += 8
        if ballr2.y >= 700:
            ballr2.y = -50
            ballr2 = balls2.get_rect(center = (rx2,50))
        ballr3.y += 8
        if ballr3.y >= 700:
            ballr3.y = -50
            ballr3 = balls2.get_rect(center = (rx3,50))
        if plrr.x >= 750:
            plrr.x -= 15
        if plrr.x <= 0:
            plrr.x += 10
        
        screen.blit(b,(0,0))
        screen.blit(balls,ballr)
        screen.blit(balls2,ballr2)
        screen.blit(balls3,ballr3)
        screen.blit(plrs,plrr)
        
        ds()
    else:
        screen.blit(r,rr)
        screen.blit(re,rer)
        screen.blit(Pes,Per)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rer.collidepoint(event.pos):
                st = int(pygame.time.get_ticks() /1000)
                Lives = 3
                game = True

    if Lives <= 0:
        Lives = 0
    lc = tf.render(f'Lives: {Lives}',False,'Black')
    lr = lc.get_rect(center = (130,600))
    screen.blit(lc,lr)
    pygame.display.update()
    clock.tick(60)