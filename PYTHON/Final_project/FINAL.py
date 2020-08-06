import pygame

SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE_COLOR = (255, 255, 255) 
BLACK_COLOR = (0, 0, 0)
PURPLE_COLOR = (162, 0, 255)
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont('comicsans', 60)

class PlayerCharacter:
	SPEED = 10
	def __init__(self, _path, x, y, width, height):
		object_image = pygame.image.load(_path)
		# init atributes
		self.image = pygame.transform.scale(object_image, (width, height))	
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	def move(self, direction, max_height): 
		if direction > 0:
			self.y -= self.SPEED
		elif direction < 0:
			self.y += self.SPEED
		if self.y >= max_height - 40:
			self.y = max_height - 40 			
	def detect_collition(self, other_body):
		if self.y > other_body.y + other_body.height:
			return False
		elif self.y + self.height < other_body.y:
			return False
		if self.x > other_body.x + other_body.width:
			return False
		elif self.x + self.width < other_body.x:
			return False
		return True						
	def drawA(self, background):
			background.blit(self.image, (self.x, self.y))

class Enemy1:
	SPEED = 10
	def __init__(self, image_path, x, y, width, height):
		object_image = pygame.image.load(image_path)
		self.image = pygame.transform.scale(object_image, (width, height))	
		self.x = x
		self.y = y
		self.width = width
		self.height = height		
	def move(self, max_width):  
		if self.x <= 20:
			self.SPEED = abs(self.SPEED)
		elif self.x >= max_width - 70:
			self.SPEED = -abs(self.SPEED)
		self.x += self.SPEED		
	def draw2(self, background):
			background.blit(self.image, (self.x, self.y))			
class GameObject:
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))  
        self.x = x
        self.y = y
        self.width = width
        self.height = height      
    def draw(self, background):
        background.blit(self.image, (self.x, self.y))
        
class Game:
	TICK_RATE = 60
	IS_GO = False
	direction = 0	
	WIN = False  	
	def __init__(self, image_path, title, width, height):
		self.title = title
		self.width = width
		self.height = height
		self.game_screen = pygame.display.set_mode((width, height))
		self.game_screen.fill(WHITE_COLOR)
		pygame.display.set_caption(title)
		background_image = pygame.image.load(image_path)
		self.image = pygame.transform.scale(background_image, (width, height))		
	def run_game_loop(self, level_speed):
		#declaring objects, player enemies and treasure chest
		player_image = PlayerCharacter("player.png", 375, 650, 50, 50)
		
		enemy_0 = Enemy1("enemy.png", 20, 500, 50, 50)
		enemy_0.SPEED*= level_speed

		enemy_1 = Enemy1("enemy.png", self.width - 20, 375, 50, 50)
		enemy_1.SPEED*= level_speed 

		enemy_2 = Enemy1("enemy.png", 75, 145, 100, 100)
		enemy_2.SPEED*= level_speed + 0.8
		
		enemy_3 = Enemy1("GHOST.png", self.width - 75, 145, 100, 100)
		enemy_3.SPEED = 23
		
		enemy_4 = Enemy1("GHOST.png", self.width - 75, 435, 25, 25)
		enemy_4.SPEED = 30		

		treasure = GameObject("treasure.png", 375, 50, 50, 50)
		
################### MOVEMENT CONDITION ##########################################################
		while not self.IS_GO:
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					self.IS_GO = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.direction = 1
					elif event.key == pygame.K_DOWN:
						self.direction = -1
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						self.direction = 0
########### FOR LOOP CONTINUES ##################################################################		
			print(Enemy1.SPEED)	

			self.game_screen.blit(self.image,(0, 0))

			treasure.draw(self.game_screen)		

			player_image.move(self.direction, self.height)	
			player_image.drawA(self.game_screen)		
			
			enemy_0.move(self.width) 
			enemy_0.draw2(self.game_screen)
			

			
			if level_speed > 1:
				enemy_1.move(self.width)
				enemy_1.draw2(self.game_screen)
			if level_speed > 1.5:
				enemy_2.move(self.width)
				enemy_2.draw2(self.game_screen)
				enemy_3.move(self.width)
				enemy_3.draw2(self.game_screen)
				enemy_4.move(self.width)
				enemy_4.draw2(self.game_screen)
				#BEATING THE GAME CONDITION			
			if enemy_1.SPEED == 25.0 or enemy_1.SPEED == -25.0:
				self.IS_GO = True
				text = font.render('U THE BEST...AROUND!!', True, PURPLE_COLOR)
				self.game_screen.blit(text,(129, 350))
				text = font.render("U WIN, TNX 4 PLAYIN MY LAME GAME :'(", True, PURPLE_COLOR)
				self.game_screen.blit(text,(10, 450))
				text = font.render("The game will close automatically", True, PURPLE_COLOR)
				self.game_screen.blit(text,(75, 550))
				pygame.display.update()
				clock.tick(1)
				clock.tick(1)
				clock.tick(1)
				clock.tick(1)
				clock.tick(1)
				clock.tick(1)
				clock.tick(1)
				break

			if player_image.detect_collition(enemy_0): 
				self.IS_GO = True
				self.WIN = False			
				text = font.render('U GET NOTHIN U LOOSE >:v', True, PURPLE_COLOR)
				self.game_screen.blit(text,(129, 350))
				pygame.display.update()
				clock.tick(1)
				break
			if player_image.detect_collition(enemy_1): 
				self.IS_GO = True
				self.WIN = False				
				text = font.render('U GET NOTHIN U LOOSE >:v', True, PURPLE_COLOR)
				self.game_screen.blit(text,(129, 350))
				pygame.display.update()
				clock.tick(1)
				break
			if player_image.detect_collition(enemy_2): 
				self.IS_GO = True
				self.WIN = False				
				text = font.render("OOF! :'v", True, PURPLE_COLOR)
				self.game_screen.blit(text,(349, 350))
				pygame.display.update()
				clock.tick(1)
				break
				#WIN becomes true when grabing the chest. not a tecnical win. but a clear
			elif player_image.detect_collition(treasure):
				self.IS_GO = True		
				self.WIN = True	
				text = font.render('OK?!', True, PURPLE_COLOR)
				self.game_screen.blit(text,(349, 350))
				pygame.display.update()
				clock.tick(1)
				break
			pygame.display.update()
			clock.tick(self.TICK_RATE)
		#		
		if self.WIN:
			new_game = Game("background.png", SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
			new_game.run_game_loop(level_speed + 0.5) #CALLING THE VARIABLE + ADDING 0.5 OF SPEED VALUES
		else:
			return
pygame.init()			
new_game = Game("background.png", SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)
pygame.quit()
quit()