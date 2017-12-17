#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


def spin(programs, x):
    return programs[-x:] + programs[:-x]


def exchange(programs, a, b):
    new_a = programs[b]
    programs[b] = programs[a]
    programs[a] = new_a
    return programs


def partner(programs, a, b):
    a_idx = programs.index(a)
    b_idx = programs.index(b)
    return exchange(programs, a_idx, b_idx)


def dance(programs, moves):
    for move in moves.split(','):
        if move[0] == 's':
            programs = spin(programs, int(move[1:]))
        elif move[0] == 'x':
            a, b = move[1:].split('/')
            programs = exchange(programs, int(a), int(b))
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            programs = partner(programs, a, b)
        else:
            raise Exception('Unknown dance move: ' + move)
    return programs


def run_tests():
    assert spin(list('abcde'), 1) == list('eabcd')
    assert exchange(list('eabcd'), 3, 4) == list('eabdc')
    assert partner(list('eabdc'), 'e', 'b') == list('baedc')

    assert dance(list('abcde'), 's1,x3/4,pe/b') == list('baedc')


if __name__ == '__main__':
    run_tests()
    moves = open('day_16_input.txt').read().strip()
    start_programs = [chr(c) for c in range(97, 97 + 16)]
    programs = start_programs[::]
    for i in itertools.count():
        programs = dance(programs, moves)
        print(i+1, ''.join(programs))
        if programs == start_programs:
            print(i)
            break
