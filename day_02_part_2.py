#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import product


def intify(spreadsheet):
    """Generates an int version of a str spreadsheet.
    """
    for row in spreadsheet.split('\n'):
        yield [int(n) for n in row.split()]


def get_checksum(spreadsheet):
    checksum = 0
    for numbers in intify(spreadsheet):
        for a, b in product(numbers, numbers):
            if a < b and b % a == 0:
                checksum += b // a
                break
    return checksum


def run_tests():
    assert get_checksum(
        """5 9 2 8
        9 4 7 3
        3 8 6 5"""
    ) == 9


if __name__ == '__main__':
    run_tests()
    digits = open('day_02_input.txt').read().strip()
    print(get_checksum(digits))
