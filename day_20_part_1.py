#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations


class Particle(object):

    def __init__(self, x, y, z, vx, vy, vz, ax, ay, az):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.ax = ax
        self.ay = ay
        self.az = az

    @staticmethod
    def from_str(particle_str):
        pos = particle_str.split('p=<', 1)[1]
        pos, speed = pos.split('>, v=<', 1)
        speed, acc = speed.split('>, a=<', 1)
        acc = acc.strip('>')
        return Particle(
            *(int(x) for x in pos.split(',')),
            *(int(x) for x in speed.split(',')),
            *(int(x) for x in acc.split(',')),
        )

    def get_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
    
    def move(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def collide(self, particle):
        return self.x == particle.x and \
            self.y == particle.y and \
            self.z == particle.z


def get_closest_particle(input_str):
    particles = [Particle.from_str(particle)
                 for particle in input_str.split('\n')]
    distances = [p.get_distance() for p in particles]
    for i in range(1000):
        [p.move() for p in particles]
        remove = set()
        for p1, p2 in combinations(particles, 2):
            if p1.collide(p2):
                remove.add(p1)
                remove.add(p2)
        for p in remove:
            particles.remove(p)
        print(len(particles))
            

def run_tests():
    particles = """p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"""
    get_closest_particle(particles)


if __name__ == '__main__':
    run_tests()
    particles = open('day_20_input.txt').read().strip()
    print(get_closest_particle(particles))
