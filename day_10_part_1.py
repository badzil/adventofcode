#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def tie_knot(numbers, length, position):
    section = (numbers + numbers)[position:position+length]
    for idx, number in enumerate(reversed(section)):
        numbers[(position + idx) % len(numbers)] = number


def tie_knots(numbers, lengths):
    position = 0
    for skip_size, length in enumerate(lengths):
        tie_knot(numbers, length, position)
        position = (position + length + skip_size) % len(numbers)


def run_tests():
    numbers = [0, 1, 2, 3, 4]
    tie_knot(numbers, length=3, position=0)
    assert numbers == [2, 1, 0, 3, 4]
    tie_knot(numbers, length=4, position=3)
    assert numbers == [4, 3, 0, 1, 2]
    tie_knot(numbers, length=1, position=3)
    assert numbers == [4, 3, 0, 1, 2]

    numbers = [0, 1, 2, 3, 4]
    tie_knots(numbers, [3, 4, 1, 5])
    assert numbers == [3, 4, 2, 1, 0]


if __name__ == '__main__':
    run_tests()
    numbers = list(range(256))
    lengths = [int(l) for l in open('day_10_input.txt').read().split(',')]
    tie_knots(numbers, lengths)
    print(numbers[0] * numbers[1])
