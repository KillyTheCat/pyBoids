import random
import pygame as pg
class Boid:
    def __init__(self, velX, velY, screenwidth, screenheight):
        self.radius = random.randint(5, 15)
        self.position = pg.math.Vector2(random.randrange(screenwidth), random.randrange(screenheight))
        self.velocity = pg.math.Vector2(0, 0)
        self.acceleration = pg.math.Vector2(0, 0)
        self.velocity.x, self.velocity.y = velX, velY
        self.maxForce = 0.010

    def wrap(self, x, y):
        if self.position.x > x:
            self.position.x = 0

        if self.position.x < 0:
            self.position.x = x

        if self.position.y > y:
            self.position.y = 0

        if self.position.y < 0:
            self.position.y = y

    def alignment(self, boids, radius):
        pos = []
        total = 0
        for boid in boids:
            if boid != self and self.position.distance_to(boid.position) < radius:
                pos.append(boid.velocity)
                total += 1

        sum = pg.math.Vector2(0, 0)
        for p in pos:
            sum += p

        if total != 0:
            sum = sum / total
            steerin = sum - self.velocity
            if(steerin.magnitude()!=0):
                steerin = steerin.normalize()*self.maxForce*1.6
                self.acceleration += steerin

    def cohesion(self, boids, radius):
        pos = pg.math.Vector2(0, 0)
        total = 0
        for boid in boids:
            if boid != self and self.position.distance_to(boid.position) < radius:
                pos += boid.position
                total += 1

        if total != 0:
            sum = pos / total
            steerin = sum - self.position
            if(steerin.magnitude()!=0):
                steerin = steerin.normalize()*self.maxForce*2
                self.acceleration += steerin

    def separation(self, boids, radius):
        pos = pg.math.Vector2(0, 0)
        total = 0
        for boid in boids:
            if boid != self and self.position.distance_to(boid.position) < radius and self.position.distance_to(boid.position)>0:
                diff = self.position - boid.position
                diff /= self.position.distance_to(boid.position)
                pos += diff
                total += 1

        if total != 0:
            sum = pos / total
            steerin = sum
            if(steerin.magnitude()!=0):
                steerin -= self.velocity
                steerin = steerin.normalize()*self.maxForce*2.5
                self.acceleration += steerin