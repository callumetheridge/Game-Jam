import pygame
import sys

width = 1000
height = 500

pygame.init()
screen = pygame.display.set_mode((width, height));
clock = pygame.time.Clock()

class Player:
	def __init__(self, x, y, size):
		self.x = x
		self.y = y
		self.x_velocity = 0
		self.y_velocity = 0

		self.move_left = False
		self.move_right = False

		self.size = size
		self.gravity = 0.5
		self.in_air = True

	def handle_shooting(self, shooting):
		if not shooting:
			return
		
		mouse_x, mouse_y = pygame.mouse.get_pos()
		mouse_delta_x = mouse_x - self.x
		mouse_delta_y = mouse_y - self.y
		total_distance = abs(mouse_delta_x) + abs(mouse_delta_y)
		x_ratio = mouse_delta_x / total_distance
		y_ratio = mouse_delta_y / total_distance
		self.x_velocity = x_ratio * -1 * 20
		self.y_velocity = y_ratio * -1 * 20

	def handle_key_press(self, keys):
		if keys[pygame.K_a] and not keys[pygame.K_d]:
			self.x_velocity -= 5
		if keys[pygame.K_d] and not keys[pygame.K_a]:
			self.x_velocity += 5
		if not keys[pygame.K_d] and not keys[pygame.K_a]:
			self.x_velocity += 0
		if keys[pygame.K_d] and keys[pygame.K_a]:
			self.x_velocity += 0

	def handle_movement(self, keys, shooting):
		if self.in_air:
			self.y_velocity += self.gravity
			self.y += self.y_velocity

		if self.y >= height:
			self.in_air = True
			self.y = height - self.size
			self.y_velocity = -20

		self.handle_shooting(shooting) 

		if self.x + self.x_velocity < 0 or self.x + self.x_velocity > width:
			self.x_velocity *= -1

		self.x += self.x_velocity

	def draw_player(self):
		pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 20, 20))

def main():
	running = True
	shooting = False

	player = Player(500, 100, 20);

	while running:
		clock.tick(60)
		screen.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				shooting = True

		keys = pygame.key.get_pressed()
		player.handle_movement(keys, shooting)
		player.draw_player()
		pygame.display.update()

		shooting = False

main()
