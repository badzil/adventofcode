#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from day_10_part_2 import knot_hash
from itertools import product


def hex_to_binary(digit):
    return bin(int(digit, 16))[2:].zfill(4)


def run_tests():
    assert hex_to_binary('0') == '0000'
    assert hex_to_binary('1') == '0001'
    assert hex_to_binary('e') == '1110'


def neighbors(i, j):
    yield (i - 1, j)
    yield (i, j - 1)
    yield (i + 1, j)
    yield (i, j + 1)


def build_region(grid, i, j, name):
    grid[i][j] = name
    for x, y in neighbors(i, j):
        try:
            if grid[x][y] == '1':
                build_region(grid, x, y, name)
        except IndexError:
            # Outside the grid.
            pass


if __name__ == '__main__':
    run_tests()

    grid = []
    s = 'stpzcrnm'
    for i in range(128):
        h = knot_hash(s + '-' + str(i))
        b = ''.join(hex_to_binary(d) for d in h)
        grid.append(list(b))
    
    region = 0
#   for i, j in product(range(128), range(128)):
    for i in range(128):
        for j in range(128):
            if grid[i][j] == '1':
                region += 1
                name = 'region %s' % region
                build_region(grid, i, j, name)

    print(region)
