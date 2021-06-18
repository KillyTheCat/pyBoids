import random

import pygame
import pygame as pg
from boid import Boid




pg.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False
bCohesion = True

x, y = 100, 100

boids = []

for _ in range(40):
    boids.append(Boid(velX=random.randint(-5, 5)*0.01, velY=random.randint(-5, 5)*0.01, screenwidth=SCREEN_WIDTH, screenheight=SCREEN_HEIGHT))

while not done:
    for event in pg.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pg.KEYDOWN:
            if event.key == pygame.K_1:
                bCohesion = not bCohesion
    pygame.display.update()
    screen.fill((0, 0, 0))

    for boid in boids:

        pygame.draw.circle(screen, (255, 255, 255), boid.position, boid.radius, width=int(boid.radius/2))
        boid.position += boid.velocity
        boid.velocity += boid.acceleration
        boid.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
        if boid.velocity.magnitude() > 0 and boid.velocity.magnitude()<0.2 :
            boid.velocity = boid.velocity.normalize()*0.2
        if bCohesion:
            boid.acceleration *= 0
            boid.alignment(boids, 30)
            boid.cohesion(boids, 30)
            boid.separation(boids, 30)
