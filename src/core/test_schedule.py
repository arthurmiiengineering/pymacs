'''Test the function scheduling system.'''

# Standard library imports.
import unittest

# Project imports.
from schedule import Schedule


class TestSchedule(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule()

    def test_registration(self):
        '''Testing the addition of functions to the handlers list.'''
        self.schedule.register('test', function)
        with self.subTest('Function is registered.'):
            self.assertEqual(
                self.schedule.run('test', 'hello'),
                ['hello']
            )

        self.schedule.unregister('test', function)
        with self.subTest('Function is removed from the registry.'):
            self.assertEqual(
                self.schedule.run('test', 'hello'),
                []
            )


def function(context):
    return context


def main() -> None:
    '''Run all tests.'''
    unittest.main()


if __name__ == '__main__':
    main()