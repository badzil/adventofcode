#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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


def dance(num_programs, moves):
    programs = [chr(x) for x in range(97, 97 + num_programs)]
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
    return ''.join(programs)


def run_tests():
    assert spin(list('abcde'), 1) == list('eabcd')
    assert exchange(list('eabcd'), 3, 4) == list('eabdc')
    assert partner(list('eabdc'), 'e', 'b') == list('baedc')

    assert dance(5, 's1,x3/4,pe/b') == 'baedc'


if __name__ == '__main__':
    run_tests()
    moves = open('day_16_input.txt').read().strip()
    print(dance(16, moves))
