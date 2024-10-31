import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

pygame.init()

clock = pygame.time.Clock()
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

asteroids = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)

AsteroidField.containers = (updatable,)


def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	asteroid_field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20)
	
	while True:
		dt = clock.tick(60) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		for sprite in updatable:
			sprite.update(dt)
		screen.fill((0, 0, 0))
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()
		
		
if __name__ == "__main__":
	main()

