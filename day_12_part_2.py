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


def get_groups(pipes):
    groups = []
    for program in pipes:
        for group in groups:
            if program in group:
                break
        else:
            c = ProgramCounter(pipes)
            c.count(program)
            groups.append(c.seen_programs)
    return len(groups)


def run_tests():
    pipes = read_pipes("""0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""")
    assert get_groups(pipes) == 2


if __name__ == '__main__':
    run_tests()
    pipes = read_pipes(open('day_12_input.txt').read().strip())
    print(get_groups(pipes))
