#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_checksum(spreadsheet):
    checksum = 0
    for row in spreadsheet.split('\n'):
        numbers = [int(n) for n in row.split()]
        checksum += max(numbers) - min(numbers)
    return checksum


def run_tests():
    assert get_checksum(
        """5 1 9 5
        7 5 3
        2 4 6 8"""
    ) == 18


if __name__ == '__main__':
    run_tests()
    digits = open('day_02_input.txt').read().strip()
    print(get_checksum(digits))
