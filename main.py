import pygame
import random

pygame.init()
screen_width = 1280
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game!")

clock = pygame.time.Clock()

ball = pygame.Rect(0,0,30,30)
ball.center = (screen_width/2, screen_height/2)

computer_paddle = pygame.Rect(0,0,20,100)
computer_paddle.centery = screen_height/2

player_paddle = pygame.Rect(0,0,20,100)
player_paddle.midright = (screen_width, screen_height/2)

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
computer_speed = 5

computer_points, player_points = 0, 0
score_font = pygame.font.Font(None, 100)

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10,100)
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])
def point_won(winner):
    global computer_points, player_points

    if winner == "Computer":
        computer_points += 1
    if winner == "Player":
        player_points += 1

    reset_ball()

def animate_player():

    player_paddle.y += player_speed

    if player_paddle.top <= 0:
        player_paddle.top = 0

    if player_paddle.bottom >= screen_height:
        player_paddle.bottom = screen_height

def animate_computer():
    global computer_speed
    computer_paddle.y += computer_speed

    if ball.centery <= computer_paddle.centery:
        computer_speed = -5
    if ball.centery >= computer_paddle.centery:
        computer_speed = 5

    if computer_paddle.top <= 0:
        computer_paddle.top = 0
    if computer_paddle.bottom >= screen_height:
        computer_paddle.bottom = screen_height
        
def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1

    if ball.right >= screen_width:
        point_won("Computer")

    if ball.left <= 0:
        point_won("Player")

    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        ball_speed_x *= -1


while True:
    #Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed = 0

    animate_player()
    animate_ball()
    animate_computer()

    screen.fill('black')

    # Draw the score
    computer_score_surface = score_font.render(str(computer_points), True, "white")
    player_score_surface = score_font.render(str(player_points), True, "white")
    screen.blit(computer_score_surface, (screen_width / 4, 20))
    screen.blit(player_score_surface, (3 * screen_width / 4, 20))

    # Draw the game objects
    pygame.draw.aaline(screen, 'white', (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.ellipse(screen, 'white', ball)
    pygame.draw.rect(screen, 'white', computer_paddle)
    pygame.draw.rect(screen, 'white', player_paddle)

    # Update the display
    pygame.display.update()
    clock.tick(60)





