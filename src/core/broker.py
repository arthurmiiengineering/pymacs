'''A simple event handler class.'''

# Standard library imports.
from collections import defaultdict, deque
from dataclasses import dataclass, field


@dataclass
class Broker:
    '''An event handler, which manages a list of handlers, and a queue.'''
    def __post_init__(self):
        self.handlers = defaultdict(list)
        self.queue = deque()

    def handle(self, *events):
        def wrapper(handler):
            for event in events:
                self.handlers[event].append(handler)
        return wrapper

    def register(self, *events, handler):
        for event in events:
            self.handlers[event].append(handler)

    def unregister(self, event, handler):
        self.handlers[event].remove(handler)

    def send(self, event, **kwargs):
        return [handler(event=event, **kwargs) for handler in self.handlers[event]]

    def publish(self, event, **kwargs):
        self.queue.append((event, kwargs))

    def dispatch(self):
        queue = self.queue.copy()
        self.queue.clear()
        response = list()
        for event, kwargs in queue:
            response.extend(
                [handler(event=event, **kwargs) for handler in self.handlers[event]]
            )
        return response

broker = Broker()