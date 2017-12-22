#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import product
import time


def get_grid(pattern):
    return [list(line) for line in pattern.split('\n')]


def get_pattern(grid):
    return '\n'.join(''.join(line) for line in grid)


def flip(grid):
    return [line[::-1] for line in grid]


def rotate(grid):
    return list(zip(*grid[::-1]))


def patterns(grid):
    for g in [
        grid,
        rotate(grid),
        rotate(rotate(grid)),
        rotate(rotate(rotate(grid))),
    ]:
        yield get_pattern(g)
        yield get_pattern(flip(g))


def get_swaps(rules):
    swaps = {}
    for line in rules.split('\n'):
        i, o = line.split(' => ')
        grid_in = get_grid(i.replace('/', '\n'))
        grid_out = get_grid(o.replace('/', '\n'))
        for pattern in patterns(grid_in):
            swaps[pattern] = grid_out
    return swaps


def subsquares(grid, n):
    num_subsquares = len(grid) // n
    for x, y in product(range(num_subsquares), range(num_subsquares)):
        yield (x, y, [grid[y*n+i][x*n:(x+1)*n] for i in range(n)])


def insert_subsquare(grid, subsquare, x, y):
    size = len(subsquare)
    for i, line in enumerate(subsquare):
        grid[y*size+i][x*size:(x+1)*size] = line


def enhance(pattern, swaps):
    grid = get_grid(pattern)
    size = len(grid)
    if size % 2 == 0:
        new_size = size // 2 * 3
        new_grid = [['$'] * new_size for _ in range(new_size)]
        for x, y, subsquare in subsquares(grid, 2):
            swap = swaps[get_pattern(subsquare)]
            insert_subsquare(new_grid, swap, x, y)
    elif size % 3 == 0:
        new_size = size // 3 * 4
        new_grid = [['$'] * new_size for _ in range(new_size)]
        for x, y, subsquare in subsquares(grid, 3):
            swap = swaps[get_pattern(subsquare)]
            insert_subsquare(new_grid, swap, x, y)
    else:
        raise Exception("This should never happen")
    return get_pattern(new_grid)


def run_tests():
    pattern = """.#.
..#
###"""
    swaps = get_swaps("""../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""")
    pattern = enhance(pattern, swaps)
    assert pattern == """#..#
....
....
#..#"""
    pattern = enhance(pattern, swaps)
    assert pattern == """##.##.
#..#..
......
##.##.
#..#..
......"""


if __name__ == '__main__':
    run_tests()
    pattern = """.#.
..#
###"""
    swaps = get_swaps(open('day_21_input.txt').read().strip())
    for _ in range(5):
        pattern = enhance(pattern, swaps)
    print(pattern.count('#'))
