#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_garbage_count(stream):
    garbage_count = 0
    ignore_next_character = False
    garbage = False

    for char in stream:
        if ignore_next_character:
            ignore_next_character = False
        elif char == '!':
            ignore_next_character = True
        elif garbage:
            if char == '>':
                garbage = False
            else:
                garbage_count += 1
        elif char == '<':
            garbage = True

    return garbage_count


def run_tests():
    assert get_garbage_count('{}') == 0
    assert get_garbage_count('{{{}}}') == 0
    assert get_garbage_count('{{},{}}') == 0
    assert get_garbage_count('{{{},{},{{}}}}') == 0
    assert get_garbage_count('{<a>,<a>,<a>,<a>}') == 4
    assert get_garbage_count('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 8
    assert get_garbage_count('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 0
    assert get_garbage_count('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 17


if __name__ == '__main__':
    run_tests()
    print(get_garbage_count(open('day_09_input.txt').read()))
