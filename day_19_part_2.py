#!/usr/bin/env python3
# -*- coding: utf-8 -*-

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

def follow_path(path):
    path = [list(line) for line in path.split('\n')]
    x, y = path[0].index('|'), 0
    direction = DOWN

    while True:
        try:
            direction = move(path, x, y, direction)
        except Done:
            break
        x += direction[0]
        y += direction[1]


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Done(Exception):
    pass


def move(path, x, y, direction):
    c = path[y][x]
    new_direction = None
    if c in '|-':
        new_direction = direction
    elif c in LETTERS:
        new_direction = direction
        print(c)
    elif c == '+':
        if direction in (DOWN, UP):
            if path[y][x-1] != ' ':
                new_direction = LEFT
            elif path[y][x+1] != ' ':
                new_direction = RIGHT
        elif direction in (LEFT, RIGHT):
            if path[y-1][x] != ' ':
                new_direction = UP
            elif path[y+1][x] != ' ':
                new_direction = DOWN
    elif c == ' ':
        raise Done()
    else:
        raise Exception()

    return new_direction


def run_tests():
    path = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+"""
    follow_path(path)


if __name__ == '__main__':
    #run_tests()
    path = open('day_19_input.txt').read()
    follow_path(path)
