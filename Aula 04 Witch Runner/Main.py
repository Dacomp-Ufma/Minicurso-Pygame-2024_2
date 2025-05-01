
from sys import exit
import os
import random
import pygame
from pygame.locals import *


diretorio = os.path.dirname(__file__)
diretorio_sec = os.path.join(diretorio, 'Sprites')
diretorio_terc = os.path.join(diretorio, 'Musicas')

pygame.init()


# Parametros da tela

largura = 1280
altura = 720
pos_x = largura / 4
pos_y = altura - 150


# Cores

preto = (0, 0, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)
amarelo = (255, 255, 0)


# Tela

screen = pygame.display.set_mode((largura, altura))
icone = pygame.image.load(os.path.join(diretorio_sec, 'B_witch.gif')).convert_alpha()
pygame.display.set_icon(icone)
pygame.display.set_caption('Runner witch')


# Caminho dos sprites

sprite_sheet = pygame.image.load(os.path.join(diretorio_sec, 'bruxa.png')).convert_alpha()
sprite_sheet2 = pygame.image.load(os.path.join(diretorio_sec, 'nuvens.png')).convert_alpha()
sprite_sheet3 = pygame.image.load(os.path.join(diretorio_sec, 'chao.png')).convert_alpha()
sprite_sheet4 = pygame.image.load(os.path.join(diretorio_sec, 'arbusto.png')).convert_alpha()
sprite_sheet5 = pygame.image.load(os.path.join(diretorio_sec, 'wingull.png')).convert_alpha()
sprite_sheet6 = pygame.image.load(os.path.join(diretorio_sec, 'latias.png')).convert_alpha()
sprite_sheet7 = pygame.image.load(os.path.join(diretorio_sec, 'goma.png')).convert_alpha()

fundo = pygame.image.load(os.path.join(diretorio_sec, 'forest.png')).convert_alpha()
fundo = pygame.transform.scale(fundo, (largura, altura))
fundo_init = pygame.image.load(os.path.join(diretorio_sec, 'fundo_init.png')).convert_alpha()
fundo_init = pygame.transform.scale(fundo_init, (largura, altura))
fundo_pausa = pygame.image.load(os.path.join(diretorio_sec, 'pausa.png')).convert_alpha()
fundo_pausa = pygame.transform.scale(fundo_pausa, (largura, altura))

botao_iniciar = pygame.image.load(os.path.join(diretorio_sec, 'iniciarbotao.png')).convert_alpha()
botao_iniciar = pygame.transform.scale(botao_iniciar, (93 * 9, 31 * 3))


# Sons e Músicas
pygame.mixer.music.set_volume(0.4)
msc_fundo = pygame.mixer.music.load(os.path.join(diretorio_terc, 'metre - kumaru.mp3'))  # Pode ser .mp3
pygame.mixer.music.play(-1) 
som_pontos = pygame.mixer.Sound(os.path.join(diretorio_terc, 'smw_save_menu.wav'))  # A cada x pontos toca
som_batida = pygame.mixer.Sound(os.path.join(diretorio_terc, 'smw_lost_a_life.wav'))  # Som de morte
som_pausa = pygame.mixer.Sound(os.path.join(diretorio_terc, 'smw_pause.wav'))
som_bonus = pygame.mixer.Sound(os.path.join(diretorio_terc, 'smw_1-up.wav'))


# Variáveis Gerais
batida = False  # Variavel que determina se houve colisao ou não
relogio = pygame.time.Clock()
pontos = 0
tempo = 0
velocidade = velocidade_chao = 10

pausar = False
menu = True


# Classes de objetos do jogo
class Bruxa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_terc, 'smw_jump.wav'))
        self.som_andar = pygame.mixer.Sound(os.path.join(diretorio_terc, 'smw_stomp.wav'))

        self.imagens_bruxa = []
        for i in range(8):
            img = sprite_sheet.subsurface((0, i * 48), (32, 48))
            img = pygame.transform.scale(img, (32 * 2, 48 * 2))
            self.imagens_bruxa.append(img)

        self.index_lista = 0
        self.image = self.imagens_bruxa[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)

        self.posicao_inicial = pos_y
        self.pulo = False
        self.andei = False

    def pular(self):
        if batida:
            pass
        else:
            self.pulo = True
            self.som_pulo.play()

    def andar(self):
        if batida:
            pass
        else:
            self.andei = True
            self.som_andar.play()

    def update(self):
        if batida:
            pass
        else:
            if self.pulo:
                if self.rect.y <= 350:
                    self.pulo = False
                self.rect.y -= 20
            else:
                if self.rect.y < self.posicao_inicial:
                    self.rect.y += 20
                else:
                    self.rect.y = self.posicao_inicial

            if self.andar:
                if pygame.key.get_pressed()[pygame.K_a]:
                    self.rect.x -= 5
                    if pygame.key.get_pressed()[pygame.K_d]:
                        pass
                elif pygame.key.get_pressed()[pygame.K_d]:
                    self.rect.x += 5
                    if pygame.key.get_pressed()[pygame.K_a]:
                        pass

            if self.index_lista > 7:
                self.index_lista = 0

            self.index_lista += 0.15
            self.image = self.imagens_bruxa[int(self.index_lista)]

            if self.rect.topright[0] < 0:
                self.rect.x = largura

class Nuvens(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet2.subsurface((0, 0), (32, 14))
        self.image = pygame.transform.scale(self.image, (32 * 3, 14 * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.rect.y = random.randrange(50, 200, 50)
        self.rect.x = largura - random.randrange(300, 700, 30)

    def update(self):
        if self.rect.topright[0] < 0:  # topright é uma tupla(x,y),então para manipular só o x
            self.rect.x = largura
            self.rect.y = random.randrange(50, 100, 10)
        self.rect.x -= velocidade // 4

class Chao(pygame.sprite.Sprite):
    def __init__(self, x_chao):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet3.subsurface((0, 0), (96, 32))
        self.image = pygame.transform.scale(self.image, (96, 32 * 4))
        self.rect = self.image.get_rect()
        self.rect.x = x_chao * 96
        self.rect.y = altura - 76

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= velocidade_chao

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet4.subsurface((0, 0), (18, 34))
        self.image = pygame.transform.scale(self.image, (18 * 4, 34 * 4))
        self.rect = self.image.get_rect()
        self.rect.center = (largura - 80, altura - 90)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= velocidade

class Wingull(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagem_wingull = []
        for i in range(4):
            img = sprite_sheet5.subsurface((i * 48, 0), (48, 60))
            # img = pygame.transform.scale(img, (88 * 3 / 4, 94 * 3 / 4))
            self.imagem_wingull.append(img)

        self.index_lista = 0
        self.image = self.imagem_wingull[self.index_lista]

        self.rect = self.image.get_rect()
        self.rect.center = (largura - 100, altura - 300)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= velocidade // 2

        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.15
        self.image = self.imagem_wingull[int(self.index_lista)]

class Latias(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagem_latias = []
        for i in range(2):
            img = sprite_sheet6.subsurface((i * 42, 0), (42, 33))
            # img = pygame.transform.scale(img, (88 * 3 / 4, 94 * 3 / 4))
            self.imagem_latias.append(img)

        self.index_lista = 0
        self.image = self.imagem_latias[self.index_lista]

        self.rect = self.image.get_rect()
        self.rect.center = (largura - 100, altura - 500)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= velocidade * 5

        if self.index_lista > 1:
            self.index_lista = 0
        self.index_lista += 0.1
        self.image = self.imagem_latias[int(self.index_lista)]

class Urso(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet7.subsurface((0, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.center = (largura - 200, altura - 200)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= velocidade


# Criando grupos de sprite 
todos_sprites = pygame.sprite.Group()
grupo_obstaculo = pygame.sprite.Group()
especial_sprites = pygame.sprite.Group()
bonus = pygame.sprite.Group()

# Adicionando os Sprites aos grupos
bruxa = Bruxa()
todos_sprites.add(bruxa)

pkm2 = Latias()
especial_sprites.add(pkm2)

goma = Urso()
bonus.add(goma)

for i in range(largura * 2 // 64):
    chao = Chao(i)
    todos_sprites.add(chao)

for i in range(4):
    nuvem = Nuvens()
    todos_sprites.add(nuvem)

for i in range(2):
    pkm = Wingull()
    todos_sprites.add(pkm)
    grupo_obstaculo.add(pkm)

for i in range(3):
    obst = Obstaculo()
    todos_sprites.add(obst)
    grupo_obstaculo.add(obst)


# Funções para ciclo do jogo
def Mensagem(mensagem, tamanho, cor):

    fonte = pygame.font.SysFont('arial', tamanho, True, False)
    msg = f'PONTOS:{mensagem}'

    if batida or menu or pausar:
        msg = f'{mensagem}'

    formatado = fonte.render(msg, False, cor)
    return formatado

def Reiniciar():
    global pontos, velocidade, batida
    pontos = 0
    velocidade = 10
    batida = False
    bruxa.pulo = False
    pkm.rect.x = largura - 100
    pkm.rect.y = altura - 300
    obst.rect.x = largura - 80
    bruxa.rect.y = pos_y
    bruxa.rect.x = pos_x

def pausa():

    global pausar
    pausar = True
    
    while pausar:

        relogio.tick(60)
        screen.fill(preto)
        screen.blit(fundo_pausa, (0, 0))
        screen.blit(botao_iniciar, (largura // 2 - 250, altura // 2 - 10))

        pausado = Mensagem('Aperte espaço para voltar', 60, amarelo)
        screen.blit(pausado, (largura // 2 - 200, altura // 2))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    pausar = False
                    screen.fill(preto)
                    jogo()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

def jogo():

    global tempo, pontos, velocidade, pontuacao, batida, pausar

    while True:

        relogio.tick(30)

        screen.fill(branco)
        screen.blit(fundo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_ESCAPE and batida:
                    pygame.quit()
                    exit()
                if evento.key == K_ESCAPE:
                    pausar = True
                    som_pausa.play()
                    pausa()
                if evento.key == K_SPACE or evento.key == K_w or evento.key == K_UP:
                    if bruxa.rect.y != bruxa.posicao_inicial:
                        pass
                    else:
                        bruxa.pular()
                if evento.key == K_a or evento.key == K_d:
                    bruxa.andar()

                if evento.key == K_r and batida:
                    Reiniciar()

        colisoes = pygame.sprite.spritecollide(bruxa, grupo_obstaculo, False, pygame.sprite.collide_mask)
        colisoes2 = pygame.sprite.spritecollide(bruxa, bonus, True, pygame.sprite.collide_mask)

        # objeto,grupo,true para sumir o grupo,flag de colisão(por pixel nesse caso)

        # screen.blit(img_fundo, (0, 0))  # insere o canto superio esquerdo da imagem no ponto(0,0)
        todos_sprites.draw(screen)

        if tempo < 20:
            tempo += 1
        else:
            pontos += 1
            tempo = 0

        if colisoes and batida == False:
            som_batida.play()
            batida = True

        if colisoes2:
            som_bonus.play()
            pontos += 5
            goma.rect.x = random.randrange(0,largura,10)
            goma.rect.y = random.randrange(270,altura-200,10)
            bonus.remove(goma)
            bonus.add(goma)

        if batida == True:
            screen.fill(preto)
            morte = Mensagem('FIM DE JOGO', 60, vermelho)
            screen.blit(morte, (largura // 2 - 200, altura // 2 - 100))
            reinicio = Mensagem('aperte R para reiniciar', 40, vermelho)
            screen.blit(reinicio, (largura // 2 - 200, altura // 2))
            fechar = Mensagem('Esc para sair', 20, vermelho)
            screen.blit(fechar, (largura // 2 - 200, altura // 2 + 100))
        else:
            todos_sprites.update()
            bonus.update()
            especial_sprites.update()
            pontuacao = Mensagem(pontos, 30, vermelho)

        if pontos % 20 == 0 and pontos != 0:
            som_pontos.play()
            if velocidade >= 15:
                velocidade += 0
            velocidade += 0.3

        for i in range(1, 100):
            if 40 * i <= pontos <= 55 * i:
                bonus.draw(screen)
            if 120 * i <= pontos <= 130 * i:
                especial_sprites.draw(screen)

        screen.blit(pontuacao, (1000, 80))

        pygame.display.update()


# Ciclo principal do jogo
while menu:

    relogio.tick(60)
    screen.fill(preto)
    screen.blit(fundo_init, (0, 0))
    screen.blit(botao_iniciar, (largura // 2 - 450, altura // 2 - 10))

    inicio = Mensagem('Aperte espaço para iniciar', 60, amarelo)
    screen.blit(inicio, (largura // 2 - 400, altura // 2))

    titulo = Mensagem('RUNNER WITCH', 110, amarelo)
    screen.blit(titulo, (largura // 2 - 450, altura // 2 - 200))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                menu = False
                screen.fill(preto)
                jogo()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
