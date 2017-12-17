#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def spinlock(steps):
    idx = 0
    value_after_zero = None
    for step in range(1, 50000001):
        idx = (idx + steps) % step + 1
        if idx == 1:
            value_after_zero = step
    return value_after_zero


if __name__ == '__main__':
    print(spinlock(329))
