'''Main app and initialization.'''

# Standard libary imports.
import sys
from dataclasses import dataclass

# Project imports.
from core import extensions
from core.broker import broker
from core.schedule import schedule, Routine


@dataclass
class AppData:
    '''A representation of the global app data.'''
    prompt: str


def main(data) -> None:
    '''Primary function responsible for running the application.'''
    schedule.run(Routine.START, data)
    while True:
        if (cmd := input(data.prompt)) in ['q', 'quit']: break
        broker.send(cmd); broker.dispatch()

        schedule.run(Routine.UPDATE, data)
        schedule.run(Routine.RENDER, data)
    schedule.run(Routine.FINISH, data)


app_data = AppData('cmd: ')
if __name__ == '__main__':
    '''Load extensions and run the application.'''
    extensions.load()
    main(data)