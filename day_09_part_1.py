#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_total_score(stream):
    score = 0
    current_level = 0
    ignore_next_character = False
    garbage = False

    for char in stream:
        if ignore_next_character:
            ignore_next_character = False
        elif char == '!':
            ignore_next_character = True
        elif char == '<':
            garbage = True
        elif garbage:
            if char == '>':
                garbage = False
        elif char == '{':
            current_level += 1
        elif char == '}':
            score += current_level
            current_level -= 1

    return score


def run_tests():
    assert get_total_score('{}') == 1
    assert get_total_score('{{{}}}') == 6
    assert get_total_score('{{},{}}') == 5
    assert get_total_score('{{{},{},{{}}}}') == 16
    assert get_total_score('{<a>,<a>,<a>,<a>}') == 1
    assert get_total_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert get_total_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert get_total_score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3


if __name__ == '__main__':
    run_tests()
    print(get_total_score(open('day_09_input.txt').read()))
