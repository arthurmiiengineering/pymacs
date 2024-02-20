'''A function to register any extensions in the configuration file.'''

# Standard library imports.
import json
import importlib


def load() -> None:
    '''Imports plugins specified in the config and runs the register method.'''
    with open('config.json') as file:
        extensions = json.load(file)
    for directory, modules in extensions.items():
        for module in modules:
            extension = importlib.import_module(f'extensions.{directory}.{module}')
            extension.register()