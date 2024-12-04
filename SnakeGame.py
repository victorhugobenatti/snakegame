import pygame
import time
import random

velocidade_cobrinha = 15

# Tamanho da janela
janela_x = 720
janela_y = 480

# definindo as cores
preto = pygame.Color(0, 0, 0)
branco = pygame.Color(255, 255, 255)
vermelho = pygame.Color(255, 0, 0)
verde = pygame.Color(0, 255, 0)
azul = pygame.Color(0, 0, 255)

# iniciando pygame
pygame.init()

# Iniciando a janela do jogo
pygame.display.set_caption('Trabalho Final LPP - Snake Game')
janela_do_jogo = pygame.display.set_mode((janela_x, janela_y))

# Controlando o FPS
fps = pygame.time.Clock()

# Definindo a posição inicial da cobrinha
posicao_da_cobrinha = [100, 50]

# Definindo os primeiros 4 blocos da cobrinha
corpo_da_cobrinha = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# Posição inicial da fruta
posicao_da_fruta = [random.randrange(1, (janela_x//10)) * 10, 
                  random.randrange(1, (janela_y//10)) * 10]

spawn_fruta = True

# Direção inicial da cobrinha
# Direção = RIGHT
direcao = 'RIGHT'
mudar_para = direcao

# Pontuação inicial
score = 0

# Função para mostrar a pontuação
def mostra_score(cor, fonte, tamanho):

    # criando o objeto de fonte
    score_fonte = pygame.font.SysFont(fonte, tamanho)

    # cria um objeto da superfície do texto
    score_superficie = score_fonte.render('Score : ' + str(score), True, cor)

    # cria um objeto retangular para o texto
    score_retangulo = score_superficie.get_rect()

    # Mostre a pontuação na parte superior
    janela_do_jogo.blit(score_superficie, score_retangulo)

#  Função para mostrar a mensagem de Game Over
def game_over():

    # criando um objeto de fonte
    fonte = pygame.font.SysFont('times new roman', 50)

    game_over_superficie = fonte.render(
        'Seu Score é : ' + str(score), True, vermelho)

    # Cria um objeto retangular para o texto
    game_over_retangulo = game_over_superficie.get_rect()

    # Setando a posição do texto
    game_over_retangulo.midtop = (janela_x/2, janela_y/4)

    # Desenhando o texto na tela
    janela_do_jogo.blit(game_over_superficie, game_over_retangulo)
    pygame.display.flip()

    # Depois de 2 segundos, o jogo será encerrado
    time.sleep(2)

    # Desligando o pygame
    pygame.quit()
    
    # Sai do programa
    quit()


# Loop principal
while True:
    
    # Manipulando eventos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mudar_para = 'UP'
            if event.key == pygame.K_DOWN:
                mudar_para = 'DOWN'
            if event.key == pygame.K_LEFT:
                mudar_para = 'LEFT'
            if event.key == pygame.K_RIGHT:
                mudar_para = 'RIGHT'

    # Mudando a direção da cobrinha
    if mudar_para == 'UP' and direcao != 'DOWN':
        direcao = 'UP'
    if mudar_para == 'DOWN' and direcao != 'UP':
        direcao = 'DOWN'
    if mudar_para == 'LEFT' and direcao != 'RIGHT':
        direcao = 'LEFT'
    if mudar_para == 'RIGHT' and direcao != 'LEFT':
        direcao = 'RIGHT'

    # Movendo a cobrinha
    if direcao == 'UP':
        posicao_da_cobrinha[1] -= 10
    if direcao == 'DOWN':
        posicao_da_cobrinha[1] += 10
    if direcao == 'LEFT':
        posicao_da_cobrinha[0] -= 10
    if direcao == 'RIGHT':
        posicao_da_cobrinha[0] += 10

    # Mecanismo de crescimento da cobrinha
    # A cada vez que a cobrinha come a fruta, o score aumenta em 10
    corpo_da_cobrinha.insert(0, list(posicao_da_cobrinha))
    if posicao_da_cobrinha[0] == posicao_da_fruta[0] and posicao_da_cobrinha[1] == posicao_da_fruta[1]:
        score += 10
        spawn_fruta = False
    else:
        corpo_da_cobrinha.pop()
        
    if not spawn_fruta:
        posicao_da_fruta = [random.randrange(1, (janela_x//10)) * 10, 
                          random.randrange(1, (janela_y//10)) * 10]
        
    spawn_fruta = True
    janela_do_jogo.fill(preto)
    
    for pos in corpo_da_cobrinha:
        pygame.draw.rect(janela_do_jogo, verde,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(janela_do_jogo, branco, pygame.Rect(
        posicao_da_fruta[0], posicao_da_fruta[1], 10, 10))

    # Condicionais para o fim do jogo
    if posicao_da_cobrinha[0] < 0 or posicao_da_cobrinha[0] > janela_x-10:
        game_over()
    if posicao_da_cobrinha[1] < 0 or posicao_da_cobrinha[1] > janela_y-10:
        game_over()

    # Tocando o corpo da cobrinha
    for block in corpo_da_cobrinha[1:]:
        if posicao_da_cobrinha[0] == block[0] and posicao_da_cobrinha[1] == block[1]:
            game_over()

    # Mostrando a pontuação
    mostra_score(branco, 'times new roman', 20)

    # Atualizando a janela
    pygame.display.update()

    # FPS/Taxa de atualização
    fps.tick(velocidade_cobrinha)