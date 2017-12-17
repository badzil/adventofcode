#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def spinlock(steps):
    l = [0]
    idx = 0
    for step in range(1, 2018):
        idx = (idx + steps) % len(l) + 1
        l.insert(idx, step)
    return l[idx + 1]


def run_tests():
    assert spinlock(3) == 638


if __name__ == '__main__':
    run_tests()
    print(spinlock(329))
