'''Test the event handling capability.'''

# Standard library imports.
import unittest

# Project imports.
from broker import Broker


class TestBroker(unittest.TestCase):
    def setUp(self):
        self.broker = Broker()

    def test_registration(self):
        '''Testing the addition of functions to the handlers list.'''
        self.broker.register('hello', handler=handler)
        with self.subTest('Function is registered.'):
            self.assertEqual(
                self.broker.send('hello'),
                ['hello']
            )

        self.broker.unregister('hello', handler)
        with self.subTest('Function is removed from the registry.'):
            self.assertEqual(
                self.broker.send('hello'),
                []
            )

    def test_dispatch(self):
        '''Testing the dispatching of events from the queue.'''
        self.broker.register('hello', handler=handler)
        self.broker.publish('hello')
        self.assertEqual(
            self.broker.dispatch(),
            ['hello']
        )


def handler(event):
    return event


def main() -> None:
    '''Run all tests.'''
    unittest.main()


if __name__ == '__main__':
    main()