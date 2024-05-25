import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pong")

# Definindo as variáveis da raquete
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

# Definindo as variáveis da bola
BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Definindo as raquetes
paddle1 = pygame.Rect(50, (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)

# Definindo a bola
ball = pygame.Rect((SCREEN_WIDTH // 2) - (BALL_SIZE // 2), (SCREEN_HEIGHT // 2) - (BALL_SIZE // 2), BALL_SIZE, BALL_SIZE)

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    score1 = 0
    score2 = 0

    # Variáveis de controle de movimento
    paddle1_speed = 0
    paddle2_speed = 0
    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

    while True:
        # Capturando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle1_speed = -PADDLE_SPEED
                if event.key == pygame.K_s:
                    paddle1_speed = PADDLE_SPEED
                if event.key == pygame.K_UP:
                    paddle2_speed = -PADDLE_SPEED
                if event.key == pygame.K_DOWN:
                    paddle2_speed = PADDLE_SPEED
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle1_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle2_speed = 0

        # Movendo as raquetes
        paddle1.y += paddle1_speed
        paddle2.y += paddle2_speed

        # Limitando o movimento das raquetes
        if paddle1.top < 0:
            paddle1.top = 0
        if paddle1.bottom > SCREEN_HEIGHT:
            paddle1.bottom = SCREEN_HEIGHT
        if paddle2.top < 0:
            paddle2.top = 0
        if paddle2.bottom > SCREEN_HEIGHT:
            paddle2.bottom = SCREEN_HEIGHT

        # Movendo a bola
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Verificando colisões com as paredes superiores e inferiores
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_speed_y = -ball_speed_y

        # Verificando colisões com as raquetes
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed_x = -ball_speed_x

        # Verificando se a bola saiu da tela
        if ball.left <= 0:
            score2 += 1
            ball.x = (SCREEN_WIDTH // 2) - (BALL_SIZE // 2)
            ball_speed_x = BALL_SPEED_X
            ball_speed_y = BALL_SPEED_Y
        if ball.right >= SCREEN_WIDTH:
            score1 += 1
            ball.x = (SCREEN_WIDTH // 2) - (BALL_SIZE // 2)
            ball_speed_x = -BALL_SPEED_X
            ball_speed_y = -BALL_SPEED_Y

        # Preenchendo a tela com preto
        screen.fill(BLACK)

        # Desenhando os elementos do jogo
        pygame.draw.rect(screen, WHITE, paddle1)
        pygame.draw.rect(screen, WHITE, paddle2)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

        # Desenhando o placar
        font = pygame.font.Font(None, 74)
        text = font.render(str(score1), 1, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(score2), 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 250, 10))

        # Atualizando a tela
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
