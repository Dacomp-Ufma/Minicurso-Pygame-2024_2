import pygame
from sys import exit

# Iniciar os módulos da biblioteca
pygame.init()

# Criando a janela e uma variável pra limitar fps
tela = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

# Criando a tela de fundo
fundo = pygame.image.load("fundo\Preview\Background.png")
fundo = pygame.transform.smoothscale(fundo, (600,400))

# Criando um texto pra por na tela
fonte = pygame.font.Font(None, 50)
texto_surface = fonte.render('Joguinho', False, 'Red')
texto_rect = texto_surface.get_rect(center = (300,20))

# Criando o personagem
personagem_surface = pygame.image.load("pygameimagens\harrypotter.png")
personagem_surface = pygame.transform.scale(personagem_surface,(40,40))
personagem_rect = personagem_surface.get_rect(bottomleft = (0,365))

# Variáveis pra controlar aspectos do jogo
rodando = True
gravidade = 1.5
velocidade = 1.5
pulo = 70

# Loop principal do jogo
while rodando:
    # Verificar inputs e eventos
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()
    
    if keys[pygame.K_d]:
        personagem_rect.right += velocidade
    if (keys[pygame.K_SPACE] and (personagem_rect.bottom == 365)):
        personagem_rect.y -= pulo
    if keys[pygame.K_a]:
        personagem_rect.right -= velocidade
    
    # Gravidade do jogador
    personagem_rect.y += gravidade

    # Colocando os elementos na tela
    tela.blit(fundo,(0,0))
    tela.blit(texto_surface, texto_rect)
    tela.blit(personagem_surface, personagem_rect)
    
    # Delimitando o personagem na tela
    if (personagem_rect.right >= 600):
        personagem_rect.right = 600
    if (personagem_rect.bottom >= 365):
        personagem_rect.bottom = 365
    if (personagem_rect.left <= 0):
        personagem_rect.left = 0

    # Atualizar a tela e limitar fps
    pygame.display.update()
    clock.tick(60)