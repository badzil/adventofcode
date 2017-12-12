#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ProgramCounter(object):

    def __init__(self, pipes):
        self.pipes = pipes
        self.seen_programs = set()

    def count(self, program):
        self.seen_programs.add(program)
        for connected_program in self.pipes[program]:
            if connected_program not in self.seen_programs:
                self.count(connected_program)


def read_pipes(txt):
    pipes = {}
    for line in txt.split('\n'):
        program, connected_programs = line.split(' <-> ')
        program = int(program)
        connected_programs = [int(p) for p in connected_programs.split(', ')] 
        pipes[program] = connected_programs
    return pipes


def count_connected_programs(input_txt):
    pipes = read_pipes(input_txt)
    c = ProgramCounter(pipes)
    c.count(0)
    return len(c.seen_programs)


def run_tests():
    input_txt = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""
    assert count_connected_programs(input_txt) == 6


if __name__ == '__main__':
    run_tests()
    input_txt = open('day_12_input.txt').read().strip()
    print(count_connected_programs(input_txt))
