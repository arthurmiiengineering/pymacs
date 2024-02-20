import os
from os import system as sh
from dataclasses import dataclass, field

from core.broker import broker
from core.schedule import schedule, Routine


manual = '''cmds:
    ~ man(m): display the manual
    ~ shell($): access the system shell prompt
    ~ load(l): load a file into the buffer. creates a new buffer if valid file not found
    ~ show(s): displays the entire buffer
    ~ insert(i): takes a number of lines and appends them to the end of the document
    ~ replace(r): replaces a line by index
    ~ delete(d): deletes a line
    ~ clear(c): deletes all the lines in the buffer
    ~ write(w): saves the current buffer
    ~ quit(q): quits pyed
'''


def load(filename):
    buffer = list()
    if not os.path.exists(filename): return buffer
    with open(f'{filename}', 'r') as f:
        line = f.readline()
        while line:
            buffer.append(line.rstrip('\n'))
            line = f.readline()
    return buffer


buffer = list()
def text_edit(event):
    global buffer
    match event:
        case 'manual'|'m': print(manual)
        case 'shell'|'$': sh(input('$ '))
        case 'load'|'l':
            filename = input('name? : ')
            buffer = load(filename)
        case 'show'|'s':
            for i in range(len(buffer)):
                print(str(i + 1) + " | " + buffer[i])
        case 'insert'|'i':
            quantity = int(input('how many lines? : '))
            [buffer.append(input()) for i in range(quantity)]
        case 'replace'|'r':
            linenum = int(input('what line? : '))
            print(f'replacing line {linenum}: "{buffer[linenum - 1].strip()}" . . .')
            buffer[linenum - 1] = input()
        case 'delete'|'d':
            linenum = int(input('what line? : '))
            del buffer[linenum - 1]
        case 'clear'|'c': buffer.clear()
        case 'write'|'w':
            with open(f'{filename}', 'w') as f:
                f.write('\n'.join(buffer))
        case 'quit'|'q': quit()
        case _: print('cmd not recognized. please enter a valid cmd.')


def register():
    cmds = [
        'manual',
        'm',
        'shell',
        '$',
        'load',
        'l',
        'show',
        's',
        'insert',
        'i',
        'replace',
        'r',
        'delete',
        'd',
        'clear',
        'c',
        'write',
        'w',
        'quit',
        'q'
    ]
    broker.register(
        *cmds,
        handler=text_edit
    )

'''
can create and execute lambdas?
at each stage check validity
self documenting via the docstrings and the __doc__ attribute

@knowncmd
def processcmd(data, sep1 = ';', sep2 = '-', sep3 = '/'):
    cmds = []

    data1 = data.split(sep1)
    for i in data1:
        data2 = i.split(sep2)
        cmdcount = 0
        for j in data2:
            data3 = j.split(sep3)
            currentindex = len(cmds)
            cmds.append([])
            for c in data3: cmds[currentindex].append(c)
            if cmdcount > 0:
                cmds[currentindex].append('sysout')
            cmdcount += 1
    return cmds
cmdmanuals['processcmd'] = 'descr: parses commands into segmented chunks according to the set division character\n  -args:\n    data: the cmd to be parsed\n    sep1: 1st division character, which marks the division between unrelated cmds on the same line\n      default: ";"\n    sep2: marks the division between related cmds being piped together\n      default: "-"\n    sep3: marks the division between the cmd and its arguments\n      default: "/"\n  -returns:\n    cmds: string of formated cmds and their arguments'

sysout = None
@knowncmd
def execmd(*cmds):
    sysout = None
    for c in cmds:
        if c[0] not in knowncmds: print(f'command {c[0]} not recognized'); return
        elif c[-1] == 'sysout':
            del c[-1]
            c.append(sysout)
            sysout = knowncmds[c[0]](*c[1::])
            if sysout == 'ERROR': return 'ERROR'
        else:
            sysout = knowncmds[c[0]](*c[1::])
            if sysout == 'ERROR': return 'ERROR'
'''