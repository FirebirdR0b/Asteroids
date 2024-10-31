import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

pygame.init()

clock = pygame.time.Clock()
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

asteroids = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)

AsteroidField.containers = (updatable,)

shots = pygame.sprite.Group()
Shot.containers = (shots, updatable, drawable)



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

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			new_shot = player.shoot()
			if new_shot is not None:
				shots.add(new_shot)

		for sprite in updatable:
			sprite.update(dt)

		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game over!")
				sys.exit()

		screen.fill((0, 0, 0))

		for sprite in drawable:
			sprite.draw(screen)

		pygame.display.flip()

		for asteroid in asteroids:
			asteroid.update(dt)
		for asteroid in asteroids:
			asteroid.draw(screen)

		for asteroid in asteroids:
			for shot in shots:
				if shot.collides_with(asteroid):
					asteroid.split()
					shot.kill()
		
if __name__ == "__main__":
	main()

