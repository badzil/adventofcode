#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_next_digits_sum(digits):
    return sum(
        int(a)
        for a, b in zip(digits, digits[1:] + digits[0])
        if a == b
    )


def run_tests():
    assert get_next_digits_sum('1234') == 0
    assert get_next_digits_sum('1122') == 3
    assert get_next_digits_sum('1111') == 4
    assert get_next_digits_sum('91212129') == 9


if __name__ == '__main__':
    run_tests()
    digits = open('day_01_input.txt').read().strip()
    print(get_next_digits_sum(digits))
