#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import islice


def tie_knot(numbers, length, position):
    section = (numbers + numbers)[position:position+length]
    for idx, number in enumerate(reversed(section)):
        numbers[(position + idx) % len(numbers)] = number


def tie_knots(numbers, lengths):
    position = 0
    for skip_size, length in enumerate(lengths * 64):
        tie_knot(numbers, length, position)
        position = (position + length + skip_size) % len(numbers)


def xor(l):
    res = 0
    for n in l:
        res ^= n
    return res


def knot_hash(s):
    numbers = list(range(256))
    lengths = [ord(b) for b in s] + [17, 31, 73, 47, 23]
    tie_knots(numbers, lengths)
    dense_hash = [xor(islice(numbers, idx * 16, (idx + 1) * 16))
                  for idx in range(16)]
    return ''.join(hex(n)[2:].zfill(2) for n in dense_hash)


def run_tests():
    numbers = [0, 1, 2, 3, 4]
    tie_knot(numbers, length=3, position=0)
    assert numbers == [2, 1, 0, 3, 4]
    tie_knot(numbers, length=4, position=3)
    assert numbers == [4, 3, 0, 1, 2]
    tie_knot(numbers, length=1, position=3)
    assert numbers == [4, 3, 0, 1, 2]

    assert xor([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == 64

    assert knot_hash('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert knot_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert knot_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert knot_hash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'


if __name__ == '__main__':
    run_tests()
    s = open('day_10_input.txt').read().strip()
    print(knot_hash(s))
