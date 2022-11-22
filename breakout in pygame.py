#imports
import pygame


#imports paddle class
from paddle import Paddle
from ball import Ball
from brick import Brick
pygame.init()
#set variables
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


score = 0
lives = 3

#open the new screen
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('breakout game')

#list that will contain all sprites
all_sprites_list = pygame.sprite.Group()

#create the paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

#add paddle to list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
#sets fps
clock = pygame.time.Clock()

#will run until exited
carryOn = True
#main loop
while carryOn:
    for event in pygame.event.get(): #user does something
        if event.type == pygame.QUIT: #if user clicks exit
            carryOn = False #exit

                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(10)
            
    #---- game logic
    all_sprites_list.update()
    
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            
            carryOn = False
    
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]
    
    
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
      
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
            
        
    
    #fill screen
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    #displays score and lives
    font = pygame.font.Font(None, 34)
    text = font.render("Score :" +str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives :" +str(lives), 1, WHITE)
    screen.blit(text, (650,10))
    
    #draw sprites
    all_sprites_list.draw(screen)
    
    #update the screen
    pygame.display.flip()
    
    #set fps
    clock.tick(60)
    
pygame.quit()


