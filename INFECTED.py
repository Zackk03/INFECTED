import pygame, random, os

from pygame.constants import MOUSEBUTTONDOWN

pygame.mixer.init()
pygame.font.init()

BLACK = (0, 0, 0)
GBB_ANCHO, GBB_ALTO = 30,30
CORONAVIRUS_ANCHO, CORONAVIRUS_ALTO = 50,50
GBR_ANCHO, GBR_ALTO = 30,30
FONDO_W, FONDO_H = 400,600
TITULO_WIDTH, TITULO_HEIGHT = 800,100
LASER_ANCHO, LANSER_ALTO = 10, 15
BOTON_WIDTH, BOTON_HEIGHT = 200,75

FONDO = pygame.transform.scale(
             pygame.image.load(os.path.join("assets", "fondo.png")), (FONDO_W, FONDO_H))
MENU = pygame.transform.scale(
             pygame.image.load(os.path.join("assets", "menu.png")), (FONDO_W, FONDO_H))
TITULO = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "titulo.png")), (TITULO_WIDTH, TITULO_HEIGHT))
BOTON = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "boton.png")), (BOTON_WIDTH, BOTON_HEIGHT))
GBB_HIT = pygame.USEREVENT + 1
CORONAVIRUS_VIDA = 10
nivel = 0
HEALTH_FONT = pygame.font.SysFont("Arial Black", 30)

pium = pygame.mixer.Sound("assets/pium.wav")
gameover = pygame.mixer.Sound("assets/gameover.wav")
click = pygame.mixer.Sound("assets/click.wav")
winning = pygame.mixer.Sound("assets/winning.wav")

pygame.display.set_caption("INFECTED")

class gbr(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "gbr.png")), (GBR_ANCHO, GBR_ALTO))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	
	def update(self):
		self.rect.y += 1
		if self.rect.y > 500:
			self.rect.y = -10
			self.rect.x = random.randrange(350) 

class gbb(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "globulo_blanco.png")), (GBB_ANCHO, GBB_ALTO))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
    
	def update(self):
		self.rect.y += 1
		if self.rect.y > 600:
			self.rect.y = -10
			self.rect.x = random.randrange(350)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "coronavirus.png")), (CORONAVIRUS_ANCHO, CORONAVIRUS_ALTO))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.speed_y = 0

	def changespeed(self, x):
		self.speed_x += x

	def update(self):
		self.rect.x += self.speed_x
		player.rect.y = 550

class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "laser.png")), (LASER_ANCHO, LANSER_ALTO))
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 4

def texto_pantalla(CORONAVIRUS_VIDA, score, nivel):
	vida_texto = HEALTH_FONT.render("Salud: " + str(CORONAVIRUS_VIDA), 1, [255,255,255])
	puntaje = HEALTH_FONT.render("Score: " + str(score), 1, [255,255,255])
	#screen.blit(vida_texto, (SCREEN_WIDTH - vida_texto.get_width() - 10, 10))
	screen.blit(vida_texto, (5, 5))
	screen.blit(puntaje, (5, 40))

def colicion(gbb_hit_list, CORONAVIRUS_VIDA, GBB_HIT):
	for gbb in gbb_hit_list:
		CORONAVIRUS_VIDA -= 1
		pygame.event.post(pygame.event.Event(GBB_HIT))

def draw_failed(text):
    draw_text = HEALTH_FONT.render(text, 1, [255,255,255])
    screen.blit(draw_text, (SCREEN_WIDTH/2 - draw_text.get_width() / 2, SCREEN_HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def draw_winning(text):
    draw_text = HEALTH_FONT.render(text, 1, [255,255,255])
    screen.blit(draw_text, (SCREEN_WIDTH/2 - draw_text.get_width() / 2, SCREEN_HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def draw_level(text):
    draw_text = HEALTH_FONT.render(text, 1, [255,255,255])
    screen.blit(draw_text, (10,80))
    pygame.display.update()

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
run = False
score = 0
FPS = 60

gbr_list = pygame.sprite.Group()
gbb_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

for i in range(20):
	globulo_b = gbb()
	globulo_b.rect.x = random.randrange(FONDO_W - 20)
	globulo_b.rect.y = random.randrange(600)
	gbb_list.add(globulo_b)
	all_sprite_list.add(globulo_b)

for i in range(50):
    globulo_r = gbr()
    globulo_r.rect.x = random.randrange(FONDO_W - 20)
    globulo_r.rect.y = random.randrange(600)
    gbr_list.add(globulo_r)        
    all_sprite_list.add(globulo_r)

tiempo = pygame.time.Clock()
ejecucion = True
player = Player()
all_sprite_list.add(player)
segs = 1
menu = True
run = True

while menu:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
	screen.blit(MENU, (0,0))
	#screen.blit(TITULO, ((SCREEN_WIDTH//2)-(TITULO.get_width()//2), 10))
	screen.blit(BOTON, (100, 300))
	#print(screen.get_width, screen.get_height)
	mouse = pygame.mouse.get_pos()
	if 100+200 > mouse[0] > 100 and 300+75 > mouse[1] > 300:
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				click.play()
				menu = False
				run = True
	pygame.display.update()

while run:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.changespeed(-3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(3)
			if event.key == pygame.K_SPACE:
				laser = Laser()
				laser.rect.x = player.rect.x + 30
				laser.rect.y = player.rect.y - 20
				pium.play()

				laser_list.add(laser)
				all_sprite_list.add(laser)

		if event.type == GBB_HIT:		
			CORONAVIRUS_VIDA -= 1
			#pygame.event.post(pygame.event.Event(GBB_HIT))


		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.changespeed(3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(-3)


	all_sprite_list.update() 
	gbb_hit_list = pygame.sprite.spritecollide(player, gbb_list, True)
	for laser in laser_list:
		meteor_hit_list = pygame.sprite.spritecollide(laser, gbr_list, True)	
		for meteor in meteor_hit_list:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)
			score += 1
		if laser.rect.y < -10:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)

	level = 0
	if round(segs) <= 29:
		globulo_b.rect.y += 5
		level = 1
	elif round(segs) <= 59:
		globulo_b.rect.y += 100
		level = 2
	elif round(segs) <= 89:
		globulo_b.rect.y += 15
		level = 3
	elif round(segs) <= 119:
		globulo_b.rect.y += 20
		level = 4
	elif round(segs) <= 149:
		globulo_b.rect.y += 22
		level = 5
	elif round(segs) >= 179:
		globulo_b.rect.y += 30
		level = 6

	screen.blit(FONDO, [0, 0])
	gamer_over = ""
	text = ""
	if CORONAVIRUS_VIDA <= 0:
		gamer_over = "GAME OVER"
	if score == 70:
		text = "HUMANO INFECTADO"
	if text != "":
		winning.play()
		draw_winning(text)
		run = False
		menu = True
	if gamer_over != "":
		gameover.play()
		draw_failed(gamer_over)
		run = False
		menu = True

	all_sprite_list.draw(screen)
	texto_pantalla(CORONAVIRUS_VIDA, score, nivel)
	colicion(gbb_hit_list, CORONAVIRUS_VIDA, GBB_HIT)
	draw_level(f"Nivel: {level}")
	pygame.display.flip()
	segs += 1/60

pygame.quit()