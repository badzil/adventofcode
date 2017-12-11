#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

NE = 'ne'
SE = 'se'
S = 's'
SW = 'sw'
NW = 'nw'
N = 'n'


COMBINE_STEPS = [
    (NE, S, SE),
    (SE, SW, S),
    (S, NW, SW),
    (SW, N, NW),
    (NW, NE, N),
    (N, SE, NE),
    (NE, SW, None),
    (SE, NW, None),
    (S, N, None),
]


def get_shortest_path(steps):
    step_counts = Counter(steps.split(','))
    while True:
        new_step_counts = combine_steps(step_counts)
        if new_step_counts == step_counts:
            break
        step_counts = new_step_counts
    return sum(step_counts.values())


def combine_steps(step_counts):
    new_step_counts = Counter(step_counts)
    for step_a, step_b, combine_step in COMBINE_STEPS:
        if step_a in new_step_counts and step_b in new_step_counts:
             min_steps = min(new_step_counts[step_a], new_step_counts[step_b])
             new_step_counts[step_a] -= min_steps
             new_step_counts[step_b] -= min_steps
             if combine_step is not None:
                 new_step_counts[combine_step] += min_steps
    return new_step_counts


def run_tests():
    assert get_shortest_path('ne,ne,ne') == 3
    assert get_shortest_path('ne,ne,sw,sw') == 0
    assert get_shortest_path('ne,ne,s,s') == 2
    assert get_shortest_path('se,sw,se,sw,sw') == 3


if __name__ == '__main__':
    run_tests()
    steps = open('day_11_input.txt').read().strip()
    print(get_shortest_path(steps))
