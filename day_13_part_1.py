#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def read_layers(input_txt):
    layers = {}
    for line in input_txt.strip().split('\n'):
        depth, range = line.split(': ')
        layers[int(depth)] = int(range)
    return layers


def get_severity(layers):
    # pos is both the scanner position (% the range of the current layer)
    # and the position of the packet.
    severity = 0
    for pos in range(max(layers) + 1):
        if pos not in layers:
            continue
        scanner_pos = pos % (2 * (layers[pos] - 1))
        if scanner_pos == 0:
            severity += pos * layers[pos]
    return severity


def run_tests():
    input_txt = """0: 3
1: 2
4: 4
6: 4"""
    layers = read_layers(input_txt)
    assert get_severity(layers) == 24


if __name__ == '__main__':
    run_tests()
    input_txt = open('day_13_input.txt').read().strip()
    layers = read_layers(input_txt)
    print(get_severity(layers))
