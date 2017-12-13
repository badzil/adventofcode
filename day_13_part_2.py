#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


def read_layers(input_txt):
    layers = {}
    for line in input_txt.strip().split('\n'):
        depth, range = line.split(': ')
        layers[int(depth)] = int(range)
    return layers

class Caught(Exception):
    pass


def cross_firewall(layers, delay=0):
    # pos is both the scanner position (% the range of the current layer)
    # and the position of the packet.
    for layer_depth, layer_range in layers.items():
        scanner_pos = (layer_depth + delay) % (2 * (layer_range - 1))
        if scanner_pos == 0:
            raise Caught(layer_depth)


def cross_firewall_with_delay(layers):
    for delay in itertools.count():
        try:
            cross_firewall(layers, delay)
            break
        except Caught, exc:
            pass
    return delay


def run_tests():
    input_txt = """0: 3
1: 2
4: 4
6: 4"""
    layers = read_layers(input_txt)
    assert cross_firewall_with_delay(layers) == 10


if __name__ == '__main__':
    run_tests()
    input_txt = open('day_13_input.txt').read().strip()
    layers = read_layers(input_txt)
    print(cross_firewall_with_delay(layers))
