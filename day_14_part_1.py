#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from day_10_part_2 import knot_hash


def hex_to_binary(digit):
    return bin(int(digit, 16))[2:].zfill(4)


def run_tests():
    assert hex_to_binary('0') == '0000'
    assert hex_to_binary('1') == '0001'
    assert hex_to_binary('e') == '1110'


if __name__ == '__main__':
    run_tests()

    s = 'stpzcrnm'
    c = 0
    for i in range(128):
        h = knot_hash(s + '-' + str(i))
        b = hex_to_binary(h)
        c += b.count('1')
    print(c)
