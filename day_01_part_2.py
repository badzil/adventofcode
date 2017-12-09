#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_next_digits_sum(digits):
    middle = len(digits) // 2
    return sum(
        int(a)
        for a, b in zip(digits, digits[middle:] + digits[:middle])
        if a == b
    )


def run_tests():
    assert get_next_digits_sum('1212') == 6
    assert get_next_digits_sum('1221') == 0
    assert get_next_digits_sum('123425') == 4
    assert get_next_digits_sum('123123') == 12
    assert get_next_digits_sum('12131415') == 4


if __name__ == '__main__':
    run_tests()
    digits = open('day_01_input.txt').read().strip()
    print(get_next_digits_sum(digits))
