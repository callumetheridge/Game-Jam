import pygame

width = 1500
height = 750

pygame.init()

screen = pygame.display.set_mode((width, height));
pygame.display.set_caption("Lacku is a stinky boi")
clock = pygame.time.Clock()

tile_map = [
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Tile:
	def __init__(self, x_grid, y_grid, size):
		self.x_grid = x_grid
		self.y_grid = y_grid
		self.size = size
		self.rect = pygame.Rect(x_grid * size, y_grid * size, size, size)

	@staticmethod
	def get_offset(player_y) -> int:
		offset = 0
		offset_trigger = height / 4
		if player_y < offset_trigger:
			offset = (offset_trigger) - player_y

		return offset

	def draw_tile(self, player_y):
		offset = self.get_offset(player_y)
		pygame.draw.rect(screen, (0, 0, 255), (self.x_grid * self.size, self.y_grid * self.size + offset, self.size, self.size))

class Player:
	def __init__(self, x, y, size):
		self.x = x
		self.y = y
		self.x_velocity = 0
		self.y_velocity = 0
		self.mask = 1

		self.size = size
		self.gravity = 0.5
		self.in_air = True

		self.rect = pygame.Rect(self.x, self.y, size, size)

	def air_resistance(self):
		if self.x_velocity > 0.3:
			self.x_velocity -= 0.002 * self.x_velocity**2 + 0.005 * self.x_velocity + 0.02
		if self.x_velocity < -0.3:
			self.x_velocity += 0.002 * self.x_velocity**2 + 0.005 * abs(self.x_velocity) + 0.02
		if self.x_velocity < 0.3 and self.x_velocity > 0:
			self.x_velocity -= 0.01
		if self.x_velocity < 0 and self.x_velocity > -0.3:
			self.x_velocity += 0.01
		if self.x_velocity < 0.01 and self.x_velocity > -0.01:
			self.x_velocity = 0

	def handle_shooting(self, mask_coefficient):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		mouse_delta_x = mouse_x - self.x
		mouse_delta_y = mouse_y - self.y
		total_distance = abs(mouse_delta_x) + abs(mouse_delta_y)
		x_ratio = mouse_delta_x / total_distance
		y_ratio = mouse_delta_y / total_distance
		self.x_velocity = x_ratio * -1 * 20 * mask_coefficient
		self.y_velocity = y_ratio * -1 * 20 * mask_coefficient

	def move_left(self):
		if self.x_velocity > -5:
			self.x_velocity -= 0.15

	def move_right(self):
		if self.x_velocity < 5:
			self.x_velocity += 0.15

	# def handle_key_press(self, keys):
	# 	if keys[pygame.K_a] and not keys[pygame.K_d]:
	# 		self.x_velocity -= 5
	# 	if keys[pygame.K_d] and not keys[pygame.K_a]:
	# 		self.x_velocity += 5
	# 	if not keys[pygame.K_d] and not keys[pygame.K_a]:
	# 		self.x_velocity += 0
	# 	if keys[pygame.K_d] and keys[pygame.K_a]:
	# 		self.x_velocity += 0

	def cap_speed(self):
		if self.x_velocity > 25:
			self.x_velocity = 25
		if self.x_velocity < -25:
			self.x_velocity = -25

	def handle_movement(self, keys, shooting, left, right):
		if self.in_air:
			if self.y_velocity < -10:
				self.y_velocity += self.gravity * 1.5
			else:
				self.y_velocity += self.gravity
			self.y += self.y_velocity

		if self.y - self.size >= height:
			self.in_air = True
			self.y = height - self.size
			self.y_velocity = -15

		if left and not right:
			self.move_left()
		if right and not left:
			self.move_right()

		if self.mask == 1:
			mask_coefficient = 1.4
		else:
			mask_coefficient = 1

		'''self.handle_key_press(keys)'''
		self.cap_speed()
		if shooting:
			self.handle_shooting(mask_coefficient)

		if self.x + self.x_velocity < 0 or self.x + self.x_velocity > width:
			self.x_velocity *= -1

		self.x += self.x_velocity

		self.rect.topleft = (self.x, self.y)

	def draw_player(self, offset):
		pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y + offset, 20, 20))

def main():
	running = True
	shooting = False
	right = False
	left = False

	player = Player(500, 100, 20);

	tiles = []

	for y in range(len(tile_map) - 1, 0, -1):
		for x in range(len(tile_map[y])):
			if tile_map[y][x] == 1:
				tiles.append(Tile(x, y - 45, 75))

	while running:
		clock.tick(60)
		screen.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				shooting = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					left = True
				if event.key == pygame.K_d:
					right = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					left = False
				if event.key == pygame.K_d:
					right = False
		
		offset = Tile.get_offset(player.y)
		keys = pygame.key.get_pressed()

		player.handle_movement(keys, shooting, left, right)
		
		for tile in tiles:
			tile.draw_tile(player.y)

			if pygame.Rect.colliderect(player.rect, tile.rect):
				print("Collision detected!")

		player.draw_player(offset)

		if player.in_air == True:
			player.air_resistance()

		shooting = False

		pygame.display.update()

main()
