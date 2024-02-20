'''A function schedule, allowing control of the call order of the functions in the system.'''

# Standard library import.
from enum import auto, StrEnum
from collections import defaultdict


class Routine(StrEnum):
    '''A set of steps the main process will go through.'''
    START = auto()
    UPDATE = auto()
    RENDER = auto()
    FINISH = auto()


class Schedule:
    '''A registry that manages the call order of a group of functions, under a routine name.'''
    def __init__(self):
        self.systems = defaultdict(list)

    def register(self, routine, system, priority=1000):
        system._priority = priority
        self.systems[routine].append(system)
        return self

    def unregister(self, routine, system):
        self.systems[routine].remove(system)
        return self

    def run(self, routine, context):
        schedule = sorted(
            self.systems[routine],
            key=lambda system: system._priority,
            reverse=True
        )
        return [system(context) for system in schedule]

schedule = Schedule()