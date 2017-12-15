#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def generate(factor, start, divider):
    while True:
        start = (start * factor) % 2147483647
        if start % divider == 0:
            yield start


FACTOR_A = 16807
FACTOR_B = 48271


def get_count(a, b, n):
    c = 0

    generator_a = generate(FACTOR_A, a, 4)
    generator_b = generate(FACTOR_B, b, 8)

    for i in range(n):
        a, b = generator_a.next(), generator_b.next()
        if bin(a)[-16:] == bin(b)[-16:]:
            c += 1
        if i % 100000 == 0:
            print(i, c)
    return c


def run_tests():
    assert get_count(65, 8921, 1) == 0
    assert get_count(65, 8921, 2) == 0
    assert get_count(65, 8921, 3) == 0
    assert get_count(65, 8921, 4) == 0
    assert get_count(65, 8921, 5) == 0
    assert get_count(65, 8921, 1056) == 1


if __name__ == '__main__':
    run_tests()
    print(get_count(618, 814, 5*10**6))
