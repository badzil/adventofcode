#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def generate(factor, start):
    return (start * factor) % 2147483647


FACTOR_A = 16807
FACTOR_B = 48271

def get_count(a, b, n):
    c = 0
    for i in range(n):
        a, b = generate(FACTOR_A, a), generate(FACTOR_B, b)
        if bin(a)[-16:] == bin(b)[-16:]:
            c += 1
        if i % 100000 == 0:
            print(i, c)
    return c


def run_tests():
    assert get_count(65, 8921, 1) == 0
    assert get_count(65, 8921, 2) == 0
    assert get_count(65, 8921, 3) == 1
    assert get_count(65, 8921, 4) == 1
    assert get_count(65, 8921, 5) == 1


if __name__ == '__main__':
    run_tests()
    print(get_count(618, 814, 40*10**6))
