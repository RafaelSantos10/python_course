import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Configurações da cobra
snake_block_size = 10
snake_speed = 15


# Função para desenhar a cobra na tela
def draw_snake(snake_block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(
            screen, GREEN, [block[0], block[1], snake_block_size, snake_block_size]
        )


# Loop do jogo
def gameLoop():
    game_over = False
    game_close = False

    # Inicialização da posição da cobra
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Inicialização das mudanças de posição
    x1_change = 0
    y1_change = 0

    # Inicialização da lista da cobra
    snake_List = []
    Length_of_snake = 1

    # Posição aleatória da comida
    foodx = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0

    # Loop principal
    while not game_over:
        # Game over
        while game_close == True:
            screen.fill(WHITE)
            font = pygame.font.SysFont("comicsansms", 35)
            message = font.render(
                "Você perdeu! Aperte Q para sair ou C para jogar novamente", True, RED
            )
            screen.blit(message, [screen_width / 6, screen_height / 3])

            # Atualizar a tela
            pygame.display.update()

            # Eventos do Pygame para o game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Atualizar posição da cobra
        x1 += x1_change
        y1 += y1_change

        # Desenhar a comida na tela
        screen.fill(WHITE)
        pygame.draw.rect(
            screen, RED, [foodx, foody, snake_block_size, snake_block_size]
        )

        # Atualizar a lista da
